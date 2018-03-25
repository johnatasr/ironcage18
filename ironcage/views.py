from datetime import datetime, timezone

import structlog

from django.conf import settings
from django.contrib import messages
from django.shortcuts import redirect, render

logger = structlog.get_logger()


def index(request):
    user = request.user

    if user.is_authenticated:
        if user.get_ticket() is not None and not user.profile_complete():
            messages.warning(request, 'Your profile is incomplete')
        context = {
            'ticket': user.get_ticket(),
            'orders': user.orders.all(),
            'ticket_sales_open': datetime.now(timezone.utc) < settings.TICKET_SALES_CLOSE_AT,
        }
    else:
        context = {
            'ticket_sales_open': datetime.now(timezone.utc) < settings.TICKET_SALES_CLOSE_AT,
        }

    return render(request, 'ironcage/index.html', context)


def error(request):
    1 / 0


def log(request):
    logger.info('Test log')
    return redirect('index')