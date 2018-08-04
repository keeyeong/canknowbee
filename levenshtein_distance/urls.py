from django.urls import path
from .views import MainView

urlpatterns = [
    # path('', views.index, name='index'),
    path('', MainView.as_view(), name='index')
    # path('submission', views.submission, name='submission'),
]
