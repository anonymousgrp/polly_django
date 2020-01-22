from django.urls.conf import path
from .views import *

urlpatterns = [
    path('', auth, name='auth'),
    path('login', login, name='login'),
    path('signup', signup, name='signup'),
    path('logout', logout, name='logout')
]
