document.addEventListener("DOMContentLoaded", function () {
// Timeout function for messages taken from I Think Therefore I Blog walkthrough
setTimeout(function () {
    let messages = document.getElementById("msg");
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 3000);
});