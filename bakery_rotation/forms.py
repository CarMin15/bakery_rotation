from django.forms import ModelForm
from bakery_rotation.models import BakingSlot


class BakingSlotForm(ModelForm):
    class Meta:
        model = BakingSlot
        fields = '__all__'
