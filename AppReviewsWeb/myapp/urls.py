from django.conf.urls import patterns, include, url
from django.contrib import admin
from myapp import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'AppReviewsWeb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    url(r'^$', views.index, name='index'),

)
