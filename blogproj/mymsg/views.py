from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from mymsg.models import *
from mymsg.forms import *
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView, ListView,DetailView,CreateView,DeleteView)
# Create your views here.
class msginbox(ListView,LoginRequiredMixin):
    login_url = '/login/'
    template_name = "mymsg/msgbox.html"
    model = msg

    def get_queryset(self):
        return msg.objects.filter(receiver=self.request.user).order_by('-sent_time')

class msgcompose(CreateView,LoginRequiredMixin):
    login_url = '/login/'
    template_name = "mymsg/msgcompose.html"
    redirected_field_name = 'mymsg/msgbox.html'
    form_class = msgForm
    model = msg

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.sender = self.request.user
        self.object.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


class MsgDetailView(DetailView,LoginRequiredMixin):
    template_name = "mymsg/msgdetail.html"
    model = msg

# @login_required
# def reply_to_msg(request,receiver):
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.post = post
#             comment.save()
#             return redirect('blog:post_detail',pk=post.pk)
#     else:
#         form = CommentForm(initial = {'author':request.user})
#
#     return render(request,'blog/comment_form.html',{'form':form})
