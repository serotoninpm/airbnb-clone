from django.views.generic import ListView, DetailView
from . import models


class HomeView(ListView):
    """HomeView Definition"""

    model = models.Room
    paginate_by: int = 10
    paginate_orphans: int = 5
    ordering = "created"
    context_object_name = "rooms"


class RoomDetail(DetailView):
    """RoomDetail Definition"""

    model = models.Room
