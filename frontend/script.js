let api_ip = "http://127.0.0.1:8000/api/auth/"


fetch(api_ip).then(
    response => {
        document.body.insertAdjacentHTML(response.json())
        return response.json()
    }
)
.catch(
    error => {
        console.log(error.statusText)
    }
)

