from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.contrib.auth.decorators import login_required

import braintree

from orders.models import Order
from . tasks import payment_completed

# instantiate braintree payment gateway

gateway = braintree.BraintreeGateway(settings.BRAINTREE_CONF)

@login_required
def payment_process(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id =order_id)
    total_cost = order.get_total_cost()

    if request.method == 'POST':
        # retrieve nonce 
        nonce = request.POST.get('payment_method_nonce', None)
        # create and submit transaction
        result = gateway.transaction.sale({
            'amount': f'{total_cost: 2f}',
            'payment_method_nonce': nonce,
            'options': {
                'submit_for_settlement': True
            }
        })

        if result.is_success:
            # mark the order as paid 
            order.paid = True
            # store unique transaction tree 
            order.braintree_id = result.transaction.id
            order.save()
            # launch asynchronous task 
            payment_completed(order.id)
            return redirect('payment:done')
        else:
            return redirect('payment:canceled')
        
    else:
        # generate token
        client_token = gateway.client_token.generate()
        return render(request, 
                    'payment/process.html', 
                    {'order': order, 'client_token': client_token})
@login_required 
def payment_done(request):
    return render(request, 'payment/done.html')

@login_required
def paymemnt_canceled(request):
    return render(request, 'payment/canceled.html')

