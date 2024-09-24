var typingIndex = 0;

var keyboard = document.getElementById("keyboard");
var code_typing = document.getElementById("code_typing");


const urlParams = new URLSearchParams(window.location.search);

const file = urlParams.get('file');
const language = urlParams.get('language');

console.log(file + " " + language);

var codeTaskUrl = "/" + language + "/get_code/" + file;
var code;

fetch(codeTaskUrl)
.then(response => {
    if(response.ok){
        return response.text();
    } else {
        throw new Error("File not found");
    }
})
.then(code=> {
    console.log(code);

    code_typing.innerHTML = '';

    for(let i = 0; i < code.length; i++){
        let char = code[i];
        let span = document.createElement("span");

        span.textContent = char;
        span.classList.add("code-char");
        code_typing.appendChild(span);
    }


})
.catch(error => {
    console.error('Error:', error);
});




function typing(){

}



function keyDown(event) {
    const blockedKeys = [''];

    console.log(`${event.key}`);
    const keyElement = Array.from(document.getElementsByClassName('key')).find(key => key.textContent.toLowerCase() === event.key.toLowerCase());
    
    if (keyElement) {
        keyElement.classList.add('active');
        //event.preventDefault();
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