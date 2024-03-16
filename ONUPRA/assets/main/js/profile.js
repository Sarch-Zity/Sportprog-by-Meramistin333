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

var tx = document.getElementsByTagName('textarea');

for (var i = 0; i < tx.length; i++) {
    console.log(tx[i].scrollHeight)
    tx[i].setAttribute('style', 'height:' + (tx[i].scrollHeight) + 'px;overflow-y:hidden;');
    tx[i].addEventListener("input", OnInput, false);
  }


function OnInput() {
  if(this.scrollHeight > 100){
  this.style.height = 'auto';
  this.style.height = (this.scrollHeight) + 'px';}
}

const file_clip = document.querySelector(".file_clip"),
file_container = document.querySelector(".file-container");

file_clip.addEventListener("change", (e) => {
  console.log(file_clip.value)
  const value_file_clip = file_clip.value
  const startIndex = (value_file_clip.indexOf('\\') >= 0 ? value_file_clip.lastIndexOf('\\') : value_file_clip.lastIndexOf('/'));
  const filename = value_file_clip.substring(startIndex);
  console.log(file_clip.files)
  file_container.innerHTML += 
  `
  <label class="file_container_elem">
      <i class='bx bx-file'></i>
      <span>${filename}</span>
      <i class='bx bx-x x_delete'></i>

      <input class="hidden_input" type="file" disabled>
  </label>
  `;
});
document.addEventListener("change", () => {
  const x_deletes = document.querySelectorAll(".x_delete");
  x_deletes.forEach((x_delete) => {
    x_delete.addEventListener("click", () => {
      const content = x_delete.parentElement;
      
      content.remove(content);
    })
  })
})

function validateTextarea() {
    const result = document.querySelector(".result")
    const txarea = document.getElementsByTagName('textarea');
    const limit = 2007
    console.log(txarea)
    result.textContent = 0 + '/' + limit

    txarea[0].addEventListener("input", () => {
      const textLength = txarea[0].value.length
      result.textContent = textLength + '/' + limit

      if(textLength > limit){
        result.style.color = '#ff2851'
      } else if (textLength > 1200) {
        result.style.display = 'block'
      } else {
        result.style.display = 'none'
      }
    })

}
validateTextarea()