import models


def best_users(request):
    context_extras = {
        'best_users': models.User.objects.select_related().order_by('-rating')[:10],
    }
    return context_extras


def popular_tags(request):
    context_extras = {
        'popular_tags': [{'text': tag.text } for tag in models.Tag.objects.all()[:10]],
    }
    return context_extras
