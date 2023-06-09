document.getElementById('js-contact-btn').addEventListener('click', function(e) {
    e.preventDefault();

    var emailInput = document.querySelector('input[name="email"]');
    var email = emailInput.value;

    fetch('../api/contact', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            email: email
        })
    })
    .then(function(response) {
        return response.text();
    })
    .then(function(text) {
        var resultDiv = document.getElementById('js-contact-result');
        if (text === 'success') {
            resultDiv.textContent = resultDiv.getAttribute('data-success-msg');
        } else {
            resultDiv.textContent = resultDiv.getAttribute('data-error-msg');
        }
    })
    .catch(function(error) {
        var resultDiv = document.getElementById('js-contact-result');
        resultDiv.textContent = resultDiv.getAttribute('data-error-msg');
    });
});