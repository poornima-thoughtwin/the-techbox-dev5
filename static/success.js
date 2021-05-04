const manageBillingForm = document.querySelector('#manage-billing-form');
manageBillingForm.addEventListener('submit', function(e) {
  e.preventDefault();
  fetch('/customer-portal', {
    method: 'POST'
  })
    .then(function(response) {
      return response.json()
    })
    .then(function(data) {
      window.location.href = data.url;
    })
    .catch(function(error) {
      console.error('Error:', error);
    });
});