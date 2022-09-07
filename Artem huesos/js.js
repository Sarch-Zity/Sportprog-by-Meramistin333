
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
    const emailBaza = "Kslsider@gmail.com";
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
        if (!emailInput.value.match(emailBaza)){
        emailField.classList.remove("successfully");
        emailField.classList.remove("invalid2");
        emailField.classList.remove("invalid3");
        return emailField.classList.add("invalid");
        
    } if (
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
      /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,128}$/;

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
            initial = window.setTimeout(() => {
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
        }, 1000);
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
        const usersBaza = "users";
        const usersPattern = /^[a-z]{4,25}$/;
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
                    async function request(url, data, csrftoken) {
                        const response = await fetch(url, {
                            method: 'POST',
                            headers: {
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'X-CSRFToken': csrftoken,
                            },
                            body: JSON.stringify(data),
                        })
                        const result = await response.text()
                        return result
                    }
                    async function check_username() {
                        const url = '{% url "check_uesrname_s" %}'
                        const data = {'uesrname': document.getElementsByName('uesrname').value, }
                        const csrftoken = '{{ csrf_token }}'
                        const result = await request(url, data, csrftoken)
                        console.log(result)
                    } check_username()
            if (
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
cPassInput.addEventListener("keyup", initialclearTimeout);
usersInput.addEventListener("keyup", initialclearTimeout);
usersInput.addEventListener("keyup", checkUsers);
emailInput.addEventListener("keyup", checkEmail);
passInput.addEventListener("keyup", createPass);
cPassInput.addEventListener("keyup", confirmPass);


form.addEventListener("submit", (e) => {
    e.preventDefault();
    checkEmail();
    checkUsers();
    createPass();
    confirmPass();
    if (
        !usersField.classList.contains("invalid") &&
        !emailField.classList.contains("invalid") &&
        !passField.classList.contains("invalid") &&
        !cPassField.classList.contains("invalid") &&

        usersField.classList.contains("successfully") &&
        emailField.classList.contains("successfully") &&
        passField.classList.contains("successfully") &&
        cPassField.classList.contains("successfully")
    ) {
        location.href = form.getAttribute("method");
    }
});