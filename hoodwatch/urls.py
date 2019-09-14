from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include,url
from . import views

urlpatterns=[


    url(r'^profile/',views.profile,name='profile'),
    url('^$',views.index,name ='index'),


    url(r'^tinymce/', include('tinymce.urls')),
    
    

    

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

    
