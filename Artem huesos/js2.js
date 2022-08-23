const form = document.querySelector("form"),
usersField = form.querySelector(".users-field"),
usersInput = usersField.querySelector(".users"),
passField = form.querySelector(".create-password"),
passInput = passField.querySelector(".password")

function createPass(){
    if (true) 
{
  const passPatterrn = 
      /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,35}$/;

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
    if (true) 
    {
        usersField.classList.remove("invalid");
        usersField.classList.remove("invalid2");
        usersField.classList.remove("invalid3");
        const usersBaza = "users";
        const usersPattern = /^[a-z]{4,40}$/;
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
            function initialon(){
                initial = window.setTimeout(() => {  
            console.log("fssds")    
            if (!usersInput.value.match(usersBaza)){
            usersField.classList.remove("successfully");
            usersField.classList.remove("invalid2");
            usersField.classList.remove("invalid3");
            return usersField.classList.add("invalid");
            
        } if (
                !usersField.classList.contains("invalid") &&
                !usersField.classList.contains("invalid2") &&
                !usersField.classList.contains("invalid3")
            ) {
                usersField.classList.remove("invalid");
            usersField.classList.remove("invalid2");
            usersField.classList.remove("invalid3");
            return usersField.classList.add("successfully");
            } }, 1000);
            }
            
            initialon();
        }}}
}
function initialclearTimeout()
{
    clearTimeout(initial);
}
usersInput.addEventListener("keyup", checkUsers);
passInput.addEventListener("keyup", createPass);
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