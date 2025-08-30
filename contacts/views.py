# contacts/views.py

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Prepare the email
            subject = f'New Contact Form Submission from {name}'
            email_message = f'Name: {name}\nEmail: {email}\n\nMessage:\n{message}'
            from_email = 'your-sending-email@example.com'  # The email it will be sent from
            recipient_list = ['your-receiving-email@example.com'] # The email that receives the message

            # Send the email
            send_mail(subject, email_message, from_email, recipient_list)

            # Redirect to a new URL:
            return redirect('success')
    else:
        form = ContactForm()

    return render(request, 'contacts/contact.html', {'form': form})

def success_view(request):
    return render(request, 'contacts/success.html')