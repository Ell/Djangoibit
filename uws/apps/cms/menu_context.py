from cms.models import Show, Grouping


def side_menu(request):
    shows = Show.objects.order_by('-date').all()
    groupings = Grouping.objects.order_by('position').all()

    return {'shows': shows, 'groupings': groupings}
