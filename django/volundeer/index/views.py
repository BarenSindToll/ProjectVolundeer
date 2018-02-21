from django.shortcuts import render_to_response
from django.template import RequestContext


def home(request):
    if request.user.is_authenticated():
        template = 'homepage.html'
    else:
        template = 'index.html'
    return render_to_response(template)
