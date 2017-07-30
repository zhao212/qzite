from django.shortcuts import render,get_object_or_404,redirect
from myresume.models import *
from myresume.forms import *
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView, ListView,DetailView,CreateView,UpdateView,DeleteView)
# Create your views here.
# class ResumeListView(LoginRequiredMixin,ListView):
#     template_name = 'myresume/my_resume.html'
#     context_object_name = 'basic_info_list'
#     def get_queryset(self):
#             return res_basic.objects.order_by('last_name')
#
# class ResumeListView(LoginRequiredMixin,ListView):
#     template_name = 'myresume/my_resume.html'
#     context_object_name = 'education_list'
#     def get_queryset(self):
#             return res_basic.objects.order_by('start_date')

class ResumeListView(LoginRequiredMixin,ListView):
    template_name = 'myresume/my_resume.html'
    context_object_name = 'basic_info_list'
    queryset = res_basic.objects.all()
    def get_context_data(self, **kwargs):
        context = super(ResumeListView, self).get_context_data(**kwargs)
        context['basic_info_list'] = res_basic.objects.filter(user=self.request.user)
        context['education_list'] = res_education.objects.filter(user=self.request.user)
        context['project_list'] = res_project.objects.filter(user=self.request.user)
        context['work_list'] = res_work.objects.filter(user=self.request.user)
        context['skill_list'] = res_skill.objects.filter(user=self.request.user)
        context['award_list'] = res_award.objects.filter(user=self.request.user)
        # And so on for more models
        return context

class WebResumeListView(LoginRequiredMixin,ListView):
    template_name = 'myresume/webcv.html'
    context_object_name = 'basic_info_list'
    queryset = res_basic.objects.all()
    def get_context_data(self, **kwargs):
        context = super(WebResumeListView, self).get_context_data(**kwargs)
        context['basic_info_list'] = res_basic.objects.filter(user=self.request.user)
        context['education_list'] = res_education.objects.filter(user=self.request.user)
        context['project_list'] = res_project.objects.filter(user=self.request.user)
        context['work_list'] = res_work.objects.filter(user=self.request.user)
        context['skill_list'] = res_skill.objects.filter(user=self.request.user)
        context['award_list'] = res_award.objects.filter(user=self.request.user)
        # And so on for more models
        return context

class BasicInfoUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirected_field_name = 'myresume/my_resume.html'
    form_class = ResBasicForm
    model = res_basic

class CreateBasicInfoView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirected_field_name = 'myresume/my_resume.html'
    form_class = ResBasicForm
    model = res_basic

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class BasicDeleteView(LoginRequiredMixin,DeleteView):
    model = res_basic
    success_url = reverse_lazy('myresume:resumepage')

class EduUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirected_field_name = 'myresume/my_resume.html'
    form_class = ResEduForm
    model = res_education

class CreateEduView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirected_field_name = 'myresume/my_resume.html'
    form_class = ResEduForm
    model = res_education

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class EduDeleteView(LoginRequiredMixin,DeleteView):
    model = res_education
    success_url = reverse_lazy('myresume:resumepage')

class ProUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirected_field_name = 'myresume/my_resume.html'
    form_class = ResProForm
    model = res_project

class CreateProView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirected_field_name = 'myresume/my_resume.html'
    form_class = ResProForm
    model = res_project

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class ProDeleteView(LoginRequiredMixin,DeleteView):
    model = res_project
    success_url = reverse_lazy('myresume:resumepage')

class WorkUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirected_field_name = 'myresume/my_resume.html'
    form_class = ResWorkForm
    model = res_work

class CreateWorkView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirected_field_name = 'myresume/my_resume.html'
    form_class = ResWorkForm
    model = res_work

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class WorkDeleteView(LoginRequiredMixin,DeleteView):
    model = res_work
    success_url = reverse_lazy('myresume:resumepage')

class SkillUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirected_field_name = 'myresume/my_resume.html'
    form_class = ResSkillForm
    model = res_skill

class CreateSkillView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirected_field_name = 'myresume/my_resume.html'
    form_class = ResSkillForm
    model = res_skill

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class SkillDeleteView(LoginRequiredMixin,DeleteView):
    model = res_skill
    success_url = reverse_lazy('myresume:resumepage')

class AwardUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirected_field_name = 'myresume/my_resume.html'
    form_class = ResAwardForm
    model = res_award

class CreateAwardView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirected_field_name = 'myresume/my_resume.html'
    form_class = ResAwardForm
    model = res_award

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class AwardDeleteView(LoginRequiredMixin,DeleteView):
    model = res_award
    success_url = reverse_lazy('myresume:resumepage')
