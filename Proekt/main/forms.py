from django.forms import ModelForm
from user_account.models import *
from django.forms import ModelForm, NumberInput, FileInput

class CheckForm(ModelForm):
    class Meta:
        model = CheckPayment
        fields = ["amount"]
        widgets = {
            "amount": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Сумма пополнения',
                'min': '1',
            }),
        }