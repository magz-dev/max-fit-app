/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment

    CSS from here: 
    https://stripe.com/docs/stripe-js
*/

// Retrieve the elements by their IDs
const publicKeyElement = document.getElementById('id_stripe_public_key');
const secretElement = document.getElementById('id_client_secret');

// Extract the content without the first and last characters
const stripePublicKey = publicKeyElement.textContent.slice(1, -1);
const clientSecret = secretElement.textContent.slice(1, -1);

// Create a stripe instance using the public key
const stripe = Stripe(publicKey);

// Create an elements instance
const elements = stripe.elements();

// Define style for the card element
const cardStyle = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};

// Create a card element with the specified style
const cardElement = elements.create('card', {
    style: cardStyle
});

// Mount the card element to the div with id 'card-element'
cardElement.mount('#card-element');