const form = document.querySelector('form');
const nameInput = document.querySelector('#form-name');
const textInput = document.querySelector('#form-text');
const ratingInput = document.querySelector('#form-rating');
const publishButton = document.querySelector('#leave-a-comment__button');
const usersComments = document.querySelector('.users-comments');
const fields = document.querySelectorAll('.field')

// Validation
// publishButton.addEventListener('click', function (event) {
//     event.preventDefault();
//         for (i = 0; i < fields.length; i++) {
//             if (!fields.value) {
//                 fields[i].style.border = '1px solid red';
//             } else {
//                 fields[i].style.border = '';
//                 publish();
//             }
//         }
//     })

// Add a comment
publishButton.addEventListener('click', function () {
    const createDiv = document.createElement('div');
    createDiv.classList.add('users-comments__item');
    const createPName = document.createElement('p');
    const createRating = document.createElement('p');
    const createDate = document.createElement('p');
    createDate.classList.add('comment-date');
    const createPText = document.createElement('p');
    for (i = 0; i < rating.length; i++) {
        let dateToday = new Date();
        let splitDate = dateToday.toLocaleString().split(',')
        createDate.textContent = dateText[i].textContent = splitDate[0];
    }
    createPName.textContent = nameInput.value;
    if (createPName.textContent === '') {
        createPName.textContent = 'Имя Фамилия';
    };
    createPText.textContent = textInput.value;
    createRating.textContent = `Оценка: ${ratingInput.value}/10`;
    usersComments.append(createDiv);
    createDiv.append(createPName);
    createDiv.append(createRating);
    createDiv.append(createDate);
    createDiv.append(createPText);
    nameInput.value = '';
    textInput.value = '';
    ratingInput.value = '';

    publishButton.textContent = 'Опубликовано!';
    publishButton.style.border = '2px solid #08B251';
    publishButton.setAttribute('disabled', '');
    publishButton.style.backgroundColor = 'green';
    setTimeout(()=>{
        publishButton.style.backgroundColor = 'transparent';
    }, 1000)
});