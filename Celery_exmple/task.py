from celery import shared_task 
from time import sleep
from django.core.mail import send_mail


#simple sleepy function to test a functions 
@shared_task
def sleepy(duration):
    sleep(duration)
    return None


#send mail handling 
# @shared_task
# def send_mail_task():
#     send_mail('CELERY_DONE','CELERY_WORKS_FINE',
#               'freelancerudoy752@gmail.com',
#               ['udoy0304@gmail.com']
#               )
#     return None 





#upload Image handling 


#upload file handling 


