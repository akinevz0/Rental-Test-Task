from django.test import TestCase, Client
from django.urls import reverse

from datetime import date

from .factories import RentalFactory, ReservationFactory


class TestRental(TestCase):
    def setUp(self):
        self.client = Client()

        self.rentals = [RentalFactory() for _ in range(3)]
        self.reservations = [
            ReservationFactory(
                rental=self.rentals[0],
                # Ensuring no overlap
                checkin=date(2000, i, 1),
                checkout=date(2000, i, 15),
            )
            for i in range(1, 4)
        ]

    def test_previous_reservation(self):
        assert self.reservations[0].previous_reservation is None
        assert all(
            # Already doing i - 1, since enumerate goes from the second element.
            reservation.previous_reservation == self.reservations[i]
            for i, reservation in enumerate(self.reservations[1:])
        )

    def test_reservations_view(self):
        response = self.client.get(reverse("rental:reservations"))

        assert response.status_code == 200
        assert len(response.context["reservations"]) == 3
