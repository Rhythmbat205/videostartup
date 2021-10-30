from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    name = forms.CharField(widget=forms.Textarea(attrs={'class': 'textarea'}), required=True)
    email = forms.CharField(widget=forms.Textarea(attrs={'class': 'textarea'}), required=True)
    meeting_time =  forms.CharField(widget=forms.Textarea(attrs={'class': 'textarea'}), required=True)
    meeting_date = forms.CharField(widget=forms.Textarea(attrs={'class': 'textarea'}), required=True)
    remarks = forms.CharField(widget=forms.Textarea(attrs={'class': 'textarea'}), required=False)
    
    class Meta:
        model = Booking
        fields = ('name','email','meeting_time','meeting_date','remarks')