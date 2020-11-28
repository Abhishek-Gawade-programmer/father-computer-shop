from django.forms import ModelForm
from .models import Submit_Problem

class Submit_Problem_Form(ModelForm):
	class Meta:
		model = Submit_Problem
		fields = [
				'name',
				'phone',
				'email',
				'title_of_problem',
				'description_of_problem',
				'repair_photos',
		]


