from django.core.mail import EmailMessage, BadHeaderError
from django.shortcuts import render


def say_hello(request):
    try:
        # send_mail('subject', 'message', 'thomas.vu@hotmail.com', ['bob@ttcvu.com'])
        # mail_admins('subject', 'message', html_message='message')
        message = EmailMessage('subject', 'message', 'from@ttcvu.com', ['to@ttcvu.com'])
        message.attach_file('playground/static/images/dog.jpg')
        message.send()
    except BadHeaderError:
        print("hei")
    return render(request, 'hello.html', {'name': 'Mosh'})
