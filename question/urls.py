from django.conf.urls import url, patterns
from question import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^fetch$', views.get_question, name='fetch'),
)