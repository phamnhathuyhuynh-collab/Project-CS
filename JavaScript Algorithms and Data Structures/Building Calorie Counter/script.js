const calorieCounter = document.getElementById('calorie-counter'); // với document.getElementById() ta có thể sử dụng truy cập id nhanh gọn hơn
const budgetNumberInput = document.getElementById('budget');
const entryDropdown = document.getElementById('entry-dropdown');
const addEntryButton = document.getElementById('add-entry');
const clearButton = document.getElementById('clear');
const output = document.getElementById('output');
let isError = false;

function cleanInputString(str){
  const regex = /[+-\s]/g;
  return str.replace(regex, "");
}

//hàm isInvalidInput này dùng để kiểm tra xem số liệu nhập có phải là số khoa học dạng 1e3... vd như vậy không
function isInvalidInput(str){ 
  const regex = /\d+e\d+/i;
  return str.match(regex);
}

function addEntry(){
  const targetInputContainer = document.querySelector(`#${entryDropdown.value} .input-container`);
  const entryNumber = targetInputContainer.querySelectorAll('input[type="text"]').length +1;
  const HTMLString = `
    <label for="${entryDropdown.value}-${entryNumber}-name">Entry ${entryNumber} Name</label>
    <input type="text" id="${entryDropdown.value}-${entryNumber}-name" placeholder="Name" />
    <label for="${entryDropdown.value}-${entryNumber}-calories">Entry ${entryNumber} Calories</label>
    <input type="number" id="${entryDropdown.value}-${entryNumber}-calories" placeholder="Calories" />
  `;
  targetInputContainer.insertAdjacentHTML("beforeend", HTMLString);
}

function calculateCalories(e){
  e.preventDefault();
  isError = false;

  const breakfastNumberInput = document.querySelectorAll("#breakfast input[type='number']");
  const lunchNumberInput = document.querySelectorAll("#lunch input[type='number']");
  const dinnerNumberInput = document.querySelectorAll("#dinner input[type='number']");
  const snacksNumberInput = document.querySelectorAll("#snacks input[type='number']");
  const exerciseNumberInput = document.querySelectorAll("#exercise input[type='number']");

  const breakfastCalories = getCaloriesFromInputs(breakfastNumberInput);
  const lunchCalories = getCaloriesFromInputs(lunchNumberInput);
  const dinnerCalories = getCaloriesFromInputs(dinnerNumberInput);
  const snacksCalories = getCaloriesFromInputs(snacksNumberInput);
  const exerciseCalories = getCaloriesFromInputs(exerciseNumberInput);
  const budgetCalories = getCaloriesFromInputs([budgetNumberInput]); //vì budgetNUmberInput nhận số liệu không phải là 1 mảng

  if(isError){ //mặc dù đã khai isError = false; bên trên nhưng khi gọi hàm getCaloriesFromInput() có nguy cơ giá trị bị 
    return;    //thay đổi nên tốt nhất dùng hàm này để kiểm tra lại xem giá trị bị thay đổi hay chưa 
  }

  const consumedCalories = breakfastCalories + lunchCalories + dinnerCalories + snacksCalories;
  const remainingCalories = budgetCalories - consumedCalories + exerciseCalories;

  const surplusOrDeficit = remainingCalories < 0 ? 'Surplus' : 'Deficit';
  output.innerHTML = `
    <span class="${surplusOrDeficit.toLowerCase()}">${Math.abs(remainingCalories)} calorie ${surplusOrDeficit}</span>
    <hr>
    <p>${budgetCalories} Calories Budgeted</p>
    <p>${consumedCalories} Calories Consumed</p>
    <p>${exerciseCalories} Calories Burned</p>
  `;
  
  output.classList.remove('hide');
}

function getCaloriesFromInputs(list){
  let calories = 0;

  for(const item of list){
    const currVal = cleanInputString(item.value); //item.value vì list không phải là một dãy thường mà là dãy tổng hợp từ querySelector nên phải có value mới lấy được giá trị 
    const invalidInputMatch = isInvalidInput(currVal);

    if(invalidInputMatch){
      alert(`Invalid Input: ${invalidInputMatch[0]}`);
      isError = true; 
      return null;
    }

    calories += Number(currVal);
  }
  return calories;
}

function clearForm(){
  const inputContainers = Array.from(document.querySelectorAll('.input-container'));

  for(const container of inputContainers){
    container.innerHTML = "";
  }

  budgetNumberInput.value = "";
  output.innerText = "";
  output.classList.add('hide');
}

addEntryButton.addEventListener("click", addEntry);
clearButton.addEventListener("click", clearForm);
calorieCounter.addEventListener("submit", calculateCalories); //trong form: có type="submit" nên với dòng này có thể kích hoạt button calculate remaining calories