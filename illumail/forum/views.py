from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, CreateView
from forum.models import ForumSection, ForumSubsection, ForumCommunication
from forum.forms import CommForm, CreateSubsection


class ShowSection(CreateView):
    model = ForumSection
    template_name = 'sections.html'
    extra_context = {'title': 'Форум:Разделы'}
    fields = ['section', ]

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(reverse('show_section'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sections'] = ForumSection.objects.all()
        return context


class ShowSubsections(CreateView):
    model = ForumSubsection
    template_name = 'subsections.html'
    extra_context = {'title': 'Форум:Темы'}
    fields = ['subsection', ]

    def form_valid(self, form):
        fs = form.save(commit=False)
        fs.section_id = self.kwargs['pk']
        fs.save()
        return HttpResponseRedirect(reverse('show_subsections', args=[self.kwargs['pk']]))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subsections'] = ForumSubsection.objects.filter(section_id=self.kwargs['pk'])
        # context['last_comm'] = [*i.comm_text for i in ForumCommunication.objects.filter(subsection_id=self.kwargs['pk']).order_by('-id')[:1]]
        return context


class ShowCommunication(CreateView):
    model = ForumCommunication
    template_name = 'forum.html'
    extra_context = {'title': 'Форум:Обсуждение'}
    form_class = CommForm

    def form_valid(self, form):
        fs = form.save(commit=False)
        fs.user = self.request.user
        fs.subsection_id = self.kwargs['pk']
        fs.save()
        return HttpResponseRedirect(reverse('show_communication', args=[self.kwargs['pk']]))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subsection'] = ForumSubsection.objects.get(id=self.kwargs['pk'])
        context['comments'] = ForumCommunication.objects.filter(subsection_id=self.kwargs['pk']).order_by('-id')
        return context




