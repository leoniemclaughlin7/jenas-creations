document.addEventListener("DOMContentLoaded", function () {

  //JavaScrip to handle quantity selector taken from Boutique Ado walkthrough.

  //Call handleEnableDisable on all quantity inputs.
  var allQtyInputs = $('.quantity');
  for (var i = 0; i < allQtyInputs.length; i++) {
    var productId = $(allQtyInputs[i]).data('product_id');
    handleEnableDisable(productId);
  }


  //Decrement quantity.
  $('.decrement').on('click', function (e) {
    e.preventDefault();
    var closestInput = $(this).closest('.input-group').find('.quantity')[0];
    var currentValueNow = parseInt($(closestInput).val());
    $(closestInput).val(currentValueNow - 1);
    var productId = $(this).data('product_id');
    handleEnableDisable(productId);
  });

  // Increment quantity.
  $('.increment').on('click', function (e) {
    e.preventDefault();
    var closestInput = $(this).closest('.input-group').find('.quantity')[0];
    var currentValueNow = parseInt($(closestInput).val());
    $(closestInput).val(currentValueNow + 1);
    var productId = $(this).data('product_id');
    handleEnableDisable(productId);
  });

  // Disable +/- buttons outside 1-50 range.
  function handleEnableDisable(productId) {
    var currentValue = parseInt($(`#quantity_${productId}`).val());
    var minusDisabled = currentValue < 2;
    var plusDisabled = currentValue > 49;
    $(`#decrement_${productId}`).prop('disabled', minusDisabled);
    $(`#increment_${productId}`).prop('disabled', plusDisabled);

  }

  //Call handleEnableDisable when quantity changes.
  $('.quantity').change(function () {
    var productId = $(this).data('product_id');
    handleEnableDisable(productId);
  });

});

document.addEventListener('DOMContentLoaded', function () {
  // JavaScript to enable bootstrap toast notifications. 
  var toasts = document.querySelector('.toast');
  var toast = new bootstrap.Toast(toasts);

  toast.show();

  var toastClose = toasts.querySelector('.close');
  toastClose.addEventListener('click', function () {
    toast.hide();
  });
});