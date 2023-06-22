from django.conf import settings
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from courses.templatetags import news_tags
from study_groups.models import StudyGroup
from users.models import CustomUser
from .models import Courses, Posts, CompletedTaskModel, Category, Comments, Progress, Quiz
from .forms import *
from django.views.generic import ListView, DeleteView, UpdateView, DetailView, CreateView, TemplateView
from django.contrib import messages


class ShowCourses(ListView):
    model = Courses
    template_name = 'courses.html'
    context_object_name = 'courses'
    extra_context = {'title': 'Курсы', 'subtitle': 'Все курсы'}
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Courses.objects.all()
        context['categories'] = Category.objects.all()
        context['sort'] = self.request.GET.get('sort')
        context['paginate_by'] = self.paginate_by
        return context


class SortCourses(ListView):
    model = Courses
    template_name = 'courses.html'
    context_object_name = 'courses'
    extra_context = {'title': 'Курсы', 'subtitle': 'Курсы'}
    paginate_by = 100

    def get_queryset(self):
        sort = self.request.GET.get('sort')
        if sort == 'new':
            return Courses.objects.order_by('-time_created')
        if sort == 'old':
            return Courses.objects.order_by('time_created')
        if sort == 'cheap':
            return Courses.objects.order_by('type_course')
        if sort == 'expensive':
            return Courses.objects.order_by('-type_course')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class FilterCourses(ListView):
    model = Courses
    template_name = 'courses.html'
    context_object_name = 'courses'
    paginate_by = 100

    def get_queryset(self):
        filtration = self.request.GET.get('filter')
        if filtration == 'free':
            return Courses.objects.filter(type_course='1').order_by('-time_created')
        if filtration == 'payment':
            return Courses.objects.filter(type_course='2').order_by('type_course')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class ShowPosts(CreateView):
    model = Posts
    template_name = 'courses_posts.html'
    extra_context = {'title': 'Информация'}
    form_class = CommentForm

    def form_valid(self, form):
        fs = form.save(commit=False)
        fs.author = self.request.user
        fs.course_id = self.kwargs['course_id']
        fs.save()
        return HttpResponseRedirect(reverse('show_posts', args=[self.kwargs['course_id']]))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['course'] = Courses.objects.get(id=self.kwargs['course_id'])
        context['posts'] = Posts.objects.filter(course_id=self.kwargs['course_id'])
        context['tests'] = Quiz.objects.filter(course_id=self.kwargs['course_id'])
        context['comments'] = Comments.objects.filter(course_id=self.kwargs['course_id'])
        context['count_comments'] = len(Comments.objects.filter(course_id=self.kwargs['course_id']))
        try:
            context['progress'] = Progress.objects.get(course_id=self.kwargs['course_id'], user=self.request.user.id)
        except Exception:
            context['progress'] = 0
        context['good_tests'] = GoodTestModel.objects.filter(course_id=self.kwargs['course_id'])

        if len(Quiz.objects.filter(course=context['course'])) > 0:
            context['tasks'] = len(Quiz.objects.filter(course=context['course']))



        # список курсов у пользователя, чтобы потом исчезала кнопка "Вступить"
        if self.request.user.is_authenticated:
            context['user_courses'] = CustomUser.objects.get(username=self.request.user).user_courses.all()

            context['is_followed'] = False
            if Courses.objects.get(id=self.kwargs['course_id']) in CustomUser.objects.get(id=self.request.user.id).user_courses.all():
                context['is_followed'] = True
            else:
                context['is_followed'] = False
        return context


def show_specific_post(request, course_id, post_id):
    posts_in_course = Posts.objects.filter(course_id=course_id)
    post = Posts.objects.get(id=post_id)
    context = {
        'posts_in_course': posts_in_course,
        'post': post,
    }
    return render(request, 'specific_post.html', context)


class ShowSpecificTest(CreateView):
    form_class = AnswerForm
    template_name = 'specific_test.html'
    extra_context = {'title': 'Тест'}

    def form_valid(self, form):
        quiz = Quiz.objects.get(pk=self.kwargs['test_id'])
        fs = form.save(commit=False)
        fs.quiz_id = Quiz.objects.get(pk=self.kwargs['test_id']).id
        fs.user_id = self.request.user.id
        fs.save()
        if form.cleaned_data['user_answer'] == Quiz.objects.get(pk=fs.quiz_id).true_answer:
            messages.success(self.request, 'Результат записан. Верно.')
            progress, created = Progress.objects.get_or_create(user=self.request.user, course=Courses.objects.get(pk=self.kwargs['pk']), defaults={'progress': 0})
            if not created:
                if progress.progress < quiz.course.quiz_set.count():
                    progress = Progress.objects.get(user=self.request.user, course=Courses.objects.get(pk=self.kwargs['pk']))
                    progress.progress += 1
                    progress.save()
                else:
                    messages.error(self.request, 'Вы уже прошли этот тест, баллы не начислятся.')
            else:
                progress.progress += 1
                progress.save()
        else:
            messages.success(self.request, 'Результат записан. Неверно.')
        return HttpResponseRedirect(reverse('show_posts', args=[Courses.objects.get(pk=self.kwargs['pk']).id]))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['course'] = Courses.objects.get(pk=self.kwargs['pk'])
        context['test'] = Quiz.objects.get(pk=self.kwargs['test_id'])
        return context


class CreateCourse(CreateView):
    form_class = CreateOrUpdateCourseForm
    template_name = 'create_course.html'
    success_url = reverse_lazy('teaching')
    extra_context = {'title': 'Создание курса'}

    def form_valid(self, form):
        fs = form.save(commit=False)
        fs.author = self.request.user
        fs.save()
        return redirect('show_courses')


