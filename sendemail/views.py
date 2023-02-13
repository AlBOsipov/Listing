from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from .forms import ContactForm
from config.settings import RECIPIENTS_EMAIL, DEFAULT_FROM_EMAIL
from docx import Document


def listing_view(request):
    """Take data from form send and make .docx"""
    if request.method == 'GET':
        form = ContactForm()
    elif request.method == 'POST':

        form = ContactForm(request.POST)
        # open your form to add data
        document = Document('blank.docx')
        if form.is_valid():
            form_data = {}
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            for key, value in form.cleaned_data.items():
                form_data[key] = value
            message = '\n'.join(
                '{}: {}'.format(field.label,
                                form_data[field.name]) for field in form
            )
            message_doc = '. '.join(
                '{}: {}'.format(field.label,
                                form_data[field.name]) for field in form
            )
            make_word(document, subject, message_doc)

            try:
                send_mail(f'{subject} от {from_email}', message,
                          DEFAULT_FROM_EMAIL, RECIPIENTS_EMAIL)
                file_path = f'{subject}.docx'
                return render(request, 'listing/view_word_file.html',
                              {'file_path': file_path})
            except BadHeaderError:
                return HttpResponse('Ошибка в теме письма.')

    else:
        return HttpResponse('Неверный запрос.')
    return render(request, "listing/create_listing.html", {'form': form})


def make_word(document, subject, message_doc):
    document.add_paragraph(message_doc)
    document.save(f'static/{subject}.docx')
