from django import forms
from .models import DatabaseModel
from django.utils.translation import gettext_lazy as _


# this is our ModelForm ORM which connects back to the MySQL database
class DatabaseForm(forms.ModelForm):

    # here we define all Form metadata
    class Meta:
        # this is the DatabaseModel we will connect to in this form
        model = DatabaseModel
        # these are the input fields of the form
        fields = ('col_str', 'col_num', 'col_date')
        # these are the HTML labels of the form elements
        labels = {
            'col_str': _('Produce'),
            'col_num': _('Price'),
            'col_date': _('Date'),
        }
        # these are the HTML help text next to the input field elements
        help_texts = {
            'col_str': _('(enter name of produce)'),
            'col_num': _('(enter price of produce)'),
            'col_date': _('(YYYY-MM-DD)'),
        }
