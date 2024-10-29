from django import forms 

class URLForm(forms.Form):
    original_url = forms.URLField(label='Enter your URL:', widget=forms.URLInput(attrs={'class': 'form-control'}))