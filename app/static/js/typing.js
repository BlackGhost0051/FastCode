var keyboard = document.getElementById("keyboard");


function keyDown(event) {
    const blockedKeys = [''];

    console.log(`${event.key}`);
    const keyElement = Array.from(document.getElementsByClassName('key')).find(key => key.textContent.toLowerCase() === event.key.toLowerCase());
    
    if (keyElement) {
        keyElement.classList.add('active');
        event.preventDefault();
    }
}

function keyUp(event) {
    const keyElement = Array.from(document.getElementsByClassName('key')).find(key => key.textContent.toLowerCase() === event.key.toLowerCase());
    if (keyElement) {
        keyElement.classList.remove('active');
    }
}


document.addEventListener('keydown', keyDown);
document.addEventListener('keyup', keyUp);


keyboard.addEventListener('click', function(event) {
    if (event.target.classList.contains('key')) {
        event.target.classList.toggle('active');
    }
});