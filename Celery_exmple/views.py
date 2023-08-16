from django.shortcuts import render
from django.http import HttpResponse
from .task import * 
from django.core.mail import send_mail

# Create your views here.

def index(request):
    # sleep(10) after 10 second past this route response 
    sleepy.delay(10) # in the ui return fast but work on this delay in the celery server 
    return HttpResponse('<h1>Hello, </h1>')


# #send mail without celery 
# def send_mail_without_selery(request):
#     send_mail(
#         'Mail Title','Subjects',
#         'Form Email',
#         'To Email'
#     )
#     return HttpResponse("Sending Email Done...")

# #Note: we can see the mail is responding after 10 sec..To prevent this time we need desparatly using redis and celery 
# def send_mail_celery(request):
#     send_mail_celery.delay()
#     return HttpResponse("Send this email done..")


#Note: we can see that when we use celery only 5 sec in the server take time to send the mail and the page refresh and send response within a second wow its amazing 




