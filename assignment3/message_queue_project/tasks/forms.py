from django import forms
from .models import SecureModel

class SecureModelForm(forms.ModelForm):
    class Meta:
        model = SecureModel
        fields = ['name', 'url']

    def clean_name(self):
        name = self.cleaned_data['name']
        # Prevent XSS
        return name.strip()
    
class DataUploadForm(forms.ModelForm):
    class Meta:
        model = DataUpload
        fields = ['file']
def clean_file(self):
    file = self.cleaned_data['file']
    if not file.name.endswith('.csv'):
        raise forms.ValidationError("Only CSV files are allowed!")
    return file
