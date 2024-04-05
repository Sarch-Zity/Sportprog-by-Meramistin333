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
var patern = /competition\/[\d]+/
var home_pettern = /^\/$/

const cookie_content = document.querySelector(".cookie_fail_content"),
cookie_input = document.querySelector(".close_cockie_input");
cookie_input.addEventListener("click", () => {
    cookie_content.classList.remove("cookie_true");
    cookie_content.classList.add("cookie_false");
});

if ($('meta[name="authenticated"]').attr('content')){
    const popupBg = document.querySelector('.popup__bg-prem'),
          popup = document.querySelector('.popup-buy'),
          body = document.getElementById("body"),
          closePopupButton = document.querySelector('.close-popup-buy'); 
    $(".popup_buy_premium").on( "click", (e) => {
        popupBg.classList.add('active'); 
        popup.classList.add('active');
        body.style.overflow = "hidden";
    });
    $('.close-popup-buy').on( "click", (e) => {
        popupBg.classList.remove('active');
        popup.classList.remove('active');
        body.style.overflow = "auto" 
    });

    document.addEventListener('click', (e) => { 
        if(e.target === popupBg) { 
            popupBg.classList.remove('active'); 
            popup.classList.remove('active');
            body.style.overflow = "auto"
        }
    });
    
}

