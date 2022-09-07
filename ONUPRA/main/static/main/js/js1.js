// crftoken = form.querySelector("input[type=hidden]").value
// console.log(username, crftoken)
async function request(username, csrftoken) {
    const formData = new FormData();
    console.log(username, csrftoken)

    const response = await fetch('/signup/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({'csrfmiddlewaretoken':[csrftoken], 'username':[username]}),
    })
    console.log(JSON.stringify({'csrfmiddlewaretoken':[csrftoken], 'username':[username]}))
    // const result = await response.text()
    // return result
}
async function check_username() {
    const form = document.querySelector("form"),
    username = form.querySelector(".test").value
    const csrftoken = form.querySelector("input[type=hidden]").value
    const csrftoken2 = {'csrfmiddlewaretoken': form.querySelector("input[type=hidden]").value }
    // var xhr = new XMLHttpRequest()
    // console.log(csrftoken)
    // var body = 'csrfmiddlewaretoken=' + csrftoken + "username" + username;
    // xhr.open("POST", '/signup/', body);
    // xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    // xhr.send();
    // const result = await request(username, csrftoken)
} // check_username()

function sendRequest(method, url, body, csrftoken) {
    return new Promise((resolve, reject) =>{
        const xhr = new XMLHttpRequest()

        xhr.open(method, url)
        xhr.responseType = 'json'
        xhr.setRequestHeader('Content-Type', form.querySelector("input[type=hidden]").value),
        xhr.setRequestHeader("Content-Type", "application/json; charset=utf-8")
        xhr.onload = () => {
            if (xhr.status >= 200){
                reject(xhr.response)
            } else {
                resolve(xhr.response)
            }
        }
        xhr.onerror = () => {
            reject(xhr.response)
        }

        xhr.send(JSON.stringify(body))
    })
}
const form = document.querySelector("form")
const csrftoken = form.querySelector("input[type=hidden]").value
const x = form.querySelector("input[type=hidden]").value
const body = {
    'csrfmiddlewaretoken': [x], 
    'username': [form.querySelector(".test").value],
    'checker': ['']
}

sendRequest('POST', '/signup/', body, csrftoken)