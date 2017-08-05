from django.conf.urls import url
from . import views
app_name = 'mymsg'
urlpatterns = [
    url(r"^inbox/$", views.msginbox.as_view(), name="msginbox"),
    url(r"^compose/$", views.msgcompose.as_view(), name="msgcompose"),
    url(r"^msg/(?P<pk>\d+)$",views.MsgDetailView.as_view(),name='msgdetail'),
]
