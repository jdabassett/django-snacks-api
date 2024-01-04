
from django.urls import path

from .views import SnacksList, SnackDetailed


urlpatterns = [
    path("", SnacksList.as_view(), name="snacks_list"),
    path("<int:pk>", SnackDetailed.as_view(), name="snack_detailed")
]
