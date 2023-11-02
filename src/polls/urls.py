from django.conf.urls import path

from . import views


app_name = 'polls'

urlpatterns = [
    # ex: /polls/
    path(r'^$', views.index, name='index'),
    # ex: /polls/5/
    path(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    path(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    path(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
