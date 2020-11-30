from django.shortcuts import render
from .forms import Submit_Problem_Form
from django.contrib import messages

#EMAIL
from django.core.mail import send_mail,get_connection
from django.conf import settings 
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def homepage(request):
	if request.method=='POST':
		form = Submit_Problem_Form(request.POST,request.FILES)
		if form.is_valid():
			cd = form.cleaned_data
			username=cd.get('name')		
			con =get_connection(settings.EMAIL_BACKEND)
			send_mail(
				cd['name'],
				cd['title_of_problem']+cd.get('email'),
				settings.EMAIL_HOST_PASSWORD,
				[cd.get('email'),]
			)

			
			messages.success(request, f"Your Problem Has Been Submitted: <b>{username} </b>")
	else:
		form = Submit_Problem_Form()

	return render(request,'home/index.html',{'form':form})
