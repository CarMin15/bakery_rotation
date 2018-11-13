from django.forms import ModelForm
from django import forms
from bakery_rotation.models import BakingSlot


class BakingSlotForm(ModelForm):

    image = forms.ImageField(required=False)

    class Meta:
        model = BakingSlot
        fields = '__all__'
