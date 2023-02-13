from django import forms


BIRTH_YEAR_CHOICES = [
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.'),
]

FAVORITE_COLORS_CHOICES = (('blue', 'Blue'),
                           ('green', 'Green'),
                           ('black', 'Black'))

YES_OR_NO = [
    ('Нет', 'Да'),
    ('Нет', 'Нет'),
]

SALES_TYPE = [
    ('Прямая', 'Прямая'),
    ('Альтернатива', 'Альтернатива'),
    ('Обмен', 'Обмен'),
]

OBJECTS_TYPE = [
    ('Квартира', 'Квартира'),
    ('Комната', 'Комната'),
    ('Доля', 'Доля'),
]


class ContactForm(forms.Form):
    from_email = forms.EmailField(label='Email', required=False)
    subject = forms.CharField(label='Тема', required=False)
    new_house = forms.CharField(
        label='Новостройка',
        widget=forms.Select(choices=YES_OR_NO),)
    sales_type = forms.ChoiceField(
        label='Тип продажи',
        choices=SALES_TYPE,
        widget=forms.RadioSelect(),
        )
    obj_type = forms.CharField(
        label='Тип объекта',
        widget=forms.Select(choices=OBJECTS_TYPE),)
    rooms_on_sale = forms.IntegerField(label='Кол-во комнат на продаже')
    from_email_2 = forms.EmailField(label='Email', required=False)
    subject_2 = forms.CharField(label='Тема', required=False)
    message_2 = forms.CharField(label='Сообщение', required=False)
