const pigeonhole_sort = (arr, n) => {
    let max = arr[0];
    let min = arr[0];
    let range, i, j, index;

    for(i =1; i<n; i++){
        if(arr[i] > max){
            max = arr[i]
        };
        if(arr[i] < min){
            min = arr[i];
        }
    }

    range = max - min + 1;
    let phole = [];
    index = 0;
    for(i =0; i< n; i++){
        phole[i] = 0;
    }
    for(i = 0; i< n; i++){
        phole[arr[i]- min]++;
    }
    for(j =0; j< range; j++){
        while(phole[j] > 0){
            arr[index++] = j + min;
            phole[j]--;
        }
    }
    return arr;
}

let arr = [8, 3, 2, 7, 4, 6, 8];
 
  
console.log(pigeonhole_sort(arr,arr.length))
      
    