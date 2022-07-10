const api_ip = "https://justcors.com/tl_4958980/http://django-nominations.std-1867.ist.mospolytech.ru/api/"
//const api_ip = "http://127.0.0.1:8000/api/"
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
        return response.json();
    }
    )
    .then (
        data => {
            fetch(api_ip+"nominations/", { method:'GET'})
            .then(
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
                            <div class='card'  id='c${data[i]['id']}'>
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
                    document.querySelectorAll('.card').forEach(element => {
                        element.addEventListener('click', event =>{
                            if (event.currentTarget.id[0]=="c"){
                                console.log(event.currentTarget);
                                window.location.href = 'nomination.html?id='+event.currentTarget.id.slice(1);
                            }
                        })
                    });
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
                                <div class='card' id='c${data[i]['id']}'>
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
                        document.querySelectorAll('.card').forEach(element => {
                            element.addEventListener('click', event =>{
                                console.log(event.currentTarget);
                                window.location.href = 'nomination.html?id='+event.currentTarget.id.slice(1);
                            })
                        })
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


function get_winners() {
    fetch(api_ip+"winners/winners/", { method:'GET'})
    .then( response => {
        return response.json();
    })
    .then( data => {
        Object.keys(data).forEach( key => {
            winner = data[key];
            console.log(winner);
            let winner_card =
            `
            <div class='card' id="p${key}">
                <img class='card__img' src="${api_ip.replace("api/", "")+"media/"+winner['photo']}" alt="profile picture">
                <div class='card__textfield'>
                    <h3 class='card__nickname'>${winner['first_name']} ${winner['last_name']}</h3>
                </div>
                <div class='card__textfield'>
                    <p class='card__nomination'>${winner['nomination_title']} (${winner['year']})</p>
                </div>
            </div>`;
            document.getElementById('last_winners').insertAdjacentHTML('beforeend', winner_card);
            document.getElementById("p"+key).addEventListener('click', (e) => {
                window.location.href = 'profile.html?id='+event.currentTarget.id.slice(1);
            })
        })

    })
}


function login_page_load() {
    let login_form = document.getElementById('submit');
    let mail_input = document.getElementById('email');
    let password_input = document.getElementById('password');
    login_form.addEventListener('click', (e)=>{
        e.preventDefault();
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
                    window.location.href = 'profile.html';
                }
            }
        )
        .catch (
            error => {console.log('грусть')}
        )
    })
}


function register_page_load() {
    const form_data = new FormData();

    let register = document.getElementById('submit');
    let mail = document.getElementById('email');
    let first_name = document.getElementById('first_name');
    let last_name = document.getElementById('last_name');
    let password = document.getElementById('password');
    let image = document.getElementById('profile_image')
    let description = document.getElementById('description')


    register.addEventListener('click', (e)=>{
        form_data.append('photo', image.files[0]);
        form_data.append('password', password.value);
        form_data.append('first_name', first_name.value);
        form_data.append('last_name', last_name);
        form_data.append('email', mail.value);
        form_data.append('description', description.value);
        e.preventDefault();
        fetch(api_ip + "auth/register/", {
                headers: {
                    'Accept': 'application/json',
                },
                method:'POST',
                body: form_data
            }
        )
        .then(
            response => {
                console.log(response)
                return response.json();
            }
        )
        .then (
            data => {
                console.log(data);
                if(data['message']=='success'){ 
                    window.location.href = "login.html"
                }
                else {
                    document.querySelector('.form').insertAdjacentHTML('beforebegin', invalid_data_field)
                }
            }
        )
        .catch (
            error => {console.log('грусть')}
        )
    })
}


function check_login() {
    if (get_cookie('token')!=null) {
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

function check_footer(){
    document.body.insertAdjacentHTML('beforeend', `<footer class='footer' w3-include-html='templates/footer.html'></footer>`);
}

function logout(){
    setCookie('token', '', {'max-age': -1});
    window.location.href = 'login.html';
}


function get_nomination(){
    const id = new URL(window.location.href).searchParams.get('id');
    fetch(api_ip + "competition/"+id+"/")
    .then(
        response => {
            return response.json();
        }
    )
    .then( data=> {
        fetch(api_ip+"nominations/"+data['nomination_id']+"/", { method:'GET'})
        .then(
            response => {
                return response.json();
            }
        )
        .then (        
            nomination => {
                let title = nomination['title'];
                let description = nomination['description'];
                let cover = data['cover'];

                document.getElementById('nomination').innerHTML = 
                 `
                 <h2 class='nomination__title'>Номинация: ${title}</h2>
                 <div class="nomination__interactions">
                     <img class='nomination__img' src="${cover}" alt="nomination picture">
                     <input class='nomination__button button--green' type="button" value='Участвовать'>
                 </div>
                 <div class="nomination__info">
                     <p class="nomination__info-title">О номинации:</p>
                     <p class="nomination__info-text">${description}</p>
                     <p class="nomination__info-title">Победитель: <a href="">Шарлота Заморская</a></p>
                 </div>`
                console.log(nomination)
                console.log(data)
            }
        )
        .catch(
            error => {
                console.log(error.statusText);
            }
        )
    })

}



function get_profile() {
    const id = new URL(window.location.href).searchParams.get('id');
    let request_ip = "";
    let me = false;
    if (id!=null){
        request_ip = api_ip + "auth/" + id +"/";
    }
    else {
        if (check_login()) {
            request_ip = api_ip + "auth/me/";
            me = true;
        }
        else {
            console.log("Вы не авторизированы")
        }
    }
    fetch(request_ip, {'credentials':'include'})
    .then(
        response => {
            return response.json();
        }
    )
    .then( data => {
        let head = `<h2 class='profile__title'>Профиль: ${data['first_name']} ${data['last_name']}</h2>`
        if (me) {
            head = `<h2 class='profile__title'>Мой профиль</h2>`
        }
        console.log(data);
        console.log(document.getElementById("profile"));
        // <a class='profile__interactive-link' href="">Хочу стать организатором</a>
        document.getElementById("profile").innerHTML = `
        ${head}
        <div class="profile__interactions">
            <img class='profile__img' src="${data['photo']}" alt="profile picture">
        </div>
        <div class="profile__info">
            <p class="profile__info-title">ФИО: ${data['first_name']} ${data['last_name']}</p>
            <p class="profile__info-title">Почта: <a href="mailto:${data['email']}">${data['email']}</a></p>
            <p class="profile__info-title">Обо мне:</p>
            <p class="profile__info-text">${data['description']}</p>
        </div>`
    })
}
