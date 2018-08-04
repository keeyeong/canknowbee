from django.shortcuts import render
from django.views.generic import TemplateView

from twitterscraper import query

import logging


class MainView(TemplateView):

    template_name = "main/index.html"
    logger = logging.getLogger(__name__)


    def get(self, request):
        context = {
            'result': None
        }
        return render(request, 'main/index.html', context)

    def post(self, request):

        context = {
            'result': tweets
        }
        return render(request, 'main/index.html', context)
