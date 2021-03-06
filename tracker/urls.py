from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.home_page, name = 'home_page'),
    url(r'^posts', views.post_list, name='post_list'),
	url(r'^evidence/(?P<pk>\d+)/$', views.evidence_detail, name='evidence_detail'),
	url(r'^evidence/new/$', views.evidence_new, name='evidence_new'),
	url(r'^post/(?P<pk>\d+)/edit/$', views.evidence_edit, name='evidence_edit'),
	url(r'^accounts/logout/$',views.log_out, name='log_out'),
]