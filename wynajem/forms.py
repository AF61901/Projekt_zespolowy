from django import forms
from .models import Zamow

class DateInput(forms.DateInput):
    input_type = 'date'

class ZamowForm(forms.ModelForm):
    MIEJSCE_SELECT = (
        ('0', 'Rzeszów, Dworzec Główny PKP'),
        ('1', 'Rzeszów, Lotnisko Jasionka'),
        ('2', 'Sopot, Dworzec Główny PKP'),
        ('3', 'Warszawa, Lotnisko Chopina'),
        ('4', 'Warszawa, Metro Wilanowska'),
        ('5', 'Warszawa, Dworzec Centralny'),
        ('6', 'Wrocław, Dworzec Główny PKP'),
        ('7', 'Sosnowiec, Dworzec Główny PKP'),
        ('8', 'Poznań, Lotnisko Ławica'),
        ('9', 'Olsztyn, Dworzec Główny PKP'),
        ('10', 'Łódź, Dworzec Łódź Kaliska'),
    )
    miejsce_odbioru = forms.ChoiceField(choices=MIEJSCE_SELECT, required = True)
    miejsce_oddania = forms.ChoiceField(choices=MIEJSCE_SELECT, required = True)
    data_odbioru = forms.DateField(widget=DateInput)
    data_oddania = forms.DateField(widget=DateInput)
    class Meta:
        model = Zamow
        fields = [
            "miejsce_odbioru",
            "miejsce_oddania",
            "data_odbioru",
            "data_oddania",
        ]
