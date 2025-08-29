from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_booking_confirmation(email, booking_id):
    subject = "Booking Confirmation"
    message = f"Thank you for your booking! Your booking ID is {booking_id}."
    from_email = "noreply@alxtravel.com"
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list)
    return f"Confirmation email sent to {email} for booking {booking_id}"
