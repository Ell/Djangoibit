from django.views.generic import TemplateView, DetailView

from cms.models import Page, Show


class Homepage(TemplateView):
    template_name = "homepage.html"


class Page(DetailView):
    context_object_name = 'page'
    template_name = "page.html"
    model = Page

    def get_context_data(self, **kwargs):
        context = super(Page, self).get_context_data(**kwargs)
        return context


class Show(DetailView):
    context_object_name = 'show'
    model = Show
    template_name = "show.html"

    def get_context_data(self, **kwargs):
        context = super(Show, self).get_context_data(**kwargs)
        return context
