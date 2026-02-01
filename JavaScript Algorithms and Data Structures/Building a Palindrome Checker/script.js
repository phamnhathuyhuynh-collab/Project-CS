const result = document.getElementById('result');
const checkButton = document.getElementById('check-btn');
const textInput = document.getElementById('text-input');

const showResult = () =>{
    if(palindromeChecker(textInput.value)){
        result.innerHTML = `<p>${textInput.value} is a Palindrome</p>`;
    }else{
        result.innerHTML = `<p>${textInput.value} is not a Palindrome</p>`;
    }
    result.classList.remove('hide');
}


const palindromeChecker = (textInputValue) =>{
    const regex = /[^a-zA-Z0-9]/gi; 
    const afterDelete = textInputValue.replace(regex , '');
    for(let i = 0; i < Math.floor(afterDelete.length/2); i++){
            if(afterDelete[i].toLowerCase() !== afterDelete[afterDelete.length-i-1].toLowerCase()){
                return false;
            }
    }
    return true;
}

checkButton.addEventListener("click", () => {
    if(textInput.value === ""){
        alert("Please input a value");
    }else{
        showResult();
    }
});