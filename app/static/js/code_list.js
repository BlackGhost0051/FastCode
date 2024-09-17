var currentUrl = window.location.href;
var code_list = document.getElementById("code_list")


var urlTask = currentUrl + "/list"

fetch(urlTask)
    .then(response => response.json())
    .then(data => {
        data.forEach(file => {
            var li = document.createElement("li");
            li.textContent = file;
            code_list.appendChild(li);
        });
    })
    .catch(error => {
        console.error('Error fetching task list:', error);
    });