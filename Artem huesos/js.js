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
    const emailPattern = /^[^ ]+@[^ ]+\.[a-z]{2,323}$/;
    if (!emailInput.value.match(emailPattern)){
        emailField.classList.remove("successfully");
        return emailField.classList.add("invalid");
    }
    
    else if(emailInput.value.match(emailPattern)){
        emailField.classList.remove("invalid");
        return emailField.classList.add("successfully")
      }
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
    const passPatterrn = 
      /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;

      if(!passInput.value.match(passPatterrn)){
        passField.classList.remove("successfully");
        return passField.classList.add("invalid")
      }
      
      else if(passInput.value.match(passPatterrn)){
        passField.classList.remove("invalid");
        return passField.classList.add("successfully")
      }
}

function confirmPass(){
    if (passInput.value !== cPassInput.value || cPassInput.value === ""){
        cPassField.classList.remove("successfully");
        return cPassField.classList.add("invalid");
    }
    
    else if(passInput.value === cPassInput.value && cPassInput.value !== ""){
        cPassField.classList.remove("invalid");
        return cPassField.classList.add("successfully")
      }
}
function checkUsers(){
    const usersPattern = "users";
    if (!usersInput.value.match(usersPattern)){
        usersField.classList.remove("successfully");
        return usersField.classList.add("invalid");
    }
    
    else if(usersInput.value.match(usersPattern)){
        usersField.classList.remove("invalid");
        return usersField.classList.add("successfully")
      }
}
form.addEventListener("submit", (e) => {
    e.preventDefault();
    checkUsers();
    checkEmail();
    createPass();
    confirmPass();

    usersInput.addEventListener("keyup", checkUsers);
    emailInput.addEventListener("keyup", checkEmail);
    passInput.addEventListener("keyup", createPass);
    cPassInput.addEventListener("keyup", confirmPass);

    if (
        !usersField.classList.contains("invalid") &&
        !emailField.classList.contains("invalid") &&
        !passField.classList.contains("invalid") &&
        !cPassField.classList.contains("invalid")
    ) {
        location.href = form.getAttribute("method");
    }
});