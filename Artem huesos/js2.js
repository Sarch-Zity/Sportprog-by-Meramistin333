const form = document.querySelector("form"),
usersField = form.querySelector(".users-field"),
usersInput = usersField.querySelector(".users"),
passField = form.querySelector(".create-password"),
passInput = passField.querySelector(".password")

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
    createPass();

    usersInput.addEventListener("keyup", checkUsers);
    passInput.addEventListener("keyup", createPass);

    if (
        !usersField.classList.contains("invalid") &&
        !passField.classList.contains("invalid")
    ) {
        location.href = form.getAttribute("method");
    }
});