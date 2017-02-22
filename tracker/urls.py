from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
	url(r'^evidence/(?P<pk>\d+)/$', views.evidence_detail, name='evidence_detail'),
]