const arr = [5,0,9,1,7,4,2,6,3,8];
function bubble_Sort(arr)
{
    var swapp;
    var n = arr.length-1;
    console.log(n);
    var x=arr;
    do {
        swapp = false;
        for (var i=0; i < n; i++)
        {
            if (x[i] < x[i+1])
            {
               var temp = x[i];
               x[i] = x[i+1];
               x[i+1] = temp;
               swapp = true;
            }
        }
        n--;
    } while (swapp);
 return x; 
}

var sortedArray = bubble_Sort(arr);
console.log(sortedArray);
// console.log(sortedArray.toString());
console.log(sortedArray.join(" "));