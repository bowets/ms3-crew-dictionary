// Checks that the user entered the password correctly  
document.querySelector('#register-submit').onclick = function() {
    let password = document.querySelector('#regpassword').value,
        confirmPassword = document.querySelector('#cregpassword').value;

    if (password != confirmPassword) {
        alert("Your passwords don't match. Please try again");
        confirmPassword.focus();
        return false
    }
    return true
    
}