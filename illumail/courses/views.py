from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from .models import Courses, Posts, CompletedTaskModel
from .forms import ComplitedTaskForm, CreateOrUpdateCourseForm
from django.views.generic import ListView, DeleteView, UpdateView, DetailView, CreateView


class ShowCourses(ListView):
    model = Courses
    template_name = 'courses.html'
    context_object_name = 'courses'
    extra_context = {'title': 'Курсы'}


def show_posts(request, course_id):
    course = Courses.objects.get(id=course_id)
    posts = Posts.objects.filter(course_id=course_id)
    return render(request, 'courses_posts.html', {'posts': posts, 'course': course})


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
    extra_context = {'title': 'Поиск курсов'}

    def get_queryset(self):
        return Courses.objects.filter(title__icontains=self.request.GET.get('search', ''))


class Teaching(ListView):
    model = Courses
    template_name = 'teaching.html'
    context_object_name = 'courses'
    extra_context = {'title': 'Преподавание'}
