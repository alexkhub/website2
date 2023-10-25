const profileSettingsButton = document.querySelector('.fa-cogs');
const profileSettingsContainer = document.querySelector('.profile-settings__container');
const profileSettings = document.querySelector('.profile-settings');
const closeButtons = document.querySelectorAll('#confirm, .fa-times');
const body = document.querySelector('body');

profileSettingsButton.addEventListener('click', () => {
    profileSettingsContainer.style.display = 'block';
    setTimeout(() => {
        profileSettings.style.opacity = 100;
    }, 0);
    body.style.overflowY = 'hidden';
});

closeButtons.forEach(el => {
    el.addEventListener('click', () => {
        profileSettings.style.opacity = 0;
        setTimeout(() => {
            profileSettingsContainer.style.display = 'none';
        }, 300);
        body.style.overflowY = 'scroll';

        confirmEmail.value = '';
        email.value = '';
        confirmPassword.value = '';
        password.value = '';
    })
})

// Email validation
const email = document.querySelector('#email__input');
const confirmEmail = document.querySelector('#confirm-email__input');

confirmEmail.addEventListener('input', () => {
    if (confirmEmail.value !== email.value) {
        confirmEmail.style.borderBottom = '2px solid red';
    } else {
        confirmEmail.style.borderBottom = '2px solid green';
    }
})

email.addEventListener('input', () => {
    if (confirmEmail.value !== email.value) {
        confirmEmail.style.borderBottom = '2px solid red';
    } else {
        confirmEmail.style.borderBottom = '2px solid green';
    }
})

// Password validation
const password = document.querySelector('#password__input');
const confirmPassword = document.querySelector('#confirm-password__input');

confirmPassword.addEventListener('input', () => {
    if (confirmPassword.value !== password.value) {
        confirmPassword.style.borderBottom = '2px solid red';
    } else {
        confirmPassword.style.borderBottom = '2px solid green';
    }
})

password.addEventListener('input', () => {
    if (confirmPassword.value !== password.value) {
        confirmPassword.style.borderBottom = '2px solid red';
    } else {
        confirmPassword.style.borderBottom = '2px solid green';
    }
})
