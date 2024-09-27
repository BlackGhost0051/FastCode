var languages_block = document.getElementById("languages_block");
var taskUrl =  "/languages_list";



console.log(taskUrl);


fetch(taskUrl)
    .then(responce => {
        if(responce.ok){
            return responce.json();
        } else {
            throw new Error("Something go wrong");
        }
    })
    .then(data => {
        console.log(data);
        
        Object.entries(data).forEach(([key, value]) => {
            var li = document.createElement("li");
            var a = document.createElement("a");
            var img = document.createElement("img");
            var p = document.createElement("p");

            img.src = `/static/images/${value}_logo.svg`;
            img.alt = `${value} logo`;

            p.textContent = value;
            a.href = `/${value}`;

            a.prepend(p);
            a.prepend(img);
            li.appendChild(a);
            languages_block.appendChild(li);
        });
    })
    .catch(error => {
        console.error('Error:', error);
      });