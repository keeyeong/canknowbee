from django.shortcuts import render
from django.views.generic import TemplateView


class MainView(TemplateView):
    template_name = "main/index.html"

    def get(self, request):
        context = {
            'results': []
        }
        return render(request, 'main/index.html', context)

    def post(self, request):
        context = {
            'results': [request.POST['content']]
        }
        return render(request, 'main/index.html', context)
