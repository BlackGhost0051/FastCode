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
        const keys = Object.keys(data);
        
        
        console.log(keys);
        console.log(data);
        console.log(data[0].file_name);
        
    })
    .catch(error => {
        console.log(error);
    })