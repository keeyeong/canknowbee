from django.shortcuts import render
from django.views.generic import TemplateView

from twitterscraper import query

import logging


class MainView(TemplateView):

    template_name = "main/index.html"
    logger = logging.getLogger(__name__)


    def get(self, request):
        context = {
            'results': []
        }
        return render(request, 'main/index.html', context)

    def post(self, request):
        tweets = query.query_single_page(request.POST['content'])[0]
        context = {
            'results': tweets
        }
        return render(request, 'main/index.html', context)
