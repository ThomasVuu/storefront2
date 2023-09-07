from django.core.mail import send_mail, mail_admins, BadHeaderError
from django.shortcuts import render


def say_hello(request):
    try:
        # send_mail('subject', 'message', 'thomas.vu@hotmail.com', ['bob@ttcvu.com'])
        mail_admins('subject', 'message', html_message='message')
    except BadHeaderError:
        print("hei")
    return render(request, 'hello.html', {'name': 'Mosh'})
