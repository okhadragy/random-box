from django.contrib import admin
from .settings import *
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(('root.urls','root'),namespace="root")),
]
urlpatterns += static(MEDIA_URL,document_root=MEDIA_ROOT)
urlpatterns += static(STATIC_URL,document_root=STATIC_ROOT)