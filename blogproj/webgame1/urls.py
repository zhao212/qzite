from django.conf.urls import url
from . import views
app_name = 'webgame1'
urlpatterns = [
# url(r'^$',views.IndexView.as_view(),name = 'index'),
url(r'^game1/$',views.Game1View.as_view(),name = 'game1'),

]
