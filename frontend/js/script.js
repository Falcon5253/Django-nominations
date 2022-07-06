let api_ip = "http://django-nominations.std-1867.ist.mospolytech.ru/api/"
const awaitTimeout = delay => new Promise(resolve => setTimeout(resolve, delay));

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