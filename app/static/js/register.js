console.log("Register");

const register_button = document.getElementById("register_button");
const login_input = document.getElementById("login");
const password_0_input = document.getElementById("password_0");
const password_1_input = document.getElementById("password_1");

register_button.addEventListener("click", () => {
    fetch("/register",{
        method: "POST",
        body: JSON.stringify(
            {
            login: login_input.value,
            password_0: password_0_input.value,
            password_1: password_1_input.value
            }
        ),
        headers:{
            "Content-type": "application/json; charset=UTF-8"
        }
    })
    .then((response) => { 
        if (!response.ok){
            console.error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
    })
    .then((data) => {
        console.log(data)
    })
    .catch((error) => {
        console.error("Error occurred:", error);
    });
});