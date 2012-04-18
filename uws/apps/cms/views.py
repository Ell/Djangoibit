from django.views.generic import DetailView
from django.shortcuts import render

from cms.models import Page, Show


def homepage(request):
    page = Page.objects.get(frontpage=True)
    return render(request, "homepage.html", {"page": page})


class PageView(DetailView):
    context_object_name = 'page'
    template_name = "page.html"
    model = Page

    def get_context_data(self, **kwargs):
        context = super(PageView, self).get_context_data(**kwargs)
        return context


class ShowView(DetailView):
    context_object_name = 'show'
    model = Show
    template_name = "show.html"

    def get_context_data(self, **kwargs):
        context = super(ShowView, self).get_context_data(**kwargs)
        return context
