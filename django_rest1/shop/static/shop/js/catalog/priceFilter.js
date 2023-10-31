const minPriceSlider = document.querySelector('#price-min__input');
const minPriceText = document.querySelector('#price-range-min');
const maxPriceSlider = document.querySelector('#price-max__input');
const maxPriceText = document.querySelector('#price-range-max');
const itemPrice = document.querySelectorAll('.item p:nth-of-type(2)');

// Set input max value
let maxPrices = [];
itemPrice.forEach(el => {
    maxPrices.push(el.textContent.split('рублей')[0] / 1);
});
const getMaxPrice = Math.max(...maxPrices);
minPriceSlider.setAttribute('max', getMaxPrice);
maxPriceSlider.setAttribute('max', getMaxPrice);
maxPriceSlider.setAttribute('value', getMaxPrice);
maxPriceText.setAttribute('value', getMaxPrice);

// Choose min & max prices && Show products that match the price
minPriceText.addEventListener('input', () => {
    minPriceSlider.value = minPriceText.value;

    itemPrice.forEach(el => {
        if (minPriceText.value / 1 > el.textContent.split('рублей')[0] / 1) {
            el.parentElement.style.transform = 'scale(0.1)';
            setTimeout(() => {
                el.parentElement.style.display = 'none';
            }, 300);
        } else if (minPriceText.value / 1 < el.textContent.split('рублей')[0] / 1) {
            el.parentElement.style.display = 'flex';
        }

    })
});
minPriceSlider.addEventListener('input', () => {
    minPriceText.value = minPriceSlider.value;

    itemPrice.forEach(el => {
        if (minPriceSlider.value / 1 > el.textContent.split('рублей')[0] / 1) {
            el.parentElement.style.transform = 'scale(0.1)';
            setTimeout(() => {
                el.parentElement.style.display = 'none';
            }, 300);
        } else if (minPriceSlider.value / 1 < el.textContent.split('рублей')[0] / 1) {
            el.parentElement.style.display = 'flex';
            setTimeout(() => {
                el.parentElement.style.transform = 'scale(1)';
            }, 0);
        }
        if (maxPriceSlider.value / 1 < el.textContent.split('рублей')[0] / 1) {
            el.parentElement.style.display = 'none';
        } else if (maxPriceSlider.value / 1 > el.textContent.split('рублей')[0] / 1) {
            el.parentElement.style.display = 'flex';
        }
    })
});
maxPriceText.addEventListener('input', () => {
    maxPriceSlider.value = maxPriceText.value;

    itemPrice.forEach(el => {
        if (maxPriceText.value / 1 < el.textContent.split('рублей')[0] / 1) {
            el.parentElement.style.transform = 'scale(0.1)';
            setTimeout(() => {
                el.parentElement.style.display = 'none';
            }, 300);
        } else if (maxPriceText.value / 1 > el.textContent.split('рублей')[0] / 1) {
            el.parentElement.style.display = 'flex';
            setTimeout(() => {
                el.parentElement.style.transform = 'scale(1)';
            }, 0);
        }
    })
});
maxPriceSlider.addEventListener('input', () => {
    maxPriceText.value = maxPriceSlider.value;

    itemPrice.forEach(el => {
        if (maxPriceSlider.value / 1 < el.textContent.split('рублей')[0] / 1) {
            el.parentElement.style.transform = 'scale(0.1)';
            setTimeout(() => {
                el.parentElement.style.display = 'none';
            }, 300);
        } else if (maxPriceSlider.value / 1 >= el.textContent.split('рублей')[0] / 1) {
            el.parentElement.style.display = 'flex';
            setTimeout(() => {
                el.parentElement.style.transform = 'scale(1)';
            }, 0);
        }
        if (minPriceSlider.value / 1 > el.textContent.split('рублей')[0] / 1) {
            el.parentElement.style.display = 'none';
        } else if (minPriceSlider.value / 1 <= el.textContent.split('рублей')[0] / 1) {
            el.parentElement.style.display = 'flex';
        }
    })
});