class UpdateCourse(UpdateView):
    form_class = CreateOrUpdateCourseForm
    template_name = 'update_course.html'
    extra_context = {'title': 'Изменить курс'}
    context_object_name = 'course'
    queryset = Courses.objects.all()

    def form_valid(self, form):
        fs = form.save(commit=False)
        fs.author = self.request.user
        fs.save()
        return HttpResponseRedirect(reverse('show_posts', args=[self.kwargs['pk']]))


def delete_course(request, pk):
    course = Courses.objects.get(id=pk)
    course.delete()
    return HttpResponseRedirect(reverse('teaching'))


class SearchCourse(ListView):
    model = Courses
    template_name = 'search_courses.html'
    context_object_name = 'courses'
    extra_context = {'title': 'Поиск курсов', 'subtitle': 'По Вашему запросу найдено:'}

    def get_queryset(self):
        return Courses.objects.filter(title__icontains=self.request.GET.get('search', ''))


class Teaching(ListView):
    model = Courses
    template_name = 'teaching.html'
    extra_context = {'title': 'Преподавание'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Courses.objects.filter(author=self.request.user.id)
        context['groups'] = StudyGroup.objects.filter(author=self.request.user.id)
        return context


def category_courses(request, category_id):
    category = Category.objects.get(id=category_id) # для получения тайтла, чтобы перредать в сабтайтл
    courses = Courses.objects.filter(category_id=category_id)
    categories = Category.objects.all()  # для вывода категорий, не только на главной странице, но и в категориях курсов
    paginator = Paginator(courses, 3)
    page_num = request.GET.get('page', 1)
    page_objects = paginator.get_page(page_num)
    return render(request, 'courses.html', {'courses': courses, 'subtitle': category.title, 'categories': categories, 'page_obj': page_objects})


class Learning(ListView):
    model = CustomUser
    template_name = 'learning.html'
    extra_context = {'title': 'Обучение', 'subtitle': 'Изучаемые курсы:'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_courses'] = CustomUser.objects.get(id=self.request.user.id).user_courses.all()
        context['user_groups'] = CustomUser.objects.get(id=self.request.user.id).user_groups.all()
        return context


def join_the_course(request, pk):
    Courses.objects.get(id=pk).customuser_set.add(request.user)
    return HttpResponseRedirect(reverse('learning'))


def leave_the_course(request, pk):
    Courses.objects.get(id=pk).customuser_set.remove(request.user)
    return HttpResponseRedirect(reverse('learning'))


class ShowNews(TemplateView):
    template_name = 'news.html'
    extra_context = {'title': 'Новости', 'subtitle': 'Актуальные новости в сфере образования:'}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news'] = news_tags.itog
        return context


class CreatePost(CreateView):
    form_class = CreateOrUpdatePostForm
    template_name = 'create_task.html'
    extra_context = {'title': 'Создание задания'}

    def form_valid(self, form):
        fs = form.save(commit=False)
        fs.course_id = self.kwargs['course_id']
        fs.save()
        return HttpResponseRedirect(reverse('show_posts', args=[fs.course_id]))


def delete_post(request, pk, post_id):
    course = Courses.objects.get(id=pk)
    post = Posts.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect(reverse('teaching'))


class CreateTest(CreateView):
    form_class = CreateTestForm
    template_name = 'create_quiz.html'
    extra_context = {'title': 'Создание теста'}

    def form_valid(self, form):
        fs = form.save(commit=False)
        fs.course_id = self.kwargs['pk']
        fs.save()
        return HttpResponseRedirect(reverse('show_posts', args=[fs.course_id]))


def redirectik(request):
    return redirect('show_courses')


"""Unrealize"""
def create_test(request):
    if request.method == 'POST':
        test_form = TestingForm(request.POST)
        question_forms = [QuestionForm(request.POST, prefix=str(x), instance=Question()) for x in range(int(request.POST['question_count']))]
        answer_forms = [ReplyForm(request.POST, prefix=str(x), instance=Reply()) for x in range(int(request.POST['answer_count']))]

        if test_form.is_valid() and all([qf.is_valid() for qf in question_forms]) and all([af.is_valid() for af in answer_forms]):
            test = test_form.save()
            for qf in question_forms:
                question = qf.save(commit=False)
                question.test = test
                question.save()
                for af in answer_forms:
                    answer = af.save(commit=False)
                    answer.question = question
                    answer.save()

            return redirect('test_list')

    else:
        test_form = TestingForm()
        question_forms = [QuestionForm(prefix=str(x), instance=Question()) for x in range(5)]
        answer_forms = [ReplyForm(prefix=str(x), instance=Answer()) for x in range(20)]

    return render(request, 'create_test.html', {'test_form': test_form, 'question_forms': question_forms, 'answer_forms': answer_forms})


class GoodTest(CreateView):
    model = GoodTestModel
    template_name = 'course_test.html'
    extra_context = {'title': 'Тест'}
    form_class = GoodAnswerForm

    def form_valid(self, form):
        # fs = form.save(commit=False)
        form.save()
        return HttpResponseRedirect(reverse('show_courses'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['questions'] = QuestionModel.objects.filter(test_id=self.kwargs['pk'])
        return context


def save_user_answer(request, pk, question_id):
    course = Courses.objects.get(pk=pk)
    # test = GoodTest.objects.get(pk=pk)
    form = GoodAnswerForm()
    if request.method == "POST":
        form = GoodAnswerForm(request.POST)
        if form.is_valid():
            fs = form.save(commit=False)
            fs.question_id = QuestionModel.objects.get(pk=question_id).id
            fs.user_id = request.user.id
            fs.user_answer = form.cleaned_data['user_answer']
            fs.save()
    return HttpResponseRedirect(reverse('show_posts', args=[course.id])) # edit this


