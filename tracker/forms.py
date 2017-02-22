from django import forms
from .models import Evidence

class EvidenceForm(forms.ModelForm):
	
	class Meta:
		model = Evidence
		fields = ('title', 'text',)