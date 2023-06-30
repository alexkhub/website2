const searchInput = document.querySelector('#header-search');
const searchIcon = document.querySelector('.search-icon');
const searchIconText = document.querySelector('.search-icon i')

// Search animation

searchInput.addEventListener('focus', function() {
    searchIcon.classList.toggle('search-icon-left');
    searchIconText.style.border = 'none';
    searchInput.style.paddingLeft = 15 + 'px';
});

searchInput.addEventListener('blur', function() {
    searchIcon.classList.toggle('search-icon-left');
    searchIconText.style.border = '1px solid white';
    searchInput.style.paddingLeft = 45 + 'px';
});