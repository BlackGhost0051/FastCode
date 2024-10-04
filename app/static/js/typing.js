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
        
        if(char === '\n'){
            console.log("Line");
            span.classList.add("new-line-char");
            var br = document.createElement("br");
            code_typing.appendChild(br);
        }
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
        scrollToCurrentChar();
    }
}

function keyDown(event) {
    const currentChar = code[typingIndex];
    const chars = document.getElementsByClassName("code-char");


    if(event.key === "Shift"){
        return;
    }

    if(typingIndex == code.length - 1){
        console.log("End");
        console.log(failedChars);
        return;
    }

    

    if (event.key === "Tab") {
        event.preventDefault();
        console.log("TAB");

        for(var i = 0; i < 4; i++){
            if (code[typingIndex] === ' ') {
                typingIndex++;
                typing();
                console.log("Space added for Tab, index now:", typingIndex);
            } else {
                chars[typingIndex].classList.add("failed");
                failedChars.push(currentChar);
                typingIndex++;
                typing();
            }
        }

        return;
    }

    if (event.key === "Enter") {
        if (currentChar === '\n') {
            typingIndex++;
            typing();
            console.log("New line detected, moving index to:", typingIndex);
        } else {
            chars[typingIndex].classList.add("failed");
            failedChars.push(currentChar);
            typingIndex++;
            typing();
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

function scrollToCurrentChar() {
    const currentChar = document.getElementsByClassName("blinking")[0];
    if (currentChar) {
        currentChar.scrollIntoView({ behavior: "smooth", block: "center" });
    }
}

document.addEventListener('keydown', keyDown);
document.addEventListener('keyup', keyUp);


keyboard.addEventListener('click', function(event) {
    if (event.target.classList.contains('key')) {
        event.target.classList.toggle('active');
    }
});