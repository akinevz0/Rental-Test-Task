from datetime import datetime
from django.core.paginator import Paginator
from django.shortcuts import render

from .models import Reservation


def reservations(request):
    reservations = Reservation.objects.all().order_by("id")

    Reservation.objects.filter(checkin__gt=datetime(year=2000))

    reservations_pages = Paginator(reservations, 20)

    try:
        current_page = int(request.GET.get("page", 1))
    except ValueError:
        current_page = 1
    else:
        current_page = max(
            1, min(reservations_pages.page_range.stop - 1, current_page))

    reservations_page = reservations_pages.page(current_page)

    return render(
        request,
        "rental/reservations.html",
        {
            "reservations": reservations_page,
            "page": {
                "previous": reservations_page.previous_page_number()
                if current_page > 1
                else None,
                "next": reservations_page.next_page_number()
                if current_page < reservations_pages.page_range.stop - 1
                else None,
                "current": current_page,
                "total": reservations_pages.num_pages,
            },
        },
    )
