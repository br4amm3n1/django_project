from django.contrib import admin
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('registration/', include('REGpage.urls')),
    path('admin/', admin.site.urls),
    path('', include('newwebpage.urls')),
    path('news/', include('news.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
