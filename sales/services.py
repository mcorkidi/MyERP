def confirm_sales_order(order):
    order.status = 'confirmed'
    order.save(update_fields=['status'])


def mark_payment_paid(payment):
    payment.status = 'paid'
    payment.save(update_fields=['status'])
