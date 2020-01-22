from django.urls import path
from django.conf import settings
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('<int:pk>/', DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', results, name='results'),
    path('<int:question_id>/vote/', vote, name='vote')
]
