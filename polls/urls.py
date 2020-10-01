from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.IndexViewSet.as_view(), name='index'),
    path('<int:pk>/', views.DetailViewSet.as_view(), name="detail"),
    path('<int:pk>/results/',
         views.ResultsViewSet.as_view(), name="results"),
    path('vote/<int:pk>/<int:choice>/', views.vote, name="vote")
]
