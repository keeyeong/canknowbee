import logging

from django.shortcuts import render
from django.views.generic import TemplateView

from .service import calculate


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
            'source': request.POST['source'],
            'target': request.POST['target'],
            'result': calculate(request.POST['source'], request.POST['target'])
        }
        return render(request, 'main/index.html', context)
