from django.forms import ModelForm
from .models import Booking


# Code added for loading form data on the Booking page
class BookingForm(ModelForm):
    """
    A form for creating or updating a booking.

    This form is used to collect and validate user input for creating or updating a booking.
    It is based on the `Booking` model and includes all fields defined in the model.

    Usage:
    form = BookingForm(request.POST or None)
    if form.is_valid():
        booking = form.save()

    Attributes:
    - model: The model class that the form is based on (Booking).
    - fields: The fields to include in the form (all fields in the Booking model).
    """
    class Meta:
        model = Booking
        fields = "__all__"
