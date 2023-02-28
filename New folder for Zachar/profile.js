const upload_photo = document.querySelector(".input_upload_"),
save_photo = document.querySelector(".input_upload_save"),
input_upload_photo = document.querySelector(".upload-photo-file")

input_upload_photo.addEventListener('change', function(){
  if( this.value ){
    save_photo.classList.remove("save_photo");
    upload_photo.classList.add("change_photo")
  } else { 
  }
});



const ctx = document.getElementById('myChart');

var chart = new Chart(ctx, {
  type: 'line',

  data: {
    labels: ['18 февраля', '12 июля', '31 августа', '23 сентебря', '10 ноября', '23 декабря', '1 января'],
    datasets: [{
        label: '',
        data: [103, 154, 342, 179, 503, 647, 1000],
        fill: false,
        borderColor: '#91BFBC',
        backgroundColor: '#91BFBC',
        tension: 0.01,
        pointBackgroundColor: '#91BFBC',
        pointBorderColor: '#91BFBC',
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





let popupBg = document.querySelector('.popup__bg');
let popup = document.querySelector('.popup');
let openPopupButtons = document.querySelector('.open-popup');
let closePopupButton = document.querySelector('.close-popup'); 


openPopupButtons.addEventListener('click', (e) => { 
    e.preventDefault(); 
    popupBg.classList.add('active'); 
    popup.classList.add('active'); 
});

closePopupButton.addEventListener('click',() => { 
    popupBg.classList.remove('active');
    popup.classList.remove('active'); 
});

document.addEventListener('click', (e) => { 
    if(e.target === popupBg) { 
        popupBg.classList.remove('active'); 
        popup.classList.remove('active'); 
    }
});