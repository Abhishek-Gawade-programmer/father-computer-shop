from django.db import models
'''
NAME OF CUSTOMER

PHONE NUMBER OF COSTUMER

EMAIL OF CUSTOMER(OPTIONAL)

TITTLE OF PROBLE

DECRPTION OD Problem

SEND PHOTES OF YOUR PROBLEM 

'''
class Submit_Problem(models.Model):
	name=models.CharField(max_length=50)
	phone=models.PositiveIntegerField()
	email=models.EmailField(blank=True)
	title_of_problem=models.CharField(max_length=100)
	description_of_problem=models.TextField(blank=True)
	repair_photos= models.FileField(verbose_name='Sent Photos Of Your Problem',upload_to='uploads/',blank=True)

	def __str__(self):
		return self.name


