from cms.models import Show, Grouping
import requests


def side_menu(request):
    shows = Show.objects.order_by('-date').all()
    groupings = Grouping.objects.order_by('position').all()

    r = requests.get('http://ultrawizardsword.net:8000/status.xsl')
    if r.text == "dj":
        live = True
    else:
        live = False

    return {'shows': shows, 'groupings': groupings, 'live': live}
