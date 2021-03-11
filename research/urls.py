from django.urls import path
from . import views

urlpatterns = [
    path("", views.research_index, name="research_index"),
    path("<int:pk>/", views.research_detail, name="research_detail"),
]

