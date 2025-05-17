from django.db import models


class Rental(models.Model):
    name = models.CharField(max_length=255, help_text="Name of the rental")

    def __str__(self):
        return self.name


class Reservation(models.Model):
    # Choosing set null, as these are transactions records
    rental = models.ForeignKey(
        Rental, null=True, related_name="reservations", on_delete=models.SET_NULL
    )

    checkin = models.DateField(help_text="Date of check in")
    # Checking out may be in the future, so may not be certain which is why it's None
    checkout = models.DateField(help_text="Date of check out", blank=True, null=True)

    @property
    def previous_reservation(self):
        previous_reservations = Reservation.objects.filter(
            rental=self.rental, checkin__lt=self.checkin
        )
        if not previous_reservations.exists():
            return None
        return previous_reservations.order_by("-checkin").first()
