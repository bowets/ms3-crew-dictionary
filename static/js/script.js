function checkPassword() {
    let password = document.querySelector('#regpassword');
    let confirm = document.querySelector('#cregpassword');
    if(confirm.value == password.value) {
        confirm.setCustomValidity('');
    } else {
        confirm.setCustomValidity('Passwords do not match')
    }
}