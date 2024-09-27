var random_button = document.getElementById("random_button");


random_button.addEventListener('click', () => {

    fetch("/languages_list")
        .then(responce => {
            if(responce.ok){
                return responce.json();
            } else {
                throw new Error("Something go wrong");
            }
        })
        .then(data =>{
            const keys = Object.keys(data);
            const randomLanguage = data[keys[Math.floor(Math.random() * keys.length)]];

            
            return fetch(`/${randomLanguage}/list`)
                .then(response => {
                    if(response.ok){
                        return response.json();
                    } else {
                        throw new Error("Failed to get files for the selected language");
                    }
                })
                .then(files =>{
                    const randomFile = files[Math.floor(Math.random() * files.length)];
                    console.log(randomLanguage + " " + randomFile);


                    const url = `/typing?file=${randomFile}&language=${randomLanguage}`;
                    window.location.href = url;
                });
        })
        .catch(error => {
            console.error(error);
        });
});