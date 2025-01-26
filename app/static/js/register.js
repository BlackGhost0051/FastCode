console.log("Register");

const register_button = document.getElementById("register_button");
const login_input = document.getElementById("login");
const password_0_input = document.getElementById("password_0");
const password_1_input = document.getElementById("password_1");

register_button.addEventListener("click", () => {
    const login = login_input.value;
    const password0 = password_0_input.value;
    const password1 = password_1_input.value;

    if (!login || !password0 || !password1) {
        alert("All fields are required!");
        return;
    }

    if (password0 !== password1) {
        alert("Passwords do not match!");
        return;
    }

    fetch("/register",{
        method: "POST",
        body: JSON.stringify(
            {
            login: login,
            password: password0,
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
        window.location.href = '/login';
    })
    .catch((error) => {
        console.error("Error occurred:", error);
    });
});