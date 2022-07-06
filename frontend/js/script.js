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
                    comps => {
                        let title = '';
                        description = '';
                        cards = `<h2 class='cards__title'>Актуальные номинации</h2>`;
                        for (let i = 0; i < data.length; i++) {
                            for (let j = 0; j < comps.length; j++) {
                                if (data[i]['nomination_id']==comps[j]['id']) {
                                    title = comps[j]['title'];
                                    description = comps[j]['description'];
                                }
                            }
                            console.log(comps);
                            console.log(data);
                            // if(comps[i]['year']<=) сделать чтобы прошедшие номинации отображались не тут
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
                        document.querySelectorAll('.cards')[0].innerHTML = cards;
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



function get_nomination(nomination_id) {

}