from django.core.mail import send_mail


def send_confirmation_email(email, code):
    full_link = f'http://localhost:8000/account/activate/{code}'
    send_mail(
        'Активация пользователя',
        f'Код активации: {full_link}',
        'ulanovulukbek2@gmail.com',
        [email]
    )
