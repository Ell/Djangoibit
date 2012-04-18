from django.db import models
from django.template.defaultfilters import slugify


class Show(models.Model):
    dj = models.CharField("DJ Name", max_length=420)
    name = models.CharField("Show Name", max_length=50)
    songfile = models.URLField("Shows MP3 Link")
    image = models.ImageField("Shows Image", upload_to='shows/', blank=True)
    imageurl models.URLField("Show Image URL (One or the other not both)", blank=True)
    description = models.TextField("Description (markdown)")
    date = models.DateField()
    slug = models.SlugField(editable=False)
    year = models.PositiveIntegerField(editable=False, blank=True)
    songfile_size = models.PositiveIntegerField("Size in MB of songfile")
    songfile_length = models.PositiveIntegerField("Length in seconds of set")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.year = self.date.year
        super(Show, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return "/s/%s/" % self.slug


class Grouping(models.Model):
    title = models.CharField("Grouping Title", max_length=50)
    position = models.IntegerField("Groupings Position")

    def __unicode__(self):
        return self.title


class Page(models.Model):
    grouping = models.ForeignKey("Grouping")
    title = models.CharField("Page Title", max_length=50)
    content = models.TextField("Page Content (markdown)")
    slug = models.SlugField(editable=False)
    frontpage = models.BooleanField(default=False, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Page, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title
