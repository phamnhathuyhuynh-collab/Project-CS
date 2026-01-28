const numberOrNameInput = document.getElementById("search-input");
const searchBtn = document.getElementById("search-button");
const informations = document.getElementById("creatures-information");
const stat= document.querySelectorAll(".change p");
let creature1Url = "https://rpg-creature-api.freecodecamp.rocks/api/creature/";
let creaturesUrl = "https://rpg-creature-api.freecodecamp.rocks/api/creatures";

const nameCreature = document.getElementById("creature-name");
const idCreature = document.getElementById("creature-id");
const weightCreature = document.getElementById("weight");
const heightCreature = document.getElementById("height");
const typesCreature = document.getElementById("types");
const specialCreature = document.getElementById("special");




const fetchData = async () => {
    try {
        const res = await fetch(`${creature1Url}${numberOrNameInput.value}`);
        const data = await res.json();
        showResult(data);
             
    }catch(err) {
        alert("creature not found");
    }
}



const showResult = (data) => {
    
    const { id, name, weight, height, special, types, stats } = data;

    stat.forEach((item, index) => item.textContent = stats[index].base_stat);
    nameCreature.innerHTML = name;
    idCreature.innerHTML = `#${id}`;
    weightCreature.innerHTML = `Weight: ${weight}`;
    heightCreature.innerHTML = `Height: ${height}`;
    if(types.length >=2){
        typesCreature.innerHTML = `
            <div class="${types[0].name}" id="type"><p>${types[0].name.toUpperCase()}</p></div>
            <div class="${types[1].name}" id="type"><p>${types[1].name.toUpperCase()}</p></div>
        `
    }else{
        typesCreature.innerHTML = `
            <div class="${types[0].name}" id="type"><p>${types[0].name.toUpperCase()}</p></div>
           
        `
    }
    specialCreature.innerHTML = `<h3>${special.name}</h3>
                                    <p>${special.description}</p>
                                    `


}

searchBtn.addEventListener("click", () => {
    fetchData();
   
});
