from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Courses, Posts, CompletedTaskModel
from .forms import ComplitedTaskForm, CreateOrUpdateCourseForm


def show_courses(request):
    courses = Courses.objects.all()
    return render(request, 'courses.html', {'courses': courses})


def show_posts(request, course_id):
    posts = Posts.objects.filter(course_id=course_id)
    return render(request, 'courses_posts.html', {'posts': posts})


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
        'form': form
    }
    return render(request, 'specific_post.html', context)


def create_course(request):
    form = CreateOrUpdateCourseForm(request.POST, request.FILES)
    if request.method == "POST":
        if form.is_valid():
            fs = form.save(commit=False)
            fs.author = request.user
            fs.save()
            return redirect('show_courses')
    else:
        form = CreateOrUpdateCourseForm()
    return render(request, 'create_course.html', {'form': form})


def update_course(request, id):
    course = Courses.objects.get(id=id)
    form = CreateOrUpdateCourseForm(instance=course)
    if request.method == "POST":
        form = CreateOrUpdateCourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            fs = form.save(commit=False)
            fs.author = request.user
            fs.save()
            return redirect('show_courses')
    return render(request, 'update_course.html', {'form': form, 'course': course})


def delete_course(request, id):
    course = Courses.objects.get(id=id)
    course.delete()
    return HttpResponseRedirect(reverse('show_courses'))
