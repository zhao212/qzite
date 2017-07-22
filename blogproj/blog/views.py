# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from blog.models import Post, Comment, MyProject
from blog.forms import PostForm, CommentForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView, ListView,DetailView,CreateView,UpdateView,DeleteView)
# Create your views here.

# class IndexView(TemplateView):
#     template_name = 'index.html'

class AboutView(TemplateView):
    template_name = 'blog/about.html'

class AppView(TemplateView):
    template_name = 'blog/apps_list.html'

class ProjectListView(ListView):
    model = MyProject
    def get_queryset(self):
        return MyProject.objects.filter(start_time__lte=timezone.now()).order_by('-start_time')


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class PostDetailView(DetailView):
    model = Post


class CreatePostView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirected_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirected_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post

class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = reverse_lazy('blog/post_list')

class DraftListView(LoginRequiredMixin,ListView):
    login_urls = '/login/'
    context_object_name = 'post_draft_list'
    template_name = 'blog/post_draft_list.html'
    redirected_field_name = 'blog/post_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')

# class ResumeFormView(CreateView):
#     redirected_field_name = 'apps/resume_page.html'
#     form_class = ResumeForm
#     model = Resume

@login_required
def post_publish(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('blog:post_detail',pk=pk)

@login_required
def add_comment_to_post(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('blog:post_detail',pk=post.pk)
    else:
        form = CommentForm(initial = {'author':request.user})

    return render(request,'blog/comment_form.html',{'form':form})

@login_required
def comment_approve(request,pk):
    comment = get_object_or_404(Comment,pk = pk)
    comment.approve()
    return redirect('blog:post_detail',pk=comment.post.pk)

@login_required
def comment_remove(request,pk):
    comment = get_object_or_404(Comment,pk = pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('blog:post_detail',pk=comment.post.pk)
