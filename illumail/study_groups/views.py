from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from users.models import CustomUser
from .models import PostsInStudyGroup, StudyGroup
from .forms import *


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


class CreateGroup(CreateView):
    form_class = CreateOrUpdateGroupForm
    template_name = 'create_group.html'
    success_url = reverse_lazy('teaching')
    extra_context = {'title': 'Создание группы'}

    def form_valid(self, form):
        fs = form.save(commit=False)
        fs.author = self.request.user
        fs.save()
        return redirect('teaching')


class UpdateGroup(UpdateView):
    form_class = CreateOrUpdateGroupForm
    template_name = 'update_group.html'
    extra_context = {'title': 'Изменить группу'}
    context_object_name = 'group'
    queryset = StudyGroup.objects.all()

    def form_valid(self, form):
        fs = form.save(commit=False)
        fs.author = self.request.user
        fs.save()
        return redirect('teaching')


def delete_group(request, pk):
    group = StudyGroup.objects.get(id=pk)
    group.delete()
    return HttpResponseRedirect(reverse('teaching'))


class CreateTask(CreateView):
    form_class = CreateOrUpdatePostForm
    template_name = 'create_new_task.html'
    extra_context = {'title': 'Создание задания'}

    def form_valid(self, form):
        fs = form.save(commit=False)
        fs.study_group_id = self.kwargs['study_group_id']
        fs.save()
        return redirect('show_posts_group', pk=fs.study_group_id)


class ShowStudents(ListView):
    model = StudyGroup
    template_name = 'students.html'
    extra_context = {'title': 'Учащиеся', 'subtitle': 'Учащиеся данной группы'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_users'] = CustomUser.objects.all()
        context['students'] = StudyGroup.objects.get(id=self.kwargs['pk']).customuser_set.all()
        return context
