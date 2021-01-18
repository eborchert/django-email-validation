from django.conf import settings
from django.shortcuts import render

from .confirm import verify_token
from .errors import NotAllFieldCompiled


def verify(request, email, email_token):
    try:
        template = settings.EMAIL_PAGE_TEMPLATE
        success, user = verify_token(email, email_token)
        return render(request, template, {'success': success, 'user': user, 'request': request})
    except AttributeError:
        raise NotAllFieldCompiled('EMAIL_PAGE_TEMPLATE field not found')
