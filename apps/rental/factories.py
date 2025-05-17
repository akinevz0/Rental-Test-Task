import factory

from datetime import date

from .models import Rental, Reservation


class RentalFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Rental

    name = factory.Sequence(lambda n: f"Rental-{n}")


class ReservationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Reservation

    rental = factory.SubFactory(RentalFactory)
    checkin = factory.Sequence(lambda n: date(2000 + n // 12, n % 12, 1))
    checkout = factory.Sequence(lambda n: date(2000 + n // 12, n % 12, 15))
