import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from catalog.models import BookInstance, Author

# make it as a Form
class RenewBookForm(forms.Form):
    """ Defines form which allows librarians to update due_back time of a book instance"""

    renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")

    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']
        
        # Check if a date is not in the past. 
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past'))

        # Check if a date is in the allowed range (+4 weeks from today).
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))

        # Remember to always return the cleaned data.
        return data

# make it as a ModelForm
class RenewBookModelForm(forms.ModelForm):
    def clean_due_back(self):
       data = self.cleaned_data['due_back']
       
       # Check if a date is not in the past.
       if data < datetime.date.today():
           raise ValidationError(_('Invalid date - renewal in past'))

       # Check if a date is in the allowed range (+4 weeks from today).
       if data > datetime.date.today() + datetime.timedelta(weeks=4):
           raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))

       # Remember to always return the cleaned data.
       return data

    class Meta:
        model = BookInstance
        fields = ['due_back']
        labels = {'due_back': _('Renewal date')}
        help_texts = {'due_back': _('Enter a date between now and 4 weeks (default 3).')}


class AuthorCreateForm(forms.ModelForm):    
    def clean_date_of_death(self):
        data = self.cleaned_data['date_of_death']
        if data and data > datetime.date.today():
            raise ValidationError(_('Invalid date - date of death in future'))

        return data

    def clean_date_of_birth(self):
        data = self.cleaned_data['date_of_birth']
        if data and data > datetime.date.today():
            raise ValidationError(_('Invalid date - date of birth in future'))

        return data

    def clean(self):
        cleaned_data = super().clean()
        date_of_birth = cleaned_data.get("date_of_birth")
        date_of_death = cleaned_data.get("date_of_death")

        if date_of_birth and date_of_death:
            if date_of_death <= date_of_birth:
                raise ValidationError(_('Invalid dates - date of death should be greater than date of birth'))

    class Meta:
        model = Author
        fields = '__all__'
