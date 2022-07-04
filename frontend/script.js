let api_ip = "http://127.0.0.1:8000/api/auth/"


fetch(api_ip, { method:'GET'}).then(
    response => {
        document.body.insertAdjacentHTML('beforeend', response);
        console.log(response.json())
    }
)
.catch(
    error => {
        console.log(error.statusText);
    }
)

