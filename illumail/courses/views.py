from django.shortcuts import render, redirect
from .models import Courses, Posts, CompletedTaskModel
from .forms import ComplitedTaskForm


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


