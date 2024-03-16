const header_burger = document.querySelector(".header_burger-btn"),
menu_bar = document.querySelector('.menu-bar'),
blackout = document.querySelector(".blackout"),
sidebar = document.querySelector(".sidebar");
header_burger.addEventListener("click", () => {
    if(menu_bar.classList.contains("open")){
        menu_bar.classList.remove("open");
        blackout.classList.remove("open");
        sidebar.classList.remove("open");
    } else {
        menu_bar.classList.add("open");
        blackout.classList.add("open");
        sidebar.classList.add("open");
    }
});

const cookie_content = document.querySelector(".cookie_fail_content"),
cookie_input = document.querySelector(".close_cockie_input");
cookie_input.addEventListener("click", () => {
    cookie_content.classList.remove("cookie_true");
    cookie_content.classList.add("cookie_false");
})



document.addEventListener('DOMContentLoaded', () => {
    const contentDiv = document.querySelector('.content');
    const navLinks = document.querySelectorAll('.nav-link-fetch');
    // const loadingOverlay = document.querySelector('.loading-overlay');
  
    // const showLoadingOverlay = () => {
    //   loadingOverlay.style.opacity = '1';
    // };
  
    // const hideLoadingOverlay = () => {
    //   loadingOverlay.style.opacity = '0';
    // };
  
    const loadScripts = (url) => {
    let head = window.document.getElementsByTagName('head')[0]
      if (url.includes('home')) {
        $.getScript("http://127.0.0.1:8000/static/main/js/home.js"); 
        // const accordionContent = document.querySelectorAll(".block");

        // accordionContent.forEach((item, index) => {
        //     let header = item.querySelector("header");
        //     header.addEventListener("click", () =>{
        //         item.classList.toggle("open");
        
        //         let description = item.querySelector(".text-1");
        //         if(item.classList.contains("open")){
        //             description.style.height = `${description.scrollHeight + 15}px`; //scrollHeight property returns the height of an element including padding , but excluding borders, scrollbar or margin
        //             item.querySelector("i").classList.replace("bx-rotate-270", "bx-rotate-90");
        //         }else{
        //             description.style.height = "0px";
        //             item.querySelector("i").classList.replace("bx-rotate-90", "bx-rotate-270");
        //         }
        //         removeOpen(index); //calling the funtion and also passing the index number of the clicked header
        //     })
        // })
        
        // function removeOpen(index1){
        //     accordionContent.forEach((item2, index2) => {
        //         if(index1 != index2){
        //             item2.classList.remove("open");
        
        //             let des = item2.querySelector(".text-1");
        //             des.style.height = "0px";
        //             item2.querySelector("i").classList.replace("bx-rotate-90", "bx-rotate-270");
        //         }
        //     })
        // }
      }
      else if (url.includes('top')) {
        var count = document.querySelectorAll('.string').length;
var cnt = 20;
var cnt_page = Math.ceil(count / cnt);

var paginator = document.querySelector(".paginator");
function create_button(){
    var page = "";
    for (var i = 0; i < cnt_page; i++) {
  page += "<span class='pagination_button paginator_pasive' data-page=" + i * cnt + "  id=\"page" + (i + 1) + "\">" + (i + 1) + "</span>";
}
paginator.innerHTML = page;
var main_page = document.getElementById("page1");
main_page.classList.remove("paginator_pasive");
main_page.classList.add("paginator_active");
}
create_button();
var main_page = document.getElementById("page1");
function ne_otobchachenie() {
    for (var i = 0; i < div_num.length; i++) {
  if (i < count) {
    div_num[i].style.display = "none";
  }
}
}
function otobrachenie() {
    for (var i = 0; i < div_num.length; i++) {
  if (i < cnt) {
    div_num[i].style.display = "";
  }
}
}
var div_num = document.querySelectorAll(".string");
otobrachenie();

var main_page = document.getElementById("page1");
main_page.classList.remove("paginator_pasive");
main_page.classList.add("paginator_active");


function pagination(event) {
  var main_page_main = document.querySelectorAll(".pagination_button");
  var e = event || window.event;
  var target = e.target;
  var id = target.id;
  
  if (target.tagName.toLowerCase() != "span") return;
  
  var num_ = id.substr(4);
  var data_page = +target.dataset.page;
  for(var i = 0; i < main_page_main.length; i++){
    main_page_main[i].classList.add("paginator_pasive");
  }
  main_page.classList.remove("paginator_active");
  main_page = document.getElementById(id);
  main_page.classList.remove("paginator_pasive");
  main_page.classList.add("paginator_active");

  var j = 0;
  for (var i = 0; i < div_num.length; i++) {
    var data_num = div_num[i].dataset.num;
    if (data_num <= data_page || data_num >= data_page)
      div_num[i].style.display = "none";

  }
  for (var i = data_page; i < div_num.length; i++) {
    if (j >= cnt) break;
    div_num[i].style.display = "";
    j++;
  }
}
let inputBox = document.querySelector(".search_container"),
            searchIcon = document.querySelector(".icon_"),
            closeIcon = document.querySelector(".x_close");
console.log(closeIcon)
searchIcon.addEventListener("click", () => inputBox.classList.add("open"));
closeIcon.addEventListener("click", () => {
    inputBox.classList.remove("open");
    document.querySelector('#elastik').value = ""
    let elastikItems = document.querySelectorAll('.elastik tr');
    elastikItems.forEach(function (elem) {
            let elem_itemms = elem.querySelector('.position__user')
            elem.style.display = "none";

            elem_itemms.innerHTML = elem_itemms.innerText;
        });
        otobrachenie();
        create_button();
});

        document.querySelector('#elastik').oninput = function () {
            let val = this.value.trim();
            let elastikItems = document.querySelectorAll('.elastik tr');
            var main_page_main = document.querySelectorAll(".pagination_button");
            if (val != '') {
                ne_otobchachenie();
                if(main_page_main.length != 0){
                    for(var i = 0; i < cnt_page; i++){
                    main_page_main[i].remove()
                };
                }
                elastikItems.forEach(function (elem) {
                    let elem_itemms = elem.querySelector('.position__user');
                    let elem_itemms_upper = elem_itemms.textContent.toLowerCase();
                    if (elem_itemms_upper.search(val.toLowerCase()) == -1) {
                        elem.style.display = "none";
                    }
                    else {
                        elem.style.display = "";
                        let str = elem_itemms.innerText;
                    }
                });
            }
            else {
                ne_otobchachenie();
                otobrachenie();
                create_button();
            }
        }
      
      }
      else if(url.includes('competition')){
        $.getScript("competition_now.js"); 
      };
    };

  
    const loadPage = (url) => {
      // showLoadingOverlay();
  
      fetch(url)
        .then(response => response.text())
        .then(html => {
          const parser = new DOMParser();
          const doc = parser.parseFromString(html, 'text/html');
          
          const newContent = doc.querySelector('.content').innerHTML;
          
          contentDiv.classList.add('fade-out');
          
          contentDiv.innerHTML = newContent;
          document.title = doc.title;

          setTimeout(() => {
            contentDiv.classList.remove('fade-out');
            history.pushState({}, '', url);
            // hideLoadingOverlay();
          }, 500);
        })
        .then(() => {
          loadScripts(url);
        });
    };
  
    navLinks.forEach(el => {
      el.addEventListener('click', (e) => {
        e.preventDefault();
  
        const url = e.currentTarget.getAttribute('href');
        loadPage(url);
      });
    });
  
    loadPage(window.location.pathname);
  
    window.addEventListener('popstate', () => {
      loadPage(window.location.pathname);
    });
  });