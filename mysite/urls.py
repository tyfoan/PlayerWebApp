from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from music.views import IndexView



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view()),
    url(r'^music/', include('music.urls')),
    url(r'^video/', include('video.urls')),

]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [url(r'^__debug__/', debug_toolbar.urls)]
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

