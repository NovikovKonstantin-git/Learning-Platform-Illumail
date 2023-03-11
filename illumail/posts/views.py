from django.shortcuts import render, redirect
from .models import *
from .forms import *


def show_all_courses(request):
    search_query = request.GET.get('search', '')
    if search_query:
        courses = Courses.objects.filter(title__icontains=search_query)
    else:
        courses = Courses.objects.all()
    context = {
        'courses': courses,
        "title": "Все курсы",
    }
    return render(request, 'all_courses.html', context)


def show_posts(request, course_id):
    posts = Posts.objects.filter(course_id=course_id)
    course_post = Courses.objects.get(pk=course_id)

    context = {
        'posts': posts,
        "title": "Задания",
        'course_post': course_post,
    }
    return render(request, 'posts.html', context)


def show_specific_task(request, course_id, post_id):
    posts = Posts.objects.get(pk=post_id)
    course = Courses.objects.get(pk=course_id)
    context = {
        'posts': posts,
        "title": f"Задание {post_id}",
    }
    return render(request, 'specific_task.html', context)


def create_course(request):
    if request.method == "POST":
        form = CreateCourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show_all_courses')
    else:
        form = CreateCourseForm()
    return render(request, 'add_course.html', {'form': form})


def join_the_course(request):
    return render(request, 'join_the_course.html')
