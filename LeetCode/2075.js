const encodedText = 'whurqonhhaymkrxebpdagccsjvoontnejzqkmqdedwkbjsas t kga kjjchpxkkuraiyvmsx gvvfbkfx yrpydxajzmmelyxy b';
const rows = 1;

let subEncodedText = encodedText.slice();

const lengthText = encodedText.length;
    let column = lengthText / rows;
    column = Math.round(column * 100) / 100;
    let a = [];
    let count = 0;
    let final_text = '';
    for (let i = 0; i < rows; i++) {
    a[i] = [];
    for (let j = 0; j < column; j++) {
        a[i][j] = encodedText[count + j];
    }
    count += column;
    }
    if(rows == 1){
        return 
    }
    const regex = /[abcdefghijklmnopqrstuvwxyz]/gi;
    let max = 0;
    for(let i = 0; i < rows;i++){
        let alphabet = 0;
        
        for(let j=0; j< column; j++){
            if((`${a[i][j]}`).match(regex)){
                alphabet++;
            }
        }
        if( alphabet > max){
            max = alphabet;
        }
    }
    for (let i = 0; i < max; i++) {
        for (let j = 0; j < rows ; j++){
            if(i+j == column -1 && a[j][i+j] == ' '){
                break;
            };
            if(a[j][i+j]){
                final_text += a[j][i+j];
            }
            
       
    }

    }
console.log(final_text)
console.log(a)


