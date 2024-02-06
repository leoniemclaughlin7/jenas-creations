document.addEventListener("DOMContentLoaded", function () {
// Timeout function for messages taken from I Think Therefore I Blog walkthrough
setTimeout(function () {
    let messages = document.getElementById("msg");
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 3000);

// Increment quantity
$('#increment').click(function(e) {
   e.preventDefault();
   var closestInput = $(this).closest('.input-group').find('.quantity')[0];
   var currentValue = parseInt($(closestInput).val());
   $(closestInput).val(currentValue + 1);
});

// Decrement quantity
$('#decrement').click(function(e) {
   e.preventDefault();
   var closestInput = $(this).closest('.input-group').find('.quantity')[0];
   var currentValue = parseInt($(closestInput).val());
   $(closestInput).val(currentValue - 1);
});

});