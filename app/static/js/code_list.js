var currentUrl = window.location.href;
var baseUrl = currentUrl.slice(0, currentUrl.lastIndexOf("/"));
var language = currentUrl.split("/").pop();
console.log("URL " + currentUrl + " " + language + " " + baseUrl);
var code_list = document.getElementById("code_list")


var urlTask = currentUrl + "/list"

fetch(urlTask)
    .then(response => response.json())
    .then(data => {
        data.forEach(file => {
            var li = document.createElement("li");
            var a = document.createElement("a");
            var deleteButton = document.createElement("button");

            a.textContent = file;
            a.href = baseUrl + "/typing?file=" + file + "&language=" + language;

            deleteButton.textContent = "Delete";
            deleteButton.addEventListener('click', function(){
                var isSure = window.confirm("Are you sure you want to delete this file?");
                if (isSure) {
                    fetch(currentUrl + "/remove_file/" + file, {
                        method: "POST",
                    })
                    .then(response => {
                        if (response.ok) {
                            li.remove();
                            alert("File deleted successfully!");
                        } else {
                            alert("Error deleting file.");
                        }
                    })
                    .catch(error => {
                        console.error('Error during deletion:', error);
                        alert("An error occurred while trying to delete the file.");
                    });
                }
            });

            
            li.appendChild(a);
            li.appendChild(deleteButton);

            code_list.appendChild(li);
        });
    })
    .catch(error => {
        console.error('Error fetching task list:', error);
    });