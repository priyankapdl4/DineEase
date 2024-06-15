from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings

def contact_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        
        # Construct the full message including the phone number
        full_message = f"Message from {name} ({email}, {phone}):\n\n{message}"
        
        # Sending email to manager
        send_mail(
            f'Contact Form Submission from {name}',
            full_message,
            email,
            [settings.MANAGER_EMAIL],  # Replace with the manager's email
            fail_silently=False,
        )
        return redirect('contact_success')  # Redirect to a success page

    return render(request, 'contact/contact.html')

def contact_success_view(request):
    return render(request, 'contact/contact_success.html')
