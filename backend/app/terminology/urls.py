from django.urls import path
from .views import TermListAPIView, TermDetailAPIViewByPK, TermDetailAPIViewBySlug


urlpatterns = [
    path('term/', TermListAPIView.as_view(), name='term-list'),
    path('term/<int:pk>/', TermDetailAPIViewByPK.as_view(), name='term-detail-id'),
    path('term/<str:slug>/', TermDetailAPIViewBySlug.as_view(),
         name='term-detail-slug'),

]
app_name = 'terminology'
