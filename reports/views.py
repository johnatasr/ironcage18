from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render

from accounts.models import User
from orders.models import Order
from tickets.models import Ticket
from grants.models import Application

from .reports import reports


@staff_member_required(login_url='login')
def index(request):
    return render(request, 'reports/index.html', {'reports': reports})


@staff_member_required(login_url='login')
def accounts_user(request, user_id):
    user = User.objects.get_by_user_id_or_404(user_id)
    context = {
        'user': user,
        'ticket': user.get_ticket(),
        'orders': user.orders.all(),
    }
    return render(request, 'reports/user.html', context)


@staff_member_required(login_url='login')
def tickets_order(request, order_id):
    order = Order.objects.get_by_order_id_or_404(order_id)
    context = {
        'order': order,
    }
    return render(request, 'reports/order.html', context)


@staff_member_required(login_url='login')
def tickets_ticket(request, ticket_id):
    ticket = Ticket.objects.get_by_ticket_id_or_404(ticket_id)
    context = {
        'ticket': ticket,
    }
    return render(request, 'reports/ticket.html', context)


@staff_member_required(login_url='login')
def finaid_report(request):

    from django.db.models import Avg, Count, Min, Sum
    fin_aid_accepted_replied = Application.objects.filter(
        replied_to__isnull=False, amount_awarded__gt=0
    ).aggregate(Sum('amount_awarded'))['amount_awarded__sum'] or 0

    fin_aid_awaiting = Application.objects.filter(
        replied_to__isnull=True, amount_awarded__gt=0
    ).aggregate(Sum('amount_awarded'))['amount_awarded__sum'] or 0

    context = {
        'awarded': fin_aid_accepted_replied,
        'awaiting': fin_aid_awaiting,
        'total': fin_aid_accepted_replied + fin_aid_awaiting,
    }
    return render(request, 'reports/finaid_report.html', context)
