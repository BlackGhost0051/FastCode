// console.log("Test");
//
// let info_div = document.getElementById("info_div");
// let all_chars_data = [];
//
// fetch("/get_statistics")
//     .then(responce => {
//         if(responce.ok){
//             return responce.json();
//         } else {
//             throw new Error("Something go wrong");
//         }
//     })
//     .then(data => {
//         info_div.innerHTML = "";
//
//         data.forEach(stat => {
//             const statDiv = document.createElement("div");
//             statDiv.classList.add("stat-div");
//
//             const fileName = document.createElement("p");
//             fileName.textContent = `File name: ${stat.file_name}`;
//             statDiv.appendChild(fileName);
//
//             const chars = document.createElement("p");
//             chars.textContent = `Failed chars: ${stat.chars}`;
//             statDiv.appendChild(chars);
//
//             all_chars_data.push(stat.chars);
//
//             const time = document.createElement("p");
//             time.textContent = `Time: ${stat.time}`;
//             statDiv.appendChild(time);
//
//             const typingSpeed = document.createElement("p");
//             typingSpeed.textContent = `Typing speed: ${stat.typing_speed !== null ? stat.typing_speed : 'N/A'}`;
//             statDiv.appendChild(typingSpeed);
//
//             const br = document.createElement("br");
//             statDiv.appendChild(br);
//
//             info_div.appendChild(statDiv);
//         });
//
//     })
//     .catch(error => {
//         console.log(error);
//     })
//
// console.log(all_chars_data);
//
// const str = "d,e,f, ,m,a,i,n,(,),:,\n, , , , ,p,r,i,n,t,(,\"T,e,t,\",),\n,\n,i,f, ,_,_,n,a,m,e,_,_, ,=,=, ,',_,_,m,a,i,n,_,_,',:\n, , , , ,m,a,i,n,(,l,u,d,e, ,<,i,n,(,n,t,f,(,\"\",\"\",t,t,t,t,\n, ,r,e,t,u,r,n, ,0,;,}";
// const charArray = str.split(',');
// charArray.sort();
//
// makeHistogram(charArray);
//
//
// function makeHistogram(chars){
//     const ctx = document.getElementById("all_info_histogram");
//
//     const histogramData = {};
//     chars.forEach(value => {
//         histogramData[value] = (histogramData[value] || 0) + 1;
//     });
//
//     console.log(histogramData);
//
//     const labels = Object.keys(histogramData);
//     const counts = Object.values(histogramData);
//
//     const backgroundColors = counts.map(() => getRandomColor());
//     const borderColors = counts.map(() => getRandomColor());
//
//     const myHistogram = new Chart(ctx, {
//         type: 'bar',
//         data: {
//             labels: labels,
//             datasets: [{
//                 label: 'Frequency',
//                 data: counts,
//                 backgroundColor: backgroundColors,
//             }]
//         },
//         options: {
//             scales: {
//                 y: {
//                     beginAtZero: true
//                 }
//             }
//         }
//     });
// }
//
// function getRandomColor() {
//     const r = Math.floor(Math.random() * 256);
//     const g = Math.floor(Math.random() * 256);
//     const b = Math.floor(Math.random() * 256);
//     const a = 0.6;
//     return `rgba(${r}, ${g}, ${b}, ${a})`;
// }