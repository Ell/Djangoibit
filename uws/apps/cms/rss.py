from django.contrib.syndication.views import Feed
from cms.models import Show
import markdown

from django.utils.feedgenerator import Rss201rev2Feed
import datetime
from datetime import time


class ItunesFeedGenerator(Rss201rev2Feed):

    def rss_attributes(self):
        return {u"version": self._version, u"xmlns:atom": u"http://www.w3.org/2005/Atom", u'xmlns:itunes': u'http://www.itunes.com/dtds/podcast-1.0.dtd'}

    def add_root_elements(self, handler):
        super(ItunesFeedGenerator, self).add_root_elements(handler)
        handler.addQuickElement(u'itunes:subtitle', self.feed['subtitle'])
        handler.addQuickElement(u'itunes:author', self.feed['author_name'])
        handler.addQuickElement(u'itunes:summary', self.feed['description'])
        handler.addQuickElement(u'itunes:category', attrs={"text": "Music"})
        handler.addQuickElement(u'itunes:explicit', self.feed['itunes_explicit'])
        handler.startElement(u"itunes:owner", {})
        handler.addQuickElement(u'itunes:name', self.feed['itunes_name'])
        handler.addQuickElement(u'itunes:email', self.feed['itunes_email'])
        handler.endElement(u"itunes:owner")
        handler.addQuickElement(u'itunes:image', attrs={"href": self.feed['itunes_image_url']})

    def add_item_elements(self,  handler, item):
        super(ItunesFeedGenerator, self).add_item_elements(handler, item)
        handler.addQuickElement(u'itunes:summary', item['summary'])
        handler.addQuickElement(u'itunes:duration', str(item['duration']))
        handler.addQuickElement(u'itunes:explicit', item['explicit'])


class ItunesPodcastPost(object):
    def __init__(self, podcast):
        self.id = podcast.id
        self.approval_date_time = podcast.date
        self.title = podcast.name
        self.summary = markdown.markdown(podcast.description)
        self.enclosure_url = podcast.songfile
        self.enclosure_length = podcast.songfile_size
        self.enclosure_mime_type = u'audio/mpeg'
        self.duration = podcast.songfile_length
        self.explicit = u'no'
        self.slug = podcast.slug
        self.description = podcast.dj + " - " + podcast.name

        def __unicode__(self):
            return "test"

        #@permalink
        #def get_absolute_url(self):
        #    return ('podcast_view', [str(self.id)])


class ITunesPodcastsFeed(Feed):
    title = "ultrawizardsword"
    link = ""
    author_name = 'relative_q'
    description = "archived sets from ultrawizardsword.net internet broadcasts. ultrawizardsword is a loose collective of djs and musicians brought together by electronic music. ultrawizardsword is both history and portent. ultrawizardsword is a thing to be reckoned with."
    subtitle = "ultrawizardsword dot net archives"
    summary = "archived sets from ultrawizardsword.net internet broadcasts. ultrawizardsword is a loose collective of djs and musicians brought together by electronic music. ultrawizardsword is both history and portent. ultrawizardsword is a thing to be reckoned with."
    itunes_name = u'relative_q'
    itunes_email = u'relative_q@youngrobots.com'
    itunes_image_url = u'http://www.youngrobots.com/media/ultrawizardsword/uws_title.png'
    itunes_explicit = u'no'
    feed_type = ItunesFeedGenerator
    feed_copyright = "Copyright %s ultrawizardsword" % datetime.date.today().year

    def items(self):
        """
        Returns a list of items to publish in this feed.
        """
        posts = Show.objects.filter()
        posts = [ItunesPodcastPost(item) for item in posts]
        return posts

    def feed_extra_kwargs(self, obj):
        extra = {}
        extra['itunes_name'] = self.itunes_name
        extra['itunes_email'] = self.itunes_email
        extra['itunes_image_url'] = self.itunes_image_url
        extra['itunes_explicit'] = self.itunes_explicit
        return extra

    def item_pubdate(self, item):
        return datetime.datetime.combine(item.approval_date_time, time())

    def item_extra_kwargs(self, item):
        return {'summary': item.summary, 'duration': item.duration, 'explicit': item.explicit}

    def item_enclosure_url(self, item):
        return item.enclosure_url

    def item_enclosure_length(self, item):
        return item.enclosure_length

    def item_enclosure_mime_type(self, item):
        return item.enclosure_mime_type

    def item_description(self, item):
        return item.summary

    def item_link(self, item):
        return "/s/%s" % item.slug

    def item_title(self, item):
        return item.description
