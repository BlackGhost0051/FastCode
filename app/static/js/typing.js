var typingIndex = 0;
var typingSpeed = 100;
var code_typing = document.getElementById("code_typing");
var code;
var failedChars = [];

const urlParams = new URLSearchParams(window.location.search);
const file = urlParams.get('file');
const language = urlParams.get('language');
var codeTaskUrl = "/" + language + "/get_code/" + file;

console.log(file + " " + language);

fetch(codeTaskUrl)
.then(response => {
    if (response.ok) {
        return response.text();
    } else {
        throw new Error("File not found");
    }
})
.then(fetchedCode => {
    code = fetchedCode;
    code_typing.innerHTML = '';

    for (let i = 0; i < code.length; i++) {
        let char = code[i];
        let span = document.createElement("span");
        span.textContent = char;
        span.classList.add("code-char");
        code_typing.appendChild(span);
    }

    typing();
})
.catch(error => {
    console.error('Error:', error);
});


function typing(reverse = false) {
    var chars = document.getElementsByClassName("code-char");

    if (reverse && typingIndex > 0) {
        chars[typingIndex].classList.remove("blinking");
        if (typingIndex > 0) {
            if (chars[typingIndex - 1].classList.contains("failed")) {
                chars[typingIndex - 1].classList.remove("failed");
            }
            chars[typingIndex - 1].classList.add("blinking");
        }
    } else if (typingIndex < code.length) {
        if (typingIndex > 0) {
            chars[typingIndex - 1].classList.remove("blinking");
        }
        chars[typingIndex].classList.add("blinking");
    }
}

function keyDown(event) {
    const currentChar = code[typingIndex];
    const chars = document.getElementsByClassName("code-char");


    if(typingIndex == code.length){
        console.log("End");
        console.log(failedChars);
        return;
    }

    if(event.key === "Shift"){
        return;
    }

    if (event.key === "Tab") {
        event.preventDefault();
        console.log("TAB");
        return;
    }
    // ? use allowed char or ban keys
    // Need make Tab = ' ', ' ', ' ' , ' '
    // Problem with \n user dont see element ( add class new_line ( css = background url(img_new_line.svg) size 0.4x0.4 ex) ?

    if (event.key === "Enter") {
        if (currentChar === '\n') {
            typing();
            typingIndex++;
            console.log("New line detected, moving index to:", typingIndex);
        }
        return;
    }

    if (event.key === "Backspace") {
        if (typingIndex > 0) {
            typing(true);
            typingIndex--;
            console.log("Backspace pressed, index now:", typingIndex);
        }
        return;
    }

    if (typingIndex < code.length && event.key === currentChar) {
        typingIndex++;
        typing();
        console.log("Character matched:", event.key, "Index now:", typingIndex);
    } else {
        chars[typingIndex].classList.add("failed");
        console.log("Incorrect character:", event.key, "Expected:", currentChar, "Index now:", typingIndex);
        failedChars.push(currentChar);
        typingIndex++;
        typing();
    }

    const keyElement = Array.from(document.getElementsByClassName('key')).find(key => key.textContent.toLowerCase() === event.key.toLowerCase());
    if (keyElement) {
        keyElement.classList.add('active');
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