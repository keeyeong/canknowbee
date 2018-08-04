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
        result = calculate(request.POST['source'], request.POST['target'])
        context = {
            'source': request.POST['source'],
            'target': request.POST['target'],
            'result': result[0],
            'matrix': result[1]
        }
        return render(request, 'main/index.html', context)
