from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="inventory"),
    path("<int:engin_id>", views.engins, name="engins")
]