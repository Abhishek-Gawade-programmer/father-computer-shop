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
from twilio.rest import Client
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
			to = [cd.get('email'),]

			t=send_mail(subject, plain_message, from_email,to,html_message=html_message)

			url="https://www.fast2sms.com/dev/bulk"
			querystring = {"authorization":'FaqMoX0CGc1KSpBJztVITZbfrAj5WsyPeLEl2u6Y9NdHDxmn3wOnqrulKsoXFAWCp0gdP37SR4cTBNYe',
					"sender_id":"FSTSMS",
					"message":'yusefgysbdvyubnvcyun hj SMS',
					"language":"english",
					"route":"t",
					"numbers":'9860390980'}


			headers = {
			    'cache-control': "no-cache"
			}

			response = requests.get(url,params=querystring)
			dic=response.json()
			print(dic)
			
			# account_sid=str(settings.TWIILIO_ACCOUNT_SID)
			# auth_token=str(settings.TWIILIO_AUTH_TOKEN)
			# client=Client(account_sid,auth_token)

			# if len(str(cd.get('phone')))==10:
			# 	cd['phone']='+91'+str(cd['phone'])

			# message=client.messages.create(
			# 	body=f'''{username} Your Problem Has Been Recorded Your id {Submit_Problem.objects.last().id} 
			# 		TITLE : {cd['title_of_problem']} 
			# 		DESCRPTION :{cd['description_of_problem']}''',
			# 	from_=str(settings.TWIILIO_NUMBER),
			# 	to=cd['phone'])
			



			messages.success(request, f"Your Problem Has Been Submitted: <b>{username} </b>")
	else:
		form = Submit_Problem_Form()

	return render(request,'home/index.html',{'form':form})




