from django.conf.urls import patterns, url
from chem import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #url(r'^about/$', views.about, name='about'),
    url(r'^add_category/$', views.add_category, name='add_category'), # NEW MAPPING!
    url(r'^category/(?P<category_name_url>\w+)/$', views.category, name='category'),  # New!
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^restricted/', views.restricted, name='restricted'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^increment/$', views.increment, name='increment'),
    url(r'^questions/$', views.questions, name='questions'),
    url(r'^questions/(?P<question_id_url>\w+)/$', views.question, name='question'),  # New!
]
