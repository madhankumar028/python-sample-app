from django.conf.urls import url
from demo import views

urlpatterns = [
    url(r'^getHestiaAdmin/$', views.GetHestiaAdmin.as_view()),
    url(r'^$', views.HomePageView.as_view()),
    url(r'^about/$', views.AboutPageView.as_view()),
    url(r'^table/$', views.TableView.as_view()),
]
