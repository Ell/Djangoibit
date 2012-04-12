from django.conf import settings
from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

from cms.views import homepage, PageView, ShowView
from cms.rss import ITunesPodcastsFeed

handler500 = "pinax.views.server_error"


urlpatterns = patterns("",
    url(r"^$", homepage, name="home"),
    url(r"^admin/", include(admin.site.urls)),

    url(r"^p/(?P<slug>[a-zA-Z0-9_.-]+)/$", PageView.as_view(), name="page"),
    url(r"^s/(?P<slug>[a-zA-Z0-9_.-]+)/$", ShowView.as_view(), name="show"),

    (r'^latest/feed/$', ITunesPodcastsFeed()),
)


if settings.SERVE_MEDIA:
    urlpatterns += patterns("",
        url(r"", include("staticfiles.urls")),
    )
