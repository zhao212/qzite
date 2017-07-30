from django.conf.urls import url
from . import views
app_name = 'myresume'
urlpatterns = [
# url(r'^$',views.IndexView.as_view(),name = 'index'),
url(r'^my_resume/$',views.ResumeListView.as_view(),name = 'resumepage'),
url(r'^web_resume/$',views.WebResumeListView.as_view(),name = 'webresumepage'),
url(r'^my_resume/(?P<pk>\d+)/basic_edit/$',views.BasicInfoUpdateView.as_view(),name = 'basic_edit'),
url(r'^my_resume/basic_new/$',views.CreateBasicInfoView.as_view(),name='basic_new'),
url(r'^my_resume/(?P<pk>\d+)/edu_edit/$',views.EduUpdateView.as_view(),name = 'edu_edit'),
url(r'^my_resume/edu_new/$',views.CreateEduView.as_view(),name='edu_new'),
url(r'^my_resume/(?P<pk>\d+)/pro_edit/$',views.ProUpdateView.as_view(),name = 'pro_edit'),
url(r'^my_resume/pro_new/$',views.CreateProView.as_view(),name='pro_new'),
url(r'^my_resume/(?P<pk>\d+)/work_edit/$',views.WorkUpdateView.as_view(),name = 'work_edit'),
url(r'^my_resume/work_new/$',views.CreateWorkView.as_view(),name='work_new'),
url(r'^my_resume/(?P<pk>\d+)/skill_edit/$',views.SkillUpdateView.as_view(),name = 'skill_edit'),
url(r'^my_resume/skill_new/$',views.CreateSkillView.as_view(),name='skill_new'),
url(r'^my_resume/(?P<pk>\d+)/award_edit/$',views.AwardUpdateView.as_view(),name = 'award_edit'),
url(r'^my_resume/award_new/$',views.CreateAwardView.as_view(),name='award_new'),
url(r'^my_resume/(?P<pk>\d+)/basic_remove/$',views.BasicDeleteView.as_view(),name = 'basic_remove'),
url(r'^my_resume/(?P<pk>\d+)/edu_remove/$',views.EduDeleteView.as_view(),name = 'edu_remove'),
url(r'^my_resume/(?P<pk>\d+)/pro_remove/$',views.ProDeleteView.as_view(),name = 'pro_remove'),
url(r'^my_resume/(?P<pk>\d+)/work_remove/$',views.WorkDeleteView.as_view(),name = 'work_remove'),
url(r'^my_resume/(?P<pk>\d+)/skill_remove/$',views.SkillDeleteView.as_view(),name = 'skill_remove'),
url(r'^my_resume/(?P<pk>\d+)/award_remove/$',views.AwardDeleteView.as_view(),name = 'award_remove'),

]
