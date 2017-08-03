from django.conf.urls import url
from . import views
app_name = 'qrgenerator'
urlpatterns = [
# url(r'^$',views.IndexView.as_view(),name = 'index'),
url(r'^$',views.QRView.as_view(),name = 'generator'),

]
