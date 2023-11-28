const sliderButtons = document.querySelectorAll('.fa-arrow-alt-circle-right, .fa-arrow-alt-circle-left');
const sliderLine = document.querySelectorAll('.slider-line');

window.addEventListener('load', () => {
    sliderLine.forEach(el => {
        if (el.children.length > 5) {
            sliderButtons.forEach(el => {
                el.style.display = 'block';
            })
        }
    })
})

const sliderLineLeftButton = document.querySelectorAll('.fa-arrow-alt-circle-left');
const sliderLineRightButton = document.querySelectorAll('.fa-arrow-alt-circle-right');
const itemElement = document.querySelectorAll('.item__element');

function sliderButtonEvent(button) {
    button.forEach(el => {
        let xOffset = 0;
        el.addEventListener('click', () => {
            if (button == sliderLineRightButton) {
                xOffset = el.previousElementSibling.style.right.split('p')[0] / 1;
                const maxOffset = (el.previousElementSibling.children.length - 5) * 255;
                xOffset += 255;
                el.previousElementSibling.style.right = xOffset + 'px';
                if (xOffset > maxOffset) {
                    xOffset = maxOffset;
                    el.previousElementSibling.style.right = xOffset + 'px';
                }
            } else if (button == sliderLineLeftButton) {
                xOffset = el.parentElement.children[2].style.right.split('p')[0] / 1;
                xOffset -= 255;
                el.parentElement.children[2].style.right = xOffset + 'px';
                console.log(xOffset);
                if (xOffset < 0) {
                    xOffset = 0;
                    el.parentElement.children[2].style.right = xOffset + 'px';
                }
            }
        })
    });
}
sliderButtonEvent(sliderLineLeftButton);
sliderButtonEvent(sliderLineRightButton);