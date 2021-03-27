function validateScript(type){
    let validations = {
        l_email: "",
        l_password: "",
    },

    d = document,

    login = d.getElementById('login'),
    l_email = d.getElementById("l_email"),
    l_password = d.getElementById("l_password")

    validations.l_email = l_email.value
    validations.l_password = l_password.value

    if (validations.l_email.length >= 2 && 
        validations["l_email"].includes("@") && 
        validations.l_password.length >= 8) {
        login.disabled = false;
    } else {
        login.disabled = true
    }
}