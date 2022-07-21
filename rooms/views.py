from django.shortcuts import redirect, render
from django.core.paginator import Paginator, EmptyPage
from . import models


def all_rooms(request):
    page = request.GET.get("page", 1)
    room_list = models.Room.objects.all()
    paginator = Paginator(room_list, 10, orphans=5)
    try:
        rooms = paginator.page(int(page))
        return render(
            request,
            "rooms/home.html",
            {
                "pages": rooms,
            },
        )
    except EmptyPage:
        return redirect("/")
