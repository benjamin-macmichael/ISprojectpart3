from django.urls import path
from .views import indexPageView
from .views import dataPageView
from .views import infoPageView
            
urlpatterns = [
    path("data/", dataPageView, name="data"),
    path("info/<int:person_id>", infoPageView, name="info"),
    path("", indexPageView, name="index"),    
]  