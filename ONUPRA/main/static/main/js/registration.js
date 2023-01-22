const form = document.querySelector("form"),
usersField = form.querySelector(".users-field"),
usersInput = usersField.querySelector(".users"),
emailField = form.querySelector(".email-field"),
emailInput = emailField.querySelector(".email"),
passField = form.querySelector(".create-password"),
passInput = passField.querySelector(".password"),
cPassField = form.querySelector(".confirm-password"),
cPassInput = cPassField.querySelector(".cPassword");

function checkEmail() {
    if (true) 
{
    emailField.classList.remove("invalid");
    emailField.classList.remove("invalid2");
    emailField.classList.remove("invalid3");
    const emailPattern = /^[^ ]+@[^ ]+\.[a-z]{2,100}$/;
    if (emailInput.value === ''){
        emailField.classList.remove("successfully");
        emailField.classList.remove("invalid");
        emailField.classList.remove("invalid2");
        return emailField.classList.add("invalid3"); }
    if (true) 
    {
        if (!emailInput.value.match(emailPattern)){
        emailField.classList.remove("successfully");
        emailField.classList.remove("invalid");
        emailField.classList.remove("invalid3");
        return emailField.classList.add("invalid2");
    }
    if (true) 
    {
        if (
            !emailField.classList.contains("invalid") &&
            !emailField.classList.contains("invalid2") &&
            !emailField.classList.contains("invalid3")
        ) {
            emailField.classList.remove("invalid");
        emailField.classList.remove("invalid2");
        emailField.classList.remove("invalid3");
        return emailField.classList.add("successfully");
        }
    }}}
    
}


const eyeIcons = document.querySelectorAll(".show-hide");

eyeIcons.forEach((eyeIcon) => {
    eyeIcon.addEventListener("click", () => {
        const pInput = eyeIcon.parentElement.querySelector("input");
        
        if(pInput.type === "password"){
            eyeIcon.classList.replace("bx-hide", "bx-show");
            return pInput.type = "text";
        }
        eyeIcon.classList.replace("bx-show", "bx-hide");
        return pInput.type = "password";
    });
});


function createPass(){
    if (true) 
{
  const passPatterrn = 
    /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[-_=+)('"!@#№;$%?&*|/,.])[A-Za-z\d-_=+)('"!@#№;$%?&*|/,.]{8,128}$/;

    passField.classList.remove("invalid2");
    passField.classList.remove("invalid3");
    if (passInput.value === ''){
        passField.classList.remove("successfully");
        passField.classList.remove("invalid2");
        return passField.classList.add("invalid3"); }
    if (true) 
    {
        if (!passInput.value.match(passPatterrn)){
        passField.classList.remove("successfully");
        passField.classList.remove("invalid3");
        return passField.classList.add("invalid2");
    }
    
        if (
            !passField.classList.contains("invalid2") &&
            !passField.classList.contains("invalid3")
        ) {
        passField.classList.remove("invalid2");
        passField.classList.remove("invalid3");
        return passField.classList.add("successfully");
        }
    }}
}


function confirmPass(){
    if (true) 
{
    cPassField.classList.remove("invalid2");
    cPassField.classList.remove("invalid3");
    if (cPassInput.value === ''){
        cPassField.classList.remove("successfully");
        cPassField.classList.remove("invalid2");
        return cPassField.classList.add("invalid3"); }
    if (true) 
    {
        function initialon(){
        if (passInput.value !== cPassInput.value){
        cPassField.classList.remove("successfully");
        cPassField.classList.remove("invalid3");
        return cPassField.classList.add("invalid2"); 
    }
        
        if (
            !cPassField.classList.contains("invalid2") &&
            !cPassField.classList.contains("invalid3")
        ) {
        cPassField.classList.remove("invalid2");
        cPassField.classList.remove("invalid3");
        return cPassField.classList.add("successfully");
        }
    }
    initialon();
    }}
}

var initial;
function checkUsers(){
    if (true) 
    {
        usersField.classList.remove("invalid");
        usersField.classList.remove("invalid2");
        usersField.classList.remove("invalid3");
        const usersPattern = /^[a-zA-Z0-9-_=+)('"!@#№;$%?&*|/,.]{3,16}$/;
        if (usersInput.value === ''){
            usersField.classList.remove("successfully");
            usersField.classList.remove("invalid");
            usersField.classList.remove("invalid2");
            return usersField.classList.add("invalid3"); }
        if (true) 
        {
            if (!usersInput.value.match(usersPattern)){
            usersField.classList.remove("successfully");
            usersField.classList.remove("invalid");
            usersField.classList.remove("invalid3");
            return usersField.classList.add("invalid2");
        }
        if (true) 
        {   
            if (
                !usersField.classList.contains("invalid") &&
                !usersField.classList.contains("invalid2") &&
                !usersField.classList.contains("invalid3")
            ) {
                usersField.classList.remove("invalid");
            usersField.classList.remove("invalid2");
            usersField.classList.remove("invalid3");
            return usersField.classList.add("successfully");
            } 
        }}}
}
usersInput.addEventListener("keyup", () => {
    checkUsers();
    validation_check();
});
emailInput.addEventListener("keyup", () => {
    checkEmail();
    validation_check();
});
passInput.addEventListener("keyup", () => {
    createPass();
    validation_check();
    if(!cPassInput.value == ''){
        confirmPass();
        console.log(1)
    } 
});
cPassInput.addEventListener("keyup", () => {
    confirmPass();
    console.log(123);
    validation_check();
});


function validation_check()
{
    if (
        usersField.classList.contains("successfully") &&
        emailField.classList.contains("successfully") &&
        passField.classList.contains("successfully") &&
        cPassField.classList.contains("successfully")
    ) {
        document.getElementById('button_form').removeAttribute('disabled');
    }
    else{
        document.getElementById('button_form').disabled = 'disabled';
    }
}
validation_check();


// form.addEventListener("submit", (e) => {
//     e.preventDefault();
//     checkEmail();
//     checkUsers();
//     createPass();
//     confirmPass();
//     if (
//         !usersField.classList.contains("invalid") &&
//         !emailField.classList.contains("invalid") &&
//         !passField.classList.contains("invalid") &&
//         !cPassField.classList.contains("invalid") &&

//         usersField.classList.contains("successfully") &&
//         emailField.classList.contains("successfully") &&
//         passField.classList.contains("successfully") &&
//         cPassField.classList.contains("successfully")
//     ) {
//         location.href = form.getAttribute("method");
//     }
// });