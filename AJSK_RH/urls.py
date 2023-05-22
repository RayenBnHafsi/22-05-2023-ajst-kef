from django.urls import path
from . import views


urlpatterns = [
    path('', views.index , name='ajst.home'),
    path('post/', views.psot, name="ajst.post"),
    path('activities/', views.active, name="ajst.activities"),
]