const input = document.getElementById("user-input");
const checkBtn = document.getElementById("check-btn");
const clearBtn = document.getElementById("clear-btn");
const results = document.getElementById("results-div");

const showResult = () =>{
    const str = input.value;
    if(checkFunction(str)){
        results.textContent += `Valid US number: ${checkFunction(str)[0]}`;
    }else if(str === ""){
        alert(`Please provide a phone number`);
    }else{
        results.textContent += `Invalid US number: ${str}`;
    }
    input.value = "";
}

const checkFunction = (str) => {
    const regex = /^1?\s?(\([0-9][0-9][0-9]\)|[0-9][0-9][0-9])[\s|-]?([0-9][0-9][0-9])[\s|-]?([0-9][0-9][0-9][0-9])$/;
    return str.match(regex);
}

const clearFunction = () => {
    results.textContent = "";
}

checkBtn.addEventListener("click", showResult);
clearBtn.addEventListener("click", clearFunction);