from django.http import HttpResponse


def index(request):
    """
    index view
    """
    return HttpResponse("Hello World. You are at the polls index.")
