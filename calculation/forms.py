from django import forms
from django.forms.widgets import TextInput
from simpleeval import simple_eval

from .models import Calculation


class CalculationForm(forms.ModelForm):
    class Meta:
        model = Calculation
        fields = ['expression']
        widgets = {
            'expression': TextInput(attrs={'autocomplete': 'off'}),
        }

    def is_valid(self):

        valid = super(CalculationForm, self).is_valid()

        if not valid:
            return valid

        try:
            simple_eval(self.cleaned_data['expression'])
            return True
        except:
            self._errors['invalid_exp'] = 'Invalid expression'
            return False
