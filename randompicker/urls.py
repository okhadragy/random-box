from django.contrib import admin
from .settings import *
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.views.i18n import JavaScriptCatalog


urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('',include(('root.urls','root'),namespace="root")),
    path('jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog'),
    path('i18n/', include('django.conf.urls.i18n')),
)
urlpatterns += static(MEDIA_URL,document_root=MEDIA_ROOT)
urlpatterns += static(STATIC_URL,document_root=STATIC_ROOT)