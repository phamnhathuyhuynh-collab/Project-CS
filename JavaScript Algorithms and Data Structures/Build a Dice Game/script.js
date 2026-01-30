const listOfAllDice = document.querySelectorAll(".die");
const scoreInputs = document.querySelectorAll("#score-options input");
const scoreSpans = document.querySelectorAll("#score-options span");
const roundElement = document.getElementById("current-round");
const rollsElement = document.getElementById("current-round-rolls");
const totalScoreElement = document.getElementById("total-score");
const rollDiceBtn = document.getElementById("roll-dice-btn");
const keepScoreBtn = document.getElementById("keep-score-btn");
const rulesContainer = document.querySelector(".rules-container");
const rulesBtn = document.getElementById("rules-btn");
const scoreHistory = document.getElementById("score-history");

let diceValuesArr = [];
let rolls = 0;
let round = 0;
let isModalShowing = false;
let score = 0;

const rollDice = () => {
    diceValuesArr = [];
    for(let i =0; i < 5; i++){
        const randomDice = Math.floor(Math.random() * 6) + 1    ;
        diceValuesArr.push(randomDice);
    };
    listOfAllDice.forEach((dice, index) => {
        dice.textContent = diceValuesArr[index];
    });
};

const updateStats = () => {
    rollsElement.textContent = rolls;
    roundElement.textContent = round;
};

const updateRadioOptions = (index, score) => {
    scoreInputs[index].disabled = false;
    scoreInputs[index].value = score;
    scoreSpans[index].textContent = `, score = ${score}`;
};

const updateScore = (selectedValue, achieved) => {
    score += parseInt(selectedValue);
    totalScoreElement.textContent = score;
    scoreHistory.innerHTML += `<li>${achieved} : ${selectedValue}</li>`;
};

const getHighestDuplicates = (arr) => {
    const counts = {};

    for(const num of arr){
        if(counts[num]){
            counts[num]++;
        }else{
            counts[num] = 1;
        }
    };
    let highestDuplicates = 0;
    for(const num of arr){
        const count = counts[num];
        if(count >=3 && count > highestDuplicates){
            highestDuplicates = count;
        }
        if( count >= 4 && count > highestDuplicates){
            highestDuplicates = count;
        };
    };
    const sumOfAllDice = arr.reduce((a, b) => a + b, 0);
    if(highestDuplicates >=4){
        updateRadioOptions(1, sumOfAllDice);
    }
    if(highestDuplicates >=3){
        updateRadioOptions(0, sumOfAllDice);
    };
};

const detectFullHouse = (arr) => {
    const counts = {};
    for(const num of arr){
        counts[num] = counts[num] ? counts[num] + 1 : 1;
    };

    const hasThreeOfAKind = Object.values(counts).includes(3);
    const hasPair = Object.values(counts).includes(2);

    if(hasPair && hasThreeOfAKind){
        updateRadioOptions(2, 25);
    };
};

const checkForStraights = (arr) => {
    const sortedNumbersArr = arr.sort((a, b) => a - b);
    const uniqueNumbersArr = [...new Set(sortedNumbersArr)];
    const uniqueNumbersStr = uniqueNumbersArr.join("");

    const smallStraightArr = ["1234", "2345", "3456"];
    const largeStraightArr = ["12345", "23456"];

    if(smallStraightArr.some(straight => uniqueNumbersStr.includes(straight))){
        updateRadioOptions(3, 30);
    }
    if(largeStraightArr.includes(uniqueNumbersStr)){
        updateRadioOptions(4, 40);
    };
};

const resetRadioOptions = () => {
    scoreInputs.forEach((input) => {
        input.disabled = true;
        input.checked = false;
    });
    scoreSpans.forEach((span) => {
        span.textContent = "";
    });
};

const resetGame = () => {
    diceValuesArr = [0, 0, 0, 0, 0];
    rolls = 0;
    round = 1;
    score = 0;
    listOfAllDice.forEach((dice, index) => {
        dice.textContent = diceValuesArr[index];
    });
    totalScoreElement.textContent = score;
    roundElement.textContent = round;
    rollsElement.textContent = rolls;
    scoreHistory.innerHTML = "";
    resetRadioOptions();
};

rollDiceBtn.addEventListener("click", () => {
    if(rolls === 3){
        alert("You have made three rolls this round. Please select a score.");
    }else{
        rolls++;
        resetRadioOptions();
        rollDice();
        updateStats();
        getHighestDuplicates(diceValuesArr);
        detectFullHouse(diceValuesArr);
        checkForStraights(diceValuesArr);
        updateRadioOptions(5, 0);
    };
});

rulesBtn.addEventListener("click", () => {
    isModalShowing = !isModalShowing;
    rulesContainer.style.display = isModalShowing ? "block" : "none";
    rulesBtn.textContent = isModalShowing ? "Hide rules" : "Show rules";
});

keepScoreBtn.addEventListener("click", () => {
    let selectedValue;
    let achieved;
    for(const radioButton of scoreInputs){
        if(radioButton.checked){
            selectedValue = radioButton.value;
            achieved = radioButton.id;
            break;

        };
    };
    if(selectedValue){
        rolls = 0;
        round++;
        updateStats();
        resetRadioOptions();
        updateScore(selectedValue, achieved);
    
    if(round > 6){
        setTimeout(() => {
            alert(`Game Over! Your total score is ${score}`);
            resetGame();
        }, 500);
    }}else{
        alert("Please select an option or roll the dice");
    }
});