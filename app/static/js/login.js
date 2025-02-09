console.log("Login");


const login_button = document.getElementById("login_button");
const login_input = document.getElementById("login");
const password_input = document.getElementById("password");



login_button.addEventListener("click", () => {
    fetch("/login",{
        method: "POST",
        body: JSON.stringify(
            {
            login: login_input.value,
            password: password_input.value
            }
        ),
        headers:{
            "Content-type": "application/json; charset=UTF-8"
        }
    })
    .then((response) => { 
        if (!response.ok){
            console.error(`HTTP error! Status: ${response.status}`);
            alert(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
    })
    .then((data) => {
        console.log(data)
        window.location.href = "/";
    })
    .catch((error) => {
        console.error("Error occurred:", error);
    });
});