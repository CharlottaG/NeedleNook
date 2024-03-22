from . import views
from django.urls import path

urlpatterns = [
    path('home/', views.PatternList.as_view(), name='home'),
]