var tryout = new XMLHttpRequest();  

const form = document.querySelector("form")  

tryout.open('POST', '/signup/', false);
tryout.setRequestHeader('x-csrf-token', form.querySelector("input[type=hidden]").value);       
tryout.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
tryout.setRequestHeader("Accept", "application/json");
const body = {
'csrfmiddlewaretoken': form.querySelector("input[type=hidden]").value, 
'username': form.querySelector(".test").value, 
'checker': ''
}
tryout.send(JSON.stringify(body));

// function sendRequest(method, url, body) {
//     const form = document.querySelector("form")
//     const headers = {
//         'x-csrf-token': form.querySelector("input[type=hidden]").value,
//         "Content-Type": "application/json; charset=utf-8",
//         "Accept": "application/json"
//     }
//     return fetch(url, {
//         method: method,
//         body: JSON.stringify(body),
//         headers: headers
//     }).then(response => {
//         return response.json()
//     })
// }

// const form = document.querySelector("form")
// const body = {
// 'csrfmiddlewaretoken': form.querySelector("input[type=hidden]").value, 
// 'username': form.querySelector(".test").value,
// 'checker': ''
// }

// sendRequest('POST', '/signup/', body)


// $(function(){
//     $('a').click(function(){
//         $.ajax({
//             url: '/signup/',
//             type: "POST",
//             data: 'uesrname=gleb',
//             success: success,
//             dataType: dataType
//           }),
//       viewResult
//     });
  
//     function viewResult(data) {
//       alert(data)
//     }
//   });