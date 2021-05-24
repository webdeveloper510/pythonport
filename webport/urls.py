from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from webportApp import views
from django.contrib import admin
from django.conf.urls import include, url
urlpatterns = [
    path('',include('webportApp.urls')),
    path('admin/', admin.site.urls),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)