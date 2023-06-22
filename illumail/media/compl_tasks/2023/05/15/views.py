from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Comment
from .forms import AddCommentForm, UpdateCommentForm
from hotels.models import Hotel
from profiles.models import Profile


def show_comments(request, hotel_id):
    comments = Comment.objects.filter(hotel_id=hotel_id)
    return render(request, 'comments.html', {'comments': comments})


def create_comment(request):
    if request.method == 'POST':
        form = AddCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = User.objects.get(username=request.user)
            form.save()
            return redirect('show_hotels')
    else:
        form = AddCommentForm()
    return render(request, 'add_comment.html', {'form': form})


def delete_comment(request, hotel_id, id):
    comment = Comment.objects.filter(hotel_id=hotel_id)
    comment = Comment.objects.get(id=id)
    comment.delete()
    return redirect('show_hotels')


def update_comment(request, hotel_id, id):
    comment = Comment.objects.filter(hotel_id=hotel_id)
    comment = Comment.objects.get(id=id)
    form = UpdateCommentForm(instance=comment)
    if request.method == 'POST':
        form = UpdateCommentForm(request.POST, instance=comment)
        if form.is_valid():
            # save_form = form.save(commit=False)
            # save_form.author = User.objects.get(username=request.user)
            form.save()
            return redirect('show_hotels')
    return render(request, 'update_comment.html', {'form': form})
