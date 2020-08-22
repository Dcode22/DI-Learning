var calcString = "";
var calcDisplay = document.getElementById("display");
// console.log(calcDisplay.innerHTML);
function my_f(btn) {
	// alert(btn);
	calcString = calcString+btn; 
	calcDisplay.innerHTML = calcString; 
	console.log(calcString);
}
function results() {
	var calcResult = eval(calcString);
	calcDisplay.innerHTML = calcResult; 
	console.log(calcString + "=" + calcResult);
	calcString = calcResult;
}

function calcClear() {
	calcString = "";
	calcDisplay.innerHTML = 0;

}
function backSpace() {
	if (calcDisplay.innerHTML.length > 1) {
      
	calcDisplay.innerHTML = calcDisplay.innerHTML.slice(0, -1);
	}
	else {
		calcString = "";
		calcDisplay.innerHTML = 0;
	}
	console.log(calcDisplay.innerHTML);
	
}