from django.conf import settings
from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

from cms.views import Homepage, Page, Show
from cms.rss import LatestShowsFeed

handler500 = "pinax.views.server_error"


urlpatterns = patterns("",
    url(r"^$", Homepage.as_view(), name="home"),
    url(r"^admin/", include(admin.site.urls)),

    url(r"^p/(?P<slug>[a-zA-Z0-9_.-]+)/$", Page.as_view(), name="page"),
    url(r"^s/(?P<slug>[a-zA-Z0-9_.-]+)/$", Show.as_view(), name="show"),

    (r'^latest/feed/$', LatestShowsFeed()),
)


if settings.SERVE_MEDIA:
    urlpatterns += patterns("",
        url(r"", include("staticfiles.urls")),
    )
