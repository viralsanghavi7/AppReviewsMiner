__author__ = 'Chetan'

from django.conf.urls import patterns, url

from ReviewMiner import views

urlpatterns = patterns('',
                       url(r'^$', views.appReview, name='appReview'),

                       url(r'^appreview$', views.appReview, name='appReview'),
                       url(r'^UploadDone$', views.appReviewUploadDone, name='uploadComplete'),
                       )
