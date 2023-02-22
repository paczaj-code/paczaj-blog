from django.urls import path
from .views import PractiseListAPIView, PractiseListByCategorySlugAPIView, PracticeDeatilsAPIView


urlpatterns = [
    path('practice/', PractiseListAPIView.as_view(), name='practise-list'),
    path('practice/<str:slug>', PractiseListByCategorySlugAPIView.as_view(),
         name='practice-by-slug'),
    path('exercice/<str:slug>', PracticeDeatilsAPIView.as_view(),
         name='exercice-by-slug'),
]

app_name = 'practice'
