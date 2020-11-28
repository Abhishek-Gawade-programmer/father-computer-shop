from django.shortcuts import render
from .forms import Submit_Problem_Form
def homepage(request):
	if request.method=='POST':
		form = Submit_Problem_Form(request.POST,request.FILES)
		if form.is_valid():
			cd = form.save()
	else:
		form = Submit_Problem_Form()

	return render(request,'home/index.html',{'form':form})
