from django.contrib.syndication.views import Feed

from cms.models import Show


class LatestShowsFeed(Feed):
    title = "UltraWizardSword Shows"
    link = '/'
    description = "Latest shows from ultrawizardsword.net"

    def items(self):
        return Show.objects.order_by('-date')[:20]

    def item_title(self, item):
        return "%s - %s" % (item.date, item.dj)

    def item_description(self, item):
        return "%s - %s" % (item.dj, item.name)
