const numberInput = document.getElementById("number");
const convertBtn = document.getElementById("convert-btn");
const output = document.getElementById("output");

const romanNumberData = [
    {
        romanNumeral: "M",
        arabicNumeral: 1000,
    },{
        romanNumeral: "CM",
        arabicNumeral: 900,
    },{
        romanNumeral: "D",
        arabicNumeral: 500,
    },{
        romanNumeral: "CD",
        arabicNumeral: 400,
    },{
        romanNumeral: "C",
        arabicNumeral: 100,
    },{
        romanNumeral: "XC",
        arabicNumeral: 90,
    },{
        romanNumeral: "L",
        arabicNumeral: 50,
    },{
        romanNumeral: "XL",
        arabicNumeral: 40,
    },{
        romanNumeral: "X",
        arabicNumeral: 10,
    },{
        romanNumeral: "IX",
        arabicNumeral: 9,
    },{
        romanNumeral: "V",
        arabicNumeral: 5,
    },{
        romanNumeral: "IV",
        arabicNumeral: 4,
    },{
        romanNumeral: "I",
        arabicNumeral: 1,
    },  
];


const showConvert = () =>{
    const val = (parseInt(numberInput.value));
    if (val < 0) {
        output.innerHTML = `<p class="alert">Please enter a number greater than or equal to 1</p>`;
        output.classList.remove('hidden');
        return;
    };
    if(!val){
        output.innerHTML = `<p class="alert">Please enter a valid number</p>`;
        output.classList.remove('hidden');
        return;
    };
    if(val > 3999){
        output.innerHTML = `<p class="alert">Please enter a number less than or equal to 3999</p>`;
        output.classList.remove('hidden');
        return;
    };
    output.innerHTML = `<p>${convert(val)}</p>`;
   output.classList.remove('hidden');
}


const convert = (val) =>{
    let result = "";
    while(val >0){
        for(let i =0; i<romanNumberData.length; i++){
            if(val >= romanNumberData[i].arabicNumeral){
                result  += romanNumberData[i].romanNumeral;
                val -= romanNumberData[i].arabicNumeral;
                break;
            }
        }
    }
    return result;
};

document.getElementById("form").addEventListener("submit", (e) => {
    e.preventDefault(); // Prevent page reload


    showConvert();
   numberInput.value = "";

});
