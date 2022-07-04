let api_ip = "http://127.0.0.1:8000/api/auth/"


fetch(api_ip, { method:'GET'}).then(
    response => {
        // document.body.insertAdjacentHTML('beforeend', response.json());
        return response.json()
    }
)
.then (
    
    data => {
        for (let i =0; i < data.length; i++){
            console.log(data[i]);  
            document.body.insertAdjacentHTML('beforeend', '<h2>'+data[i]['email']+'</h2');
            document.body.insertAdjacentHTML('beforeend', '<p>'+data[i]['first_name']+'</p');
            document.body.insertAdjacentHTML('beforeend', '<p></p>');
        }
    }
)
.catch(
    error => {
        console.log(error.statusText);
    }
)

