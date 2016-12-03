from django.conf.urls import include, url
from django.contrib import admin
from music.views import IndexView
from .settings import DEBUG


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view()),
    url(r'^music/', include('music.urls')),
    url(r'^video/', include('video.urls')),

]

if DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', debug_toolbar.urls)
    ]

