const filetext = document.querySelector(".upload_text_");
const fileinput = document.querySelector(".upload_text");
const fileinputContainer = document.querySelector(".upload_input_container");
        
        
function getoutput()
    {
const fullPath = document.getElementById('upload').value;  
const startIndex = (fullPath.indexOf('\\') >= 0 ? fullPath.lastIndexOf('\\') : fullPath.lastIndexOf('/'));
const filename = fullPath.substring(startIndex);
    if(filename != ""){
        filetext.innerHTML = filename;
        const icon_file = document.querySelector('.bxl-dropbox');
        icon_file.classList.remove("bx-tada");
        icon_file.classList.add("bx-package");
        return true;
    }
    icon_file.classList.remove("bx-package");
        icon_file.classList.add("bx-tada");
    filetext.innerHTML = "Загрузите файл";
        }

// const seconds = document.querySelector(".seconds .number");
// const minutes = document.querySelector(".minutes .number");
// const hours = document.querySelector(".hours .number");

// let secValue = 58,
// minValue = 30,
// hourValue = 1

// const timeFunctin = setInterval(() => {
//     secValue--;

//     if (secValue == 0) {
//         minValue--;
//         secValue = 60;
//     }
//     if (minValue == 0) {
//         hourValue--;
//         minValue = 60;
//     }
//     seconds.textContent = secValue < 10 ? `0${secValue}` : secValue;
//     minutes.textContent = minValue < 10 ? `0${minValue}` : minValue;
//     hours.textContent = hourValue < 10 ? `0${hourValue}` : hourValue;
// }, 1000);
const optionMenu = document.querySelector(".select-menu"),
selectBtn = optionMenu.querySelector(".select-btn"),
options = optionMenu.querySelectorAll(".option"),
sBtn_text = optionMenu.querySelector(".sBtn-text");
          
const toggleMenu = function () {
    optionMenu.classList.toggle("active");
}

selectBtn.addEventListener("click", function (e) {
    e.stopPropagation();
    toggleMenu();
});

document.addEventListener("click", function (e) {
    const target = e.target;
    const its_menu = target == optionMenu || optionMenu.contains(target);
    const its_btnMenu = target == selectBtn;
    const menu_is_active = optionMenu.classList.contains("active");

    if (!its_menu && !its_btnMenu && menu_is_active) {
        toggleMenu();
    }
});
options.forEach(option =>{
    option.addEventListener("click", ()=>{
        let selectedOption = option.querySelector(".option-text").innerText;
        sBtn_text.innerText = selectedOption;
        let selectedOptionAttribyteQuerySelector = option.querySelector(".option-text");
        let selectedOptionAttribyte = selectedOptionAttribyteQuerySelector.dataset.type;
        ileinput.setAttribute("accept", selectedOptionAttribyte);

     
        optionMenu.classList.remove("active");
    });
});


fileinputContainer.addEventListener("mouseover", ()=> {
    const icon_file = document.querySelector('.bxl-dropbox');
    icon_file.classList.add("bx-tada");
});
fileinputContainer.addEventListener("mouseout", ()=> {
    const icon_file = document.querySelector('.bxl-dropbox');
    icon_file.classList.remove("bx-tada");
});

     const tabs = document.querySelectorAll(".tab");
const contents = document.querySelectorAll(".content");
 
for (let i = 0; i < tabs.length; i++) {
	tabs[i].addEventListener("click", ( event ) => {
 
		let tabsChildren = event.target.parentElement.children;
		for (let t = 0; t < tabsChildren.length; t++) {
			tabsChildren[t].classList.remove("tab--active");
		}
		tabs[i].classList.add("tab--active");
		let tabContentChildren = document.querySelector('.container_content').children;
		for (let c = 0; c < tabContentChildren.length; c++) {
			tabContentChildren[c].classList.remove("content--active");
		}
		contents[i].classList.add("content--active");
 
	});
}