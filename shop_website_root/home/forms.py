from django.forms import ModelForm,TextInput,NumberInput,EmailInput,Textarea
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
			
			# <textarea name="description_of_problem" cols="40" rows="10" class="vLargeTextField" id="id_description_of_problem">sdgsdgsg</textarea>	
		# widgets = {
  #           	'name':TextInput(attrs={'id':'lname', 'name':'lname','required':'',
  #           							'class':'form-control-input'},
  #           							),
  #           	'phone':NumberInput(attrs={'id':'lphone', 'name':'lphone','required':'',
  #           							'class':'form-control-input'},
  #           		),
  #           	'email':EmailInput(attrs={'id':'lemail','class':'form-control-input',
  #           							'name':'lemail','required':''}),

  #           	'title_of_problem':TextInput(attrs={'id':'title_of_problem', 'name':'Title Of Problem','required':'',
  #           							'class':'form-control-input'}),

  #           	'description_of_problem':Textarea(attrs={'id':'description_of_problem', 'name':'Description Of Problem',
  #           							'class':'form-control-input','placeholder':'Description Optional'}),
            		
  #           	# 'shipping_date': forms.TextInput(attrs={'id':'bar', 'name':'bar'})
  #   		}

