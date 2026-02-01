import os
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
admin_url = os.getenv('ADMIN_URL')

urlpatterns = [
                  path('', include('pages.urls')),
                  path('listings/', include('listings.urls')),
                  path('contacts/', include('contacts.urls')),
                  path('accounts/', include('accounts.urls')),
                  path('hosts/', include('hosts.urls')),
                  path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
                  path(admin_url, admin.site.urls),
                  path("__reload__/", include("django_browser_reload.urls")),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      path("__debug__/", include(debug_toolbar.urls)),
                  ] + urlpatterns
