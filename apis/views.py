from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from snacks.models import Snack
from .serializer import SnackSerializer


class SnacksList(ListCreateAPIView):
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer


class SnackDetailed(RetrieveUpdateDestroyAPIView):
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer
