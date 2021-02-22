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

class FusionForm(forms.ModelForm):
    context_id = forms.ModelChoiceField(queryset=Context.objects.all(), empty_label= "Select context")
    fusion_context_id = forms.ModelChoiceField(queryset=Context.objects.all(), empty_label="Select context")

    ## secondo me devo appendere qua e fare tutto il processo dall'altro lato. dicendo che creo una contestualizzazione
    ## faccio tutto il processo di mix delle due/tre quando clicco sul bottone e mostrando nella pagina nuova la context creata
    class Meta:
        model = Fusioncontext_has_context
        field = ['context_id', 'fusion_context_id']
        exclude = ['id']

class ProfileForm(forms.ModelForm):
    context_id = forms.ModelChoiceField(queryset=Context.objects.all(), empty_label="Select context")

    class Meta:
        model=Profile
        fields=['name', 'method', 'level', 'context_id']
        exclude = ['id']