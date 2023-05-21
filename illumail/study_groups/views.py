from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from users.models import CustomUser
from .models import PostsInStudyGroup, StudyGroup, Valuation
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
            return HttpResponseRedirect(reverse('show_posts_group', args=[post.study_group.pk]))
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


def leave_the_group(request, pk):
    StudyGroup.objects.get(id=pk).customuser_set.remove(request.user)
    return HttpResponseRedirect(reverse('learning'))


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


class ShowValuations(CreateView):
    form_class = UpdateValuations
    template_name = 'compl_works.html'
    extra_context = {'title': 'Оценки', 'subtitle': 'Работы и оценки учащихся'}

    def form_valid(self, form):
        fs = form.save(commit=False)
        fs.post_id = self.kwargs['post_id']
        fs.user_id = self.request.user.id
        fs.save()
        return HttpResponseRedirect(reverse('show_valuations', args=[self.kwargs['pk'], self.kwargs['post_id']]))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['compl_works'] = CompletedTaskInStudyGroup.objects.filter(post_id=PostsInStudyGroup.objects.get(pk=self.kwargs['post_id']))
        return context


def show_valuations(request, pk, post_id):
    study_group = StudyGroup.objects.get(pk=pk)
    compl_works = CompletedTaskInStudyGroup.objects.filter(post_id=PostsInStudyGroup.objects.get(pk=post_id))
    form = UpdateValuations()
    if request.method == "POST":
        form = UpdateValuations(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('show_valuations', args=[study_group.id, post_id]))
    return render(request, 'compl_works.html', {'study_group': study_group, 'compl_works': compl_works, 'form': form})


def save_update_valuations(request, pk, post_id, work_id):
    study_group = StudyGroup.objects.get(pk=pk)
    compl_works = CompletedTaskInStudyGroup.objects.filter(post_id=PostsInStudyGroup.objects.get(pk=post_id))
    work = CompletedTaskInStudyGroup.objects.get(pk=work_id)
    if request.method == "POST":
        form = UpdateValuations(request.POST, request.FILES, instance=work)
        if form.is_valid():
            fs = form.save(commit=False)
            fs.post_id = PostsInStudyGroup.objects.get(pk=post_id).id #?
            fs.grade = form.cleaned_data['grade']
            fs.save()
    return HttpResponseRedirect(reverse('show_valuations', args=[study_group.id, post_id]))
