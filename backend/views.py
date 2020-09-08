from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

# Serve Single Page Application
#index = never_cache(TemplateView.as_view(template_name='index.html'))

def acme_challenge(request):
    return HttpResponse(settings.ACME_CHALLENGE_CONTENT)