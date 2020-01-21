from django.urls import path
from django.conf import settings
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('<int:question_id>/', detail, name='detail'),
    path('<int:question_id>/results/', results, name='results'),
    path('<int:question_id>/vote/', vote, name='vote')
]
