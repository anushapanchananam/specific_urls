from django.urls import path
from app2.views import*
app_name = 'nothing'

urlpatterns = [
    path('first/', first, name = 'first'),
    path('second/', second, name='second'),
    path('third/', third, name='third'),
    path('four/', four, name='four'),
]