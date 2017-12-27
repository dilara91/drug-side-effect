from django.conf.urls import url
from django.urls import path

from adverse_effects import views


app_name = "core"
urlpatterns = [
    url(r'^drug-list/$', views.drug_list),
    url(r'^home/$', views.home, name='home'),
    url(r'^drug/list/$', views.drug_details, name='drug-list'),
    url(r'^register/$', views.register, name='register'),
    url(r'^adverse-effect/add/$', views.adverse_effect, name='adverse-effect-add'),
    url(r'^adverse-effect/add/(?P<did>[\d]+)/$', views.adverse_effect, name='adverse-effect-add'),

    url(r'^blog/$', views.blog, name='blog-list'),
    url(r'^blog/new/$', views.new_blog, name='blog-new'),
    url(r'^blog/(?P<id>[\d]+)/$', views.detail_blog, name='blog-detail'),

    url(r'^search/by/drug/name/$', views.search_by_drug, name='search-by-drug'),
    url(r'^search/by/adverse/effect/$', views.search_by_adverse_effect, name='search-by-adverse-effect'),


]