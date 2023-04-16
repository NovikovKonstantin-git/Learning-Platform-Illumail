from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from courses.templatetags import news_tags
from users.models import CustomUser
from .models import Courses, Posts, CompletedTaskModel, Category
from .forms import ComplitedTaskForm, CreateOrUpdateCourseForm, CreateOrUpdatePostForm
from django.views.generic import ListView, DeleteView, UpdateView, DetailView, CreateView, TemplateView


class ShowCourses(ListView):
    model = Courses
    template_name = 'courses.html'
    context_object_name = 'courses'
    extra_context = {'title': 'Курсы', 'subtitle': 'Все курсы'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class ShowPosts(ListView):
    model = Posts
    template_name = 'courses_posts.html'
    extra_context = {'title': 'Информция'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['course'] = Courses.objects.get(id=self.kwargs['course_id'])
        context['posts'] = Posts.objects.filter(course_id=self.kwargs['course_id'])
        return context


# class ShowThePostAndCompletedTasks(UpdateView):
#     model = Posts
#     pk_url_kwarg = 'post_id'
#     form_class = ComplitedTaskForm
#     template_name = 'specific_post.html'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['posts_in_course'] = Posts.objects.filter(course_id=self.kwargs['course_id'])
#         context['post'] = Posts.objects.filter(id=self.kwargs['post_id'])
#
#     def form_valid(self, form):
#         files = self.request.FILES.getlist('file')
#         for f in files:
#             file_instance = CompletedTaskModel(file=f)
#             file_instance.user = self.request.user
#             file_instance.post = self.request.post[0]
#             file_instance.save()
#         return redirect('show_courses')


def show_specific_post(request, course_id, post_id):
    posts_in_course = Posts.objects.filter(course_id=course_id)
    post = Posts.objects.filter(id=post_id)

    if request.method == "POST":
        form = ComplitedTaskForm(request.POST, request.FILES)
        files = request.FILES.getlist('file')
        if form.is_valid():
            for f in files:
                file_instance = CompletedTaskModel(file=f)
                file_instance.user = request.user
                file_instance.post = post[0]
                file_instance.save()
            return redirect('show_courses')
    else:
        form = ComplitedTaskForm()

    context = {
        'posts_in_course': posts_in_course,
        'post': post,
        'form': form,
    }
    return render(request, 'specific_post.html', context)


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
    return HttpResponseRedirect(reverse('show_courses'))


class SearchCourse(ListView):
    model = Courses
    template_name = 'courses.html'
    context_object_name = 'courses'
    extra_context = {'title': 'Поиск курсов', 'subtitle': 'По Вашему запросу найдено:'}

    def get_queryset(self):
        return Courses.objects.filter(title__icontains=self.request.GET.get('search', ''))


class Teaching(ListView):
    model = Courses
    template_name = 'teaching.html'
    context_object_name = 'courses'
    extra_context = {'title': 'Преподавание'}


def category_courses(request, category_id):
    category = Category.objects.get(id=category_id) # для получения тайтла, чтобы перредать в сабтайтл
    courses = Courses.objects.filter(category_id=category_id)
    categories = Category.objects.all()  # для вывода категорий, не только на главной странице, но и в категориях курсов
    return render(request, 'courses.html', {'courses': courses, 'subtitle': category.title, 'categories': categories})


class Learning(ListView):
    template_name = 'learning.html'
    extra_context = {'title': 'Обучение', 'subtitle': 'Изучаемые курсы:'}
    context_object_name = 'user_courses'

    def get_queryset(self):
        return CustomUser.objects.get(id=self.request.user.id).user_courses.all()


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
        return redirect('teaching')


def delete_post(request, pk, post_id):
    course = Courses.objects.get(id=pk)
    post = Posts.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect(reverse('teaching'))

