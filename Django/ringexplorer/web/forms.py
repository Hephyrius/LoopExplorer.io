from django.forms import ModelForm, TextInput
from .models import ring

class ringIndexForm(ModelForm):
	class Meta:
		model = ring
		fields = ['ringindex']
		widgets = {'ringindex' : TextInput(attrs={'type':'number', 'class':'input form-control', 'placeholder':'Ring Index'})}