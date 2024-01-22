from datetime import timedelta

from django.shortcuts import render
from django.utils import timezone

from .models import Order, Product


def order_list(request):
    orders_last_week = Order.objects.filter(order_date__gte=timezone.now() - timedelta(days=7))
    orders_last_month = Order.objects.filter(order_date__gte=timezone.now() - timedelta(days=30))
    orders_last_year = Order.objects.filter(order_date__gte=timezone.now() - timedelta(days=365))
    products = Product.objects.all().distinct()

    context = {
        'orders_last_week': orders_last_week,
        'orders_last_month': orders_last_month,
        'orders_last_year': orders_last_year,
        'products': products,
    }

    return render(request, 'orders/order_list.html', context)
