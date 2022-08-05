const container = document.querySelector(".container"),
       pwShowHide  = document.querySelectorAll(".ewe"),
       pwShowHide2  = document.querySelectorAll(".ewe2"),
       pwFields = document.querySelectorAll(".password1"),
       pwFields2 = document.querySelectorAll(".password2");

pwShowHide.forEach(eyeIcon => {
    eyeIcon.addEventListener("click", ()=>{
        pwFields.forEach(pwField => {
            if(pwField.type === "password"){
                pwField.type = "text";
            }else{
                pwField.type = "password";
            }
        })
    })
})
pwShowHide2.forEach(eyeIcon => {
    eyeIcon.addEventListener("click", ()=>{
        pwFields2.forEach(pwFields2 => {
            if(pwFields2.type === "password"){
                pwFields2.type = "text";
            }else{
                pwFields2.type = "password";
            }
        })
    })
})

function checkPassword(){
    let password = document.getElementById("passwordBox");
    let passwordEntered = password.value;
    let password2 = document.getElementById("passwordBox1");
    let passwordEntered2 = password2.value;

    let elem = document.getElementById('alert');

    if(passwordEntered === passwordEntered2 && passwordEntered != ""){
        return true;
        console.log("gdfsgsd")
    } else if(passwordEntered2 !== ""){
        elem.innerHTML = "Пароли не совпадают";
        return false;
    }
    let nickname = document.getElementById("nicknamedBox1");
    let nicknameEntered = nickname.value;
    let email = document.getElementById("emailBox1");
    let emailEntered = email.value;

    let elemCheck = document.getElementById('check');
} 