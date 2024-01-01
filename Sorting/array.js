function bubbleSort(arr){
    let n = arr.length
    for (let i=0; i < n; i++) {
        for (let j = 0; j < n-i-1; j++ ) {
            if (arr[j] > arr[j+1]) {
                arr[j] = arr.splice(j+1, 1, arr[j])[0];
            }
        }
    }
    return arr 
}


function selectionSort(arr){
    for (let i = 0; i<arr.length; i++){
        min_index = i
        for (let j = i+1; j<arr.length; j++) {
            if arr[j]< arr[min_index] {
                min_index = j
            }
        }
        arr[j] = arr.splice(j+1, 1, arr[j])[0]; // fix this
    }
    return arr
}