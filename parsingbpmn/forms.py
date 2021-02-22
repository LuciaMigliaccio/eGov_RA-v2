from django import forms

from .models import Process, System, Context, Fusioncontext_has_context, Profile


class SystemForm(forms.ModelForm):
    class Meta:
        model = System
        fields = ['name']

class ProcessForm(forms.ModelForm):
    class Meta:
        model = Process
        exclude = ["system_id"]
        fields = ['name','xml']

class ContextualizationForm(forms.ModelForm):
    class Meta:
        model = Context
        fields = ['name', 'method']

class ProfileForm(forms.ModelForm):
    context_id = forms.ModelChoiceField(queryset=Context.objects.all(), empty_label="Select context")

    class Meta:
        model=Profile
        fields=['name', 'method', 'level', 'context_id']
        exclude = ['id']

class FusionForm(forms.Form):
    actualprofile_id = forms.ModelChoiceField(queryset=Profile.objects.all(), empty_label="Select actual profile")
    officialprofile_id = forms.ModelChoiceField(queryset=Profile.objects.all(), empty_label="Select official profile")
    targetprofile_id = forms.ModelChoiceField(queryset=Profile.objects.all(), empty_label="Select target profile")




