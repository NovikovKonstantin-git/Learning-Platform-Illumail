from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView
from users.models import CustomUser
from .models import PostsInStudyGroup, StudyGroup
from study_groups.forms import *


class ShowPostsGroups(ListView):
    model = PostsInStudyGroup
    template_name = 'study_group.html'
    extra_context = {'title': 'Учебная группа', 'subtitle': 'Группа'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = PostsInStudyGroup.objects.filter(study_group_id=self.kwargs['pk'])
        # для вывод инфы о группе и для вывода кнопок управления
        context['study_group'] = StudyGroup.objects.get(id=self.kwargs['pk'])

        context['is_followed'] = False
        if StudyGroup.objects.get(id=self.kwargs['pk']) in CustomUser.objects.get(id=self.request.user.id).user_groups.all():
            context['is_followed'] = True
        else:
            context['is_followed'] = False
        return context


def show_specific_task(request, pk, post_id):
    posts_in_group = PostsInStudyGroup.objects.filter(study_group_id=pk)
    post = PostsInStudyGroup.objects.get(id=post_id)

    if request.method == "POST":
        form = ComplitedTaskGroupForm(request.POST, request.FILES)
        files = request.FILES.getlist('file')
        if form.is_valid():
            for f in files:
                file_instance = CompletedTaskInStudyGroup(file=f)
                file_instance.user = request.user
                file_instance.post = post
                file_instance.save()
            return HttpResponseRedirect(reverse('show_posts_group', args=[post.id]))
    else:
        form = ComplitedTaskGroupForm()

    context = {
        'posts_in_group': posts_in_group,
        'post': post,
        'form': form,
    }
    return render(request, 'specific_task.html', context)


def delete_task(request, pk, post_id):
    study_group = StudyGroup.objects.get(id=pk)
    task = PostsInStudyGroup.objects.get(id=post_id)
    task.delete()
    return HttpResponseRedirect(reverse('show_posts_group', args=[study_group.id]))

