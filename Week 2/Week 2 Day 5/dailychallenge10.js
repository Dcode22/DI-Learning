var start = parseInt(prompt("Enter a number of bottles of beer on the wall to start: "));
console.log(start + " bottles of beer on the wall, " + start + " bottles of beer, take " + 1 + " down, pass it around, " + (start - 1) + " bottles of beer on the wall.")
console.log((start - 1) + " bottles of beer on the wall, " + (start - 1) + " bottles of beer, take " + 2 + " down, pass them around, " + (start - 3) + " bottles of beer on the wall.")
for (j = 3, i = (start - j); (i - j) >= 0; j++){
	console.log(i + " bottles of beer on the wall, " + i  + " bottles of beer, take " + j + " down, pass them around, " + (i-j) + " bottles of beer on the wall.");
	i = (i - j);
}
console.log("BLEEEEP! Game over fellers, ya'll drank too much! go buy more beer!")