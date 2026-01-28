const ouiButton = document.getElementById("oui")
const nonButton = document.getElementById("non")
let imageAdded = document.getElementById("image")
nonButton.addEventListener(()=>{
    imageAdded.innerHTML += `<img src="mikasa-ackerman-attack-on-titan-final-season.avif" width=700px height="450px" >`
})