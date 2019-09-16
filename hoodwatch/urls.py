from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include,url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search$', views.search, name='search'),
    url(r'^business$', views.business, name='business'),
    url(r'^profile/(?P<username>\w{0,50})$', views.profile, name='profile'),
    url(r'^edit_profile/(?P<username>\w{0,50})$', views.edit_profile, name='edit_profile'),
    url(r'^post/(\d+)$', views.post, name='post'),
    url(r'^new_business$', views.new_business, name='newbusiness'),
    url(r'^post$', views.post, name='post'),
   
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

    
