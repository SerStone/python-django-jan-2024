import os

from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template

from configs.celery import app

from core.dataclasses.user_dataclass import UserDataClass
from core.services.jwt_service import ActivateFToken, ActivateToken, JWTService


class EmailService:
    @staticmethod
    @app.task
    def __send_email(to: str, template_name: str, context: dict, subject=''):
        template = get_template(template_name)
        html_content = template.render(context)
        msg = EmailMultiAlternatives(subject, from_email=os.environ.get("EMAIL_HOST_USER"), to=[to])
        msg.attach_alternative(html_content, 'text/html')
        msg.send()

    @classmethod
    def register(cls, user: UserDataClass):
        token = JWTService.create_token(user, ActivateToken)
        url = f'http://localhost:3000/activate/{token}'
        cls.__send_email.delay(
            user.email,
            'register.html',
            {'name': user.profile.first_name, 'url': url},
            'Register'
        )

    @classmethod
    def forgot_password(cls, user: UserDataClass):
        token = JWTService.create_token(user, ActivateFToken)
        url = f'http://localhost:3000/reset/{token}'
        cls.__send_email(
            user.email,
            'forgot_pass.html',
            {'name': user.profile.first_name, 'url': url},
            'Reset Password'
        )
