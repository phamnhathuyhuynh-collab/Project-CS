let price = 19.5;
let cid =[["PENNY", 1.01], ["NICKEL", 2.05], ["DIME", 3.1], ["QUARTER", 4.25], ["ONE", 90], ["FIVE", 55], ["TEN", 20], ["TWENTY", 60], ["ONE HUNDRED", 100]];
let copy = cid.map(arr => [...arr]);

const cashInput = document.getElementById("cash");
const changeDue = document.getElementById("change-due");
const purchaseBtn = document.getElementById("purchase-btn");
const totalCash = document.querySelector(".total-cash p");
const cashDrawer = document.querySelectorAll(".price");

const pricePerCoin2 = [100, 20, 10, 5, 1, 0.25, 0.1, 0.05, 0.01];
const pricePerCoin = [0.01, 0.05, 0.1, 0.25, 1, 5, 10 ,20 , 100];
const objPricePerCoin2 = {
    0.01 : 'PENNY',
    0.05 : 'NICKEL',
    0.1 : 'DIME',
    0.25 : 'QUARTER',
    1 : 'ONE',
    5 : 'FIVE',
    10 : 'TEN',
    20 : 'TWENTY',
    100 : 'ONE HUNDRED',
}

totalCash.innerHTML += `$${Math.round(price *100) /100}`;

cashDrawer.forEach((cash, index) => {
    cash.innerHTML = `$${Math.round(cid[index][1] *100) /100}`;
});

let sumOfAllCash = cid.reduce((a,b) => a + b[1], 0);
sumOfAllCash = Math.round(sumOfAllCash*100) /100;
const calculateCashReturn = (cashCustomer) => {
    changeDue.innerHTML = "";
    let sumOfAllCash = cid.reduce((a,b) => a + b[1], 0);
    sumOfAllCash = Math.round(sumOfAllCash*100) /100;

    let cashReturn = cashCustomer - price;
    cashReturn = Math.round(cashReturn*100) /100;
  
    if(cashCustomer - price < 0){
        alert("Customer does not have enough money to purchase the item");
        return;
    };
    if(cashCustomer - price === 0){
        changeDue.textContent = "No change due - customer paid with exact cash";
        return;
    };
    if((sumOfAllCash - cashReturn) < 0){
        changeDue.textContent = "Status: INSUFFICIENT_FUNDS";
        return;
    };
    
    if(cashReturn === sumOfAllCash){
    changeDue.innerHTML = "Status: CLOSED";
    for(let i =cid.length-1; i >= 0 ; i--){
        if(cid[i][1] >0){
            const coinName = cid[i][0];
            changeDue.innerHTML += `<p>${coinName}: $${cid[i][1]}</p>`;
        }
    };
    cashDrawer.forEach((cash) => {
    cash.innerHTML = "$0";
});
    return;
} else {
    changeDue.innerHTML = "Status: OPEN";
}

    for(let i = 0; i < pricePerCoin2.length; i++ ){
        let count = 0;
        while(cashReturn >= pricePerCoin2[i] && cid[pricePerCoin2.length - i - 1 ][1] > 0 && (cashReturn - pricePerCoin2[i]) >= 0 && cashReturn > 0){
            cashReturn = Math.round((cashReturn - pricePerCoin2[i]) * 100) / 100;
            count++;
            cid[pricePerCoin2.length - i - 1 ][1] =  cid[pricePerCoin2.length - i - 1 ][1] -pricePerCoin2[i];
            cid[pricePerCoin2.length - i - 1 ][1] = Math.round(cid[pricePerCoin2.length - i - 1 ][1]*100) /100;
        };
        if(i === pricePerCoin2.length - 1){
           
            if(cashReturn > 0){
                  

                changeDue.textContent = "Status: INSUFFICIENT_FUNDS";
                return;
            }
        };
        if(count > 0){
            changeDue.innerHTML += `<p>${objPricePerCoin2[pricePerCoin2[i]]}: $${(pricePerCoin2[i] * count).toFixed(2)}</p>`;
        };   
    }
    
   cashDrawer.forEach((cash, index) => {
    cash.innerHTML = `$${Math.round(cid[index][1] *100) /100}`;
});

}



purchaseBtn.addEventListener("click", () => {
    
    calculateCashReturn(Math.round(cashInput.value*100) /100);
    cashInput.value = "";
})

