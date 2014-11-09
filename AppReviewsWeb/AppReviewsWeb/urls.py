from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings



from django.contrib import admin
admin.autodiscover()



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'AppReviewsWeb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$',include('myapp.urls') , name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^myapp/', include('myapp.urls')),
)
