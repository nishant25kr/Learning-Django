
from django.urls import path
from . import views

# localhost:8000/cahi
# localhost:8000/cahi/order
urlpatterns = [
    path('home/', views.all_chai, name="all_chai"),
    # path('order/', views.order, name="order"),


]
