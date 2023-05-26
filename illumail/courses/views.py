from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from courses.templatetags import news_tags
from study_groups.models import StudyGroup
from users.models import CustomUser
from .models import Courses, Posts, CompletedTaskModel, Category, Comments
from .forms import *
from django.views.generic import ListView, DeleteView, UpdateView, DetailView, CreateView, TemplateView


class ShowCourses(ListView):
    model = Courses
    template_name = 'courses.html'
    context_object_name = 'courses'
    extra_context = {'title': 'Курсы', 'subtitle': 'Все курсы'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Courses.objects.all()
        context['categories'] = Category.objects.all()
        context['sort'] = self.request.GET.get('sort')
        if context['sort'] == ('new'):
            return Courses.objects.order_by('-time_created')
        if context['sort'] == ('old'):
            return Courses.objects.order_by('time_created')
        return context


class SortCourses(ListView):
    model = Courses
    template_name = 'courses.html'
    context_object_name = 'courses'

    def get_queryset(self):
        sort = self.request.GET.get('sort')
        if sort == 'new':
            return Courses.objects.order_by('-time_created')
        if sort == 'old':
            return Courses.objects.order_by('time_created')
        if sort == 'cheap':
            return Courses.objects.order_by('type_course')
        if sort == 'expensive':
            return Courses.objects.order_by('-type_course', '-time_created')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class FilterCourses(ListView):
    model = Courses
    template_name = 'courses.html'
    context_object_name = 'courses'

    def get_queryset(self):
        filtration = self.request.GET.get('filter')
        if filtration == 'free':
            return Courses.objects.filter(type_course='1').order_by('-time_created')
        if filtration == 'payment':
            return Courses.objects.filter(type_course='2').order_by('-time_created')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class ShowPosts(CreateView):
    model = Posts
    template_name = 'courses_posts.html'
    extra_context = {'title': 'Информция'}
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
        fs = form.save(commit=False)
        fs.quiz_id = Quiz.objects.get(pk=self.kwargs['test_id']).id
        fs.user_id = self.request.user.id
        fs.save()
        return HttpResponseRedirect(reverse('show_posts', args=[fs.quiz_id.id]))

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
        return redirect('show_courses')


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
    return render(request, 'courses.html', {'courses': courses, 'subtitle': category.title, 'categories': categories})


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
