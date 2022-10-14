from django.urls import path
from .views import HomePageView
# from . import views


app_name = 'posts'

urlpatterns = [
    path("", HomePageView.as_view(), name='home'),
]


# urlpatterns = [
#     path("", views.home, name='home')
# ]
