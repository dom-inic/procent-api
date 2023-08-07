let form = document.querySelector('#payment');
let submit = document.querySelector('input[type="submit"]');

braintree.client.create({
    authorization: '{{ client_token }}'
}, function(clientErr, clientInstance){
    if (clientErr){
        console.error(clientErr);
        return;
    }

    braintree.hostedFields.create({
        client: clientInstance,
        styles: {
            'input': {'font-size': '13px'},
            'input.invalid': {'color': 'red'},
            'input.valid': {'color': 'green'}
        },
        fields: {
            number: {selector: '#card-number'},
            cvv: {selector: '#cvv'},
            expirationDate: {selector: '#expiration-date'}
        }
    }, function(hosedFieldsErr, hostedFieldsInstance){
        if (hosedFieldsErr){
            console.error(hosedFieldsErr);
            return;
        }
        submit.removeAttribute('disabled');
        form.addEventListener('submit', function(event){
            event.preventDefault();
            hostedFieldsInstance.tokenize(function (tokenizeErr, payload) {
                if (tokenizeErr){
                    console.error(tokenizeErr);
                    return;
                }
                // set nonce to send to server
                document.getElementById('nonce').value = payload.nonce;
                // submit form
                document.getElementById('payment').submit();
            });
        }, false);
    });
});