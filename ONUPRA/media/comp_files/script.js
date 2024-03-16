const container = document.querySelector(".container"),
       pwShowHide  = document.querySelectorAll(".showHidePw"),
       pwFields = document.querySelectorAll(".password");

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