$(document).ready(function(){
  $.ajaxSetup({
    type: 'POST',
    url: '',
    dataType: 'json',
    
    headers: {
        'X-CSRFToken': $('meta[name="csrf-token"]').attr('content')
    },
  });
});

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
      console.log(url)
      if (url.match(home_pettern)) { 
        const accordionContent = document.querySelectorAll(".block");

        accordionContent.forEach((item, index) => {
            let header = item.querySelector("header");
            header.addEventListener("click", () =>{
                item.classList.toggle("open");
        
                let description = item.querySelector(".text-1");
                if(item.classList.contains("open")){
                    description.style.height = `${description.scrollHeight + 15}px`;
                    item.querySelector("i").classList.replace("bx-rotate-270", "bx-rotate-90");
                }else{
                    description.style.height = "0px";
                    item.querySelector("i").classList.replace("bx-rotate-90", "bx-rotate-270");
                }
                removeOpen(index); 
            })
        })
        
        function removeOpen(index1){
            accordionContent.forEach((item2, index2) => {
                if(index1 != index2){
                    item2.classList.remove("open");
        
                    let des = item2.querySelector(".text-1");
                    des.style.height = "0px";
                    item2.querySelector("i").classList.replace("bx-rotate-90", "bx-rotate-270");
                }
            })
        }
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
      else if(url.match(patern)){
        const filetext = document.querySelector(".upload_text_");
        const fileinput = document.querySelector(".upload_text");
        const fileinputContainer = document.querySelector(".upload_input_container");
        const button_task1 = document.querySelector(".button-task1");
        const button_task2 = document.querySelector(".button-task2");
        const stn_text = document.querySelector(".sBtn-text");
        const select_menu = document.querySelector(".select-menu");
        var flag_fileinput = false;
        var flag_textinput = false;

        console.log(stn_text);
        function blocked_button_task1()
        {
            if(stn_text.classList.contains("blocked_text1")){
                button_task1.disabled = 'disabled';
            }
            else{
                button_task1.removeAttribute('disabled');
        
            }
        }
        blocked_button_task1();
        
        function blocked_button_task2()
        {
            if(stn_text.classList.contains("blocked_text2")){
                button_task2.disabled = 'disabled';
            }
            else{
                button_task2.removeAttribute('disabled');
        
            }
        }
        blocked_button_task2();

        $('#textarea').on('input', (e) => {
            
            if ($('#textarea').val() != ''){
                console.log($('#textarea').val() != '')
                if (stn_text.innerText != "Список"){
                    stn_text.classList.remove("blocked_text1");
                }
                blocked_button_task1();
                return flag_textinput = true;
                
            };
            flag_textinput = false;
        });
                
        $('#upload').on("change", (e) => {
            const fullPath = document.getElementById('upload').value;  
            const startIndex = (fullPath.indexOf('\\') >= 0 ? fullPath.lastIndexOf('\\') : fullPath.lastIndexOf('/'));
            const filename = fullPath.substring(startIndex);
            const icon_file = document.querySelector('.bxl-dropbox');
            if(filename != ""){
                filetext.innerHTML = filename;
                icon_file.classList.remove("bx-tada");
                icon_file.classList.add("bx-package");
                flag_fileinput = true;
                console.log(stn_text.innerText);
                if (stn_text.innerText != "Список"){
                    stn_text.classList.remove("blocked_text2");
                }
                blocked_button_task2();
                return true;
            }
            icon_file.classList.remove("bx-package");
            icon_file.classList.add("bx-tada");
            filetext.innerHTML = "Загрузите файл";
            flag_fileinput = false;
        
            
        });
        
        
        
        if(document.querySelector(".time_settings").textContent === "--:--:--"){
            ;
        }
        else{
            const seconds = document.querySelector(".seconds .number");
            const minutes = document.querySelector(".minutes .number");
            const hours = document.querySelector(".hours .number");
        
            let secValue = Number(document.querySelector(".seconds .number").textContent),
            minValue = Number(document.querySelector(".minutes .number").textContent),
            hourValue = Number(document.querySelector(".hours .number").textContent)
        
            const timeFunctin = setInterval(() => {
                if (secValue == 0 && minValue == 0 && hourValue == 0){
                    alert("Соревнование закончилось, перезагрузите страницу!");
                    location.reload();
                }
                if (secValue != 0){
                    secValue--;
                }
                else if (secValue == 0 && minValue != 0) {
                    minValue--;
                    secValue = 59;
                }
                else if (secValue == 0 && minValue == 0 && hourValue != 0) {
                    hourValue--;
                    minValue = 59;
                    secValue = 59;
                }
                else if (minValue == 0 && hourValue != 0) {
                    hourValue--;
                    minValue = 59;
                }
                // if (hourValue != 0 || minValue != 0 || secValue != 0){
                //     secValue--;
                // }
                // if(hourValue == 0 && minValue == 0 && secValue == 0){
                //     location.reload();
                // }
                // if (secValue == 0) {
                //     minValue--;
                //     secValue = 59;
                // }
                // if (minValue == 0 && hourValue != 0){
                //     hourValue--;
                //     minValue = 59;
                // }
                seconds.textContent = secValue < 10 ? `0${secValue}` : secValue;
                minutes.textContent = minValue < 10 ? `0${minValue}` : minValue;
                hours.textContent = hourValue < 10 ? `0${hourValue}` : hourValue;
            }, 1000);
        }
        
        // const timeFunctin = setInterval(() => {
        //     const seconds_text = document.querySelector(".seconds .number").textContent;
        //     const minutes_text = document.querySelector(".minutes .number").textContent;
        //     const hours_text = document.querySelector(".hours .number").textContent;
        
        //     const seconds = document.querySelector(".seconds .number");
        //     const minutes = document.querySelector(".minutes .number");
        //     const hours = document.querySelector(".hours .number");
        
        //     seconds.textContent = seconds_text < 10 ? '0${seconds_text}' : seconds_text;
        //     minutes.textContent = minutes_text < 10 ? '0${minutes_text}' : minutes_text;
        //     hours.textContent = hours_text < 10 ? '0${hours_text}' : hours_text;
        //     console.log(seconds_text, minutes_text, hours_text, seconds, minutes, hours)
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
        var selectedOptionAttribyte;
        options.forEach(option =>{
            option.addEventListener("click", ()=>{
                let selectedOption = option.querySelector(".option-text").innerText;
                sBtn_text.innerText = selectedOption;
                let selectedOptionAttribyteQuerySelector = option.querySelector(".option-text");
                let selectedOptionAttribyte = selectedOptionAttribyteQuerySelector.dataset.type;
                fileinput.setAttribute("accept", selectedOptionAttribyte);
        
                const stn_text = document.querySelector(".sBtn-text");
                if(flag_fileinput){
                    stn_text.classList.remove("blocked_text2");
                }
                if(flag_textinput){
                    stn_text.classList.remove("blocked_text1");
                }
                blocked_button_task1();
                blocked_button_task2();
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
        const contents = document.querySelectorAll(".content_hidden");
         
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
        
        
        const notification_task = document.querySelectorAll(".notification_task");
        const close_notification_task = document.querySelectorAll(".close-notification_task");
        
        for (let i = 0; i < close_notification_task.length; i++){
            close_notification_task[i].addEventListener("click", (e) => {
                for(let j = 20; j > -350; j--){
                    setTimeout(() => notification_task[i].style.right = `${j}px`, 30);
                }
                
        
                const parent = notification_task[i].parentNode;
                setTimeout(() => parent.removeChild(notification_task[i]), 1000);
                
            })
        }
        
  
  
    //   const wrapper = document.querySelector(".flex-content-d");
    //   const dsa = ``;
    //   wrapper.prepend(dsa);
    //   dsa.innerHTML = `<div class="block-content"><span><p class="time">вфывфыв</p><p class="tasktime">фвыфывфывфы</p>-<p class="test">фвфвфывфы</p></span></div>`
    
        $('#textarea_form').submit((e) => {
            e.preventDefault(); 
            const formData = new FormData(); 

            const downloadToFile = (content, filename, contentType) => {
                const file = new Blob([content], {type: contentType});
                let inputForm = document.getElementById('textarea-input');
                const file_upload = new File([file], filename)
               
        
                const dT = new ClipboardEvent('').clipboardData || new DataTransfer();
                dT.items.add(file_upload);
                inputForm.files = dT.files;
                formData.append('file', inputForm.files[0]);
        
            };
            const textArea = document.querySelector('.textarea_textupload');
            downloadToFile(textArea.value, `file${$('#upload').prop('accept')}`, `text/plain`);
            

            $('.notification_send').addClass('succefuly');
            setTimeout(() => {
                $('.notification_send').removeClass('succefuly');
            }, 2000);

            $('#textarea').val('');
            flag_textinput = false;
            $('.button-task1').addClass('blocked_text2');
            $('.button-task1').prop("disabled", true);

            $.ajax({
                type: 'POST',
                url: '',
                dataType: 'json',
                
                headers: {
                    'X-CSRFToken': $('meta[name="csrf-token"]').attr('content')
                },
                contentType: false,
                data: formData,
                success: function(response) {
                    
                },
                error: function(response) {
                
                console.log('Error:', response);
                }
            });
        });

        $('#file_form').submit(function(e) {
            e.preventDefault(); 

            const fileInput = $('#upload')[0];
            const formData = new FormData();
            formData.append('file', fileInput.files[0]);

            $('.notification_send').addClass('succefuly');
            setTimeout(() => {
                $('.notification_send').removeClass('succefuly');
            }, 2000);

            $('.bxl-dropbox').removeClass("bx-package");
            $('.bxl-dropbox').addClass("bx-tada");
            filetext.innerHTML = "Загрузите файл";
            flag_fileinput = false;
            $('#upload').val('');
            $('.button-task2').addClass('blocked_text2');
            $('.button-task2').prop("disabled", true);

            

            $.ajax({
            type: 'POST',
            url: '',
            dataType: 'json',
            
            headers: {
                'X-CSRFToken': $('meta[name="csrf-token"]').attr('content')
            },
            data: formData,
            success: function(response) {
                const wrapper = document.querySelector(".flex-content-d");
                wrapper.innerHTML += `<div class="block-content">
                    <span><p class="time">${response.time}</p><p class="tasktime">${response.link_task.title}</p>-<p class="test">${response.error}</p></span>
                    </div>`;
                
                // let div = wrapper.createElement('div');
                // div.className = "block-content";
                // div.innerHTML = `<span><p class="time">${response.time}</p><p class="tasktime">${response.link_task.title}</p>-<p class="test">${response.error}</p></span>`
                // console.log(response.attempt); // do something with response data
            },
            error: function(response) {
            
            console.log('Error:', response);
            }
      });
      });
      }
      else if(url.includes('you') || url.includes('user')){
        console.log(document.getElementById('username_name').textContent)
        
        if(url.includes('you') || (url.includes(document.getElementById('username_name').textContent)) ){
            const upload_photo = document.querySelector(".input_upload_"),
        save_photo = document.querySelector(".input_upload_save"),
        input_upload_photo = document.querySelector(".upload-photo-file")
        console.log(upload_photo, save_photo, input_upload_photo)

        input_upload_photo.addEventListener('change', function(){
        if( this.value ){
            save_photo.classList.remove("save_photo");
        } else { 
            
        }
        
        });

        let popupBg2 = document.querySelector('.pbg2');
        let popup2 = document.querySelector('.p2');
        let openPopupButtons2 = document.querySelector('.op2');
        let closePopupButton2 = document.querySelector('.cp2'); 


        openPopupButtons2.addEventListener('click', (e) => { 
            e.preventDefault(); 
            popupBg2.classList.add('active'); 
            popup2.classList.add('active'); 
        });

        closePopupButton2.addEventListener('click',() => { 
            popupBg2.classList.remove('active');
            popup2.classList.remove('active'); 
        });

        document.addEventListener('click', (e) => { 
            if(e.target === popupBg2) { 
                popupBg2.classList.remove('active'); 
                popup2.classList.remove('active'); 
            }
        });
        
        var cropper;

        $('#h').on('change', (event) => {
        var input = event.target;
        var reader = new FileReader();
        
        reader.onload = function() {
            var dataURL = reader.result;
            var image = document.getElementById('image-preview');
            image.src = dataURL;
            if (cropper) {
            cropper.destroy();
            console.log(1)
            }
            cropper = new Cropper(image, {
            aspectRatio: 1, // указываем соотношение сторон области обрезки (1:1)
            viewMode: 1, // фиксированное положение области обрезки
            crop: function(event) {
                // Здесь вы можете писать код, который реагирует на изменение выбранной области обрезки
            }
            });
        }
        
        reader.readAsDataURL(input.files[0]);
        });


        
        
        
        $('#o').submit(function(e) {
            e.preventDefault();

            var canvas = cropper.getCroppedCanvas();
            var croppedImageDataURL = canvas.toDataURL('image/jpeg');
            var image = document.getElementById('img_settings');
            console.log(image)
            image.src = croppedImageDataURL;
            
            
            
            document.getElementById('image_src').src = croppedImageDataURL;



            async function setFile(input, name, url) {
                try {
                    var blob = await (await fetch(url)).blob();
                    var dt  = new DataTransfer();
                    dt.items.add(new File([blob], name, {type: blob.type}));
                    input.files = dt.files;
                    console.log('Файл успешно вставлен:');
                    console.log(input.files);
                    const formData = new FormData(); 
                    formData.append('file', input_element.files[0]);
                    // Здесь вы можете отправить обрезанное изображение на сервер или выполнить другие операции с данными
                    console.log(input_element.files[0])
                    return formData
                }
                catch(err) {
                    console.log('Ошибка при вставке файла:');
                    console.dir(err);
                }
            }

            // Входные параметры:
            var input_element = document.getElementById('image_src');
            var file_name = 'image.jpg';
            var file_link = croppedImageDataURL;

            // Вызовем функцию для вставки файла:
            

            
                $.ajax({
                    

                    data: setFile(input_element, file_name, file_link),
                    contentType: false,
                    processData: false,
                    
                    success: function(e){
                        console.log(2)
                    },
                    error: function(e){
                        console.log(3)
                    },
                    
                })
            
        });
        }
        else {
            $('.block_avatar').css('height', '250px');
        }

        const ctx = document.getElementById('myChart');

        var arrayOfLabels = $('meta[name="labels"]').attr('content').split(",");
        var arrayOfData = $('meta[name="data"]').attr('content').split(",");
        
        arrayOfLabels.pop();
        arrayOfData.pop();
        
        var chart = new Chart(ctx, {
          type: 'line',
        
          data: {
            labels: arrayOfLabels,
            datasets: [{
                label: '',
                data: arrayOfData,
                fill: false,
                borderColor: '#4651E5',
                backgroundColor: '#4651E5',
                tension: 0.01,
                pointBackgroundColor: '#4651E5',
                pointBorderColor: '#4651E5',
                order: 1,
                spanGaps: false,
                drawActiveElementsOnTop: false,
            }]
          },
          options: {
            responsive: true,
            plugins: {
              legend: {
                position: 'bottom',
              },
              title: {
                display: true,
                text: 'Chart.js Line Chart'
              }
            }
          },
        });
      }
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

          contentDiv.classList.remove('fade-out');
          if(url.includes('you')){
            history.pushState({}, '', `/user/${document.getElementById('username_name').textContent}/`);
          }
          else{history.pushState({}, '', url);}

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