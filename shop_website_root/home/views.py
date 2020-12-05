from django.shortcuts import render
from .forms import Submit_Problem_Form
from django.contrib import messages

#EMAIL
from django.core.mail import send_mail
from django.conf import settings 
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .models import Submit_Problem
#SMS
import requests
import json


def homepage(request):
	if request.method=='POST':
		form = Submit_Problem_Form(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			cd = form.cleaned_data

			username=cd.get('name')		
			subject= f"{username}::{cd['title_of_problem']}"
			html_message = render_to_string('email_template.html', {'cd': cd})
			plain_message = strip_tags(html_message)
			from_email = settings.EMAIL_HOST_USER
			to = [cd.get('email'),'sanjaygawade29285@gmail.com','sanjay_gawde@hotmail.com']

			t=send_mail(subject, plain_message, from_email,to,html_message=html_message)

			messages.success(request, f"<b>{username} </b> Problem Has Been Submitted Check Your Email We have sent You Your Problem's Copy We Wil Reach You Soon ")
	else:
		form = Submit_Problem_Form()

	return render(request,'home/index.html',{'form':form})




