
// Function to check the passwords match on the register page
// This code was taken from StackOverflow (https://stackoverflow.com/questions/21727317/how-to-check-confirm-password-field-in-form-without-reloading-page/21727518) submitted by user "laggingreflex"
function checkPassword() {
    let password = document.querySelector('#regpassword');
    let confirm = document.querySelector('#cregpassword');
    if(confirm.value == password.value) {
        confirm.setCustomValidity('');
    } else {
        confirm.setCustomValidity('Passwords do not match')
    }
}