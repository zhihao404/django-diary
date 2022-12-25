from django import forms
from .models import Diary

class DiaryForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = ('date', 'title', 'text',)

# from django import forms
# from .models import Diary


# class DiaryForm(forms.ModelForm):
#     class Meta:
#         model = Diary
#         fields = ('date', 'title', 'text')
#         widgets = {
#             'date': forms.DateInput(attrs={'class': 'form-control'}),
#             'title': forms.TextInput(attrs={'class': 'form-control'}),
#             'text': forms.TextInput(attrs={'class': 'form-control'}),
#         }