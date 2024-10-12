console.log("Test");

let info_div = document.getElementById("info_div");

fetch("/get_statistics")
    .then(responce => {
        if(responce.ok){
            return responce.json();
        } else {
            throw new Error("Something go wrong");
        }
    })
    .then(data => {
        info_div.innerHTML = "";

        data.forEach(stat => {
            const statDiv = document.createElement("div");
            statDiv.classList.add("stat-div");

            const fileName = document.createElement("p");
            fileName.textContent = `File name: ${stat.file_name}`;
            statDiv.appendChild(fileName);

            const chars = document.createElement("p");
            chars.textContent = `Failed chars: ${stat.chars}`;
            statDiv.appendChild(chars);

            const time = document.createElement("p");
            time.textContent = `Time: ${stat.time}`;
            statDiv.appendChild(time);

            const typingSpeed = document.createElement("p");
            typingSpeed.textContent = `Typing speed: ${stat.typing_speed !== null ? stat.typing_speed : 'N/A'}`;
            statDiv.appendChild(typingSpeed);

            const br = document.createElement("br");
            statDiv.appendChild(br);

            info_div.appendChild(statDiv);
        });

    })
    .catch(error => {
        console.log(error);
    })