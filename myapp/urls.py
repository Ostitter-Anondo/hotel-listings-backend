from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("hotels/", views.hotels, name="hotels"),
    path("filteredhotels/", views.filteredhotels, name="filteredhotels"),
    path("stuff/", views.stuff, name="stuff")
]
