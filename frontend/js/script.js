// const api_ip = "http://django-nominations.std-1867.ist.mospolytech.ru/api/"
const api_ip = "http://127.0.0.1:8000/api/"
const invalid_data_field =`<div id='error' class='error'><h2 class='error__title'>Неверные данные, попробуйте еще раз</h2></div>`
const awaitTimeout = delay => new Promise(resolve => setTimeout(resolve, delay));




function get_cookie(name) {
    var match = document.cookie.match(new RegExp('(^| )' + name + '=([^;]+)'));
    if (match) return match[2];
    else {return null}
}

function setCookie(name, value, options = {}) {

    options = {
      path: '/',
      // при необходимости добавьте другие значения по умолчанию
      ...options
    };
  
    if (options.expires instanceof Date) {
      options.expires = options.expires.toUTCString();
    }
  
    let updatedCookie = encodeURIComponent(name) + "=" + encodeURIComponent(value);
  
    for (let optionKey in options) {
      updatedCookie += "; " + optionKey;
      let optionValue = options[optionKey];
      if (optionValue !== true) {
        updatedCookie += "=" + optionValue;
      }
    }
  
    document.cookie = updatedCookie;
}

async function showMenu (){
    document.querySelector('.header__list').style.animation = 'open-menu 0.5s forwards';
    document.querySelector('.header__close-burger-button').style.display = 'block';
    document.querySelector('.header__close-burger-button').style.animation = 'appear 0.5s forwards';
    await awaitTimeout(500).then( () => document.querySelector('.header__close-burger-button').style.display = 'block')
}
async function hideMenu() {
    document.querySelector('.header__list').style.animation = 'close-menu 0.5s forwards';
    document.querySelector('.header__close-burger-button').style.animation = 'disappear 0.5s forwards';
    await awaitTimeout(500).then( () => document.querySelector('.header__close-burger-button').style.display = 'none')
}
window.addEventListener("resize", function() {
    if (window.innerWidth < 1450){
        hideMenu();
    }
});


function get_new_competitions() {
    fetch(api_ip+"competition/", { method:'GET'}).then(
    response => {
        // document.body.insertAdjacentHTML('beforeend', response.json());
        return response.json();
    }
    )
    .then (
        data => {
            let nominations = fetch(api_ip+"nominations/", { method:'GET'}).then(
                response => {
                    // document.body.insertAdjacentHTML('beforeend', response.json());
                    return response.json();
                }
                )
                .then (        
                    nominations => {
                        let title = '';
                        description = '';
                        cards = `<h2 class='cards__title'>Актуальные номинации</h2>`;
                        for (let i = 0; i < data.length; i++) {
                            for (let j = 0; j < nominations.length; j++) {
                                if (data[i]['nomination_id'] == nominations[j]['id']) {
                                    title = nominations[j]['title'];
                                    description = nominations[j]['description'];
                                }
                            }
                            let comp_date = new Date(data[i]['year'])
                            let today_date = new Date()
                            title += ' (' + ('0'+comp_date.getDate()).slice(-2) + '.' + ('0'+(comp_date.getMonth()+1)).slice(-2) + '.' + comp_date.getFullYear() + ')';
                            if(comp_date > today_date){
                                cards += `
                                <div class='card'>
                                    <img class='card__img' src="${data[i]['cover']}" alt="nomination picture">
                                    <div class='card__textfield'>
                                        <h3 class='card__nomination'>${title}</h3>
                                    </div>
                                    <div class='card__textfield'>
                                        <p class='card__nomination-description'>${description}</p>
                                    </div>
                                </div>`
                            }
                        }
                        document.querySelector('#current_nominations').innerHTML = cards;
                    }
                )
                .catch(
                    error => {
                        console.log(error.statusText);
                    }
                )
        }
    )
    .catch(
        error => {
            console.log(error.statusText);
        }
    )
}


function get_old_competitions() {
    fetch(api_ip + "competition/", { method:'GET'}).then(
        response => {
            return response.json();
        }
    )
    .then (
        data => {
            let nominations = fetch(api_ip+"nominations/", { method:'GET'}).then(
                response => {
                    return response.json();
                }
                )
                .then (        
                    nominations => {
                        let title = '';
                        description = '';
                        cards = `<h2 class='cards__title'>Прошедшие номинации</h2>`;
                        for (let i = 0; i < data.length; i++) {
                            for (let j = 0; j < nominations.length; j++) {
                                if (data[i]['nomination_id']==nominations[j]['id']) {
                                    title = nominations[j]['title'];
                                    description = nominations[j]['description'];
                                }
                            }
                            let comp_date = new Date(data[i]['year']);
                            let comp_date_string = new Date(data[i]['year'])
                            let today_date = new Date();
                            title += ' (' + ('0'+comp_date.getDate()).slice(-2) + '.' + ('0'+(comp_date.getMonth()+1)).slice(-2) + '.' + comp_date.getFullYear() + ')';
                            if(comp_date <= today_date){
                                cards += `
                                <div class='card'>
                                    <img class='card__img' src="${data[i]['cover']}" alt="nomination picture">
                                    <div class='card__textfield'>
                                        <h3 class='card__nomination'>${title}</h3>
                                    </div>
                                    <div class='card__textfield'>
                                        <p class='card__nomination-description'>${description}</p>
                                    </div>
                                </div>`
                            }
                        }
                        document.querySelector('#previous_nominations').innerHTML = cards;
                    }
                )
                .catch(
                    error => {
                        console.log(error.statusText);
                    }
                )
        }
    )
    .catch(
        error => {
            console.log(error.statusText);
        }
    )
}

function login_page_load() {
    const login_form = document.getElementById('submit');
    const mail_input = document.getElementById('email');
    const password_input = document.getElementById('password');
    login_form.addEventListener('click', (e)=>{
        // 
        fetch(api_ip + "auth/login/", {
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                method:'POST',
                body: JSON.stringify({'email': mail_input.value, 'password': password_input.value})
            }
        )
        .then(
            response => {
                return response.json();
            }
        )
        .then (
            data => {
                if(data.hasOwnProperty('error')){
                    if (!document.getElementById('error')){
                        document.querySelector('.form').insertAdjacentHTML('beforebegin', invalid_data_field)
                    }
                }
                else {
                    setCookie('token', data['success'], {'max-age': 7200})
                    // document.cookie = "token="+data['success'];
                    window.location.href = 'profile.html';
                }
            }
        )
        .catch (
            error => {console.log('грусть')}
        )
    })
    // login_form.setAttribute('action', api_ip + '/auth/login');

}


function check_login() {
    if (get_cookie('token')!=null) {
        console.log(get_cookie('token'));
        return true;
    }
    else {
        return false;
    }
}

function check_header(){
    if (check_login()) {
        document.body.insertAdjacentHTML('afterbegin', `<header class='header' w3-include-html='templates/profile-header.html'></header>`);
    }
    else {
        document.body.insertAdjacentHTML('afterbegin', `<header class='header' w3-include-html='templates/login-header.html'></header>`);
    }

}

function logout(){
    setCookie('token', '', {'max-age': -1});
    window.location.href = 'login.html';
}