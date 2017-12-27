from django import forms

from adverse_effects.models import User, AdverseEffect, Blog


class UserForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(UserForm, self).__init__(*args,**kwargs)
        self.fields['pass2'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Repeat Passowrd'})

    pass2 = forms.CharField(max_length=30, required=True, label="Password" )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'age', 'sex', 'height', 'weight', 'credibility', 'username', 'email', 'password', 'pass2')

        widgets = {
            'password': forms.PasswordInput(attrs={'placeholder': 'Passowrd'}),
            'pass2': forms.PasswordInput(attrs={'placeholder': 'Repeat Passowrd',}),
        }


class AdverseEffectForm(forms.ModelForm):
    class Meta:
        model = AdverseEffect
        fields = ('drug', 'name', 'bodypart')

        widgets = {
            # 'drug': forms.Select(choices=['--- select drug ---', 'Diazepam', 'EpiPen', 'Epinephrine', 'Nitroglycerin', 'Vasopressin', 'Panadol/Acetaminophen', 'Ventolin/Salbutamol', 'Aspirin', 'Zovirax/Acyclovir']),
        }



class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog

        fields = '__all__'
        exclude = ('rating',)

        widgets = {
            'content': forms.Textarea(),
        }