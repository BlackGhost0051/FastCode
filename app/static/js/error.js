const statusCodeElement = document.getElementById("status_code");
const body = document.body;
const statusText = statusCodeElement.textContent;

let currentIndex = 0;
let delay = 2000;
let hue = 0;

statusCodeElement.innerHTML = statusText.split('').map(char => `<span>${char}</span>`).join('');
const spans = document.querySelectorAll("#status_code span");



function animate() {
    spans.forEach((span, index) => {
        setTimeout(() => {
            span.style.opacity = 0;
            setTimeout(() => {
                span.style.opacity = 1;
            }, delay/2);
        }, index * delay);
    });
}

setInterval(animate, spans.length * delay);
animate();


function changeColor() {
    hue = (hue + 1) % 360;
    body.style.backgroundColor = `hsl(${hue}, 100%, 50%)`;
}

setInterval(changeColor, 100);
