from django.shortcuts import render
from .models import *


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


# def show_specific_task(request, post_id):
#     posts = Posts.objects.get(pk=post_id)
#     context = {
#         'posts': posts,
#         "title": f"Задание {post_id}",
#     }
#     return render(request, 'specific_task.html', context)

def show_specific_task(request, course_id, post_id):
    posts = Posts.objects.get(pk=post_id)
    course = Courses.objects.get(pk=course_id)
    context = {
        'posts': posts,
        "title": f"Задание {post_id}",
    }
    return render(request, 'specific_task.html', context)
