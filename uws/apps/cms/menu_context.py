from cms.models import Show, Grouping
import requests


def side_menu(request):
    shows = Show.objects.order_by('-date').all()
    groupings = Grouping.objects.order_by('position').all()

    r = requests.get('http://ultrawizardsword.net:8000/status.xsl')
    if r.text == '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">\n\ndj\n\n':
        live = True
    else:
        live = False

    return {'shows': shows, 'groupings': groupings, 'live': live}
