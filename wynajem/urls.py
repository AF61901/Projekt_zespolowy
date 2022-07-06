from django.urls import path
from .views import (
    PostListView
)
from . import views

urlpatterns = [
    path('', views.home, name='wynajem-home'),
    path('onas/', views.onas, name='wynajem-onas'),
    path('kontakt/', views.kontakt, name='wynajem-kontakt'),
    path('oferta/', views.auta, name='wynajem-oferta'),
    path('<int:id>/szczegoly/', views.szczeg, name='wynajem-szczegoly'),
    path('<int:id>/zamow/', views.zam, name='wynajem-zamow'),
    path('moje/', PostListView.as_view(), name='wynajem-moje'),
    path('<int:id>/delete', views.delete, name = "delete"),
    path('<int:id>/detail', views.detail, name = "detail"),
]

