from django.contrib import admin

from .models import Rental, Reservation


class RentalAdmin(admin.ModelAdmin):
    list_display = ("name",)


class ReservationAdmin(admin.ModelAdmin):
    list_display = ("rental_name", "previous_reservation", "checkin", "checkout")

    def previous_reservation(self, obj):
        return obj.previous_reservation

    def rental_name(self, obj):
        return obj.rental.name


admin.site.register(Rental, RentalAdmin)
admin.site.register(Reservation, ReservationAdmin)
