document.addEventListener("DOMContentLoaded", function () {
// Timeout function for messages taken from I Think Therefore I Blog walkthrough
setTimeout(function () {
    let messages = document.getElementById("msg");
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 3000);

// increment and decrement quantity and prevent inputs of less than 1 and greater than 50
let quantity = $('#quantity').val();
if (quantity = 1){
   $('#decrement').prop('disabled', true);
} 
$('#decrement').on('click', function(e) {
   e.preventDefault();
   let currentValueNow = $('#quantity').val(); 
   currentValueNow--;
   $('#quantity').val(currentValueNow);
      if (currentValueNow <= 1) {
        $('#decrement').prop('disabled', true);
      } else if (currentValueNow >= 50) {
         $('#increment').prop('disabled', false);
      }else {
         $('#increment').prop('disabled', false);
      }
 });

 $('#increment').on('click', function(e) {
   e.preventDefault();
   let currentValueNow = $('#quantity').val();
   currentValueNow++;
   $('#quantity').val(currentValueNow);
   $('#quantity').val(currentValueNow);
   if (currentValueNow > 49) {
     $('#increment').prop('disabled', true);
   } else if (currentValueNow >= 1) {
      $('#decrement').prop('disabled', false);
   }else {
      $('#increment').prop('disabled', false);
   }
 });

});