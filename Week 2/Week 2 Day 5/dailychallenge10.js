var start = parseInt(prompt("Enter a number of bottles of beer on the wall to start: "));
console.log(start + " bottles of beer on the wall,\n "+ start + "bottles of beer,\ntake " + 1 + " down, pass it around,\n " + (start - 1) + "bottles of beer on the wall.");
console.log((start - 1) + " bottles of beer on the wall,\n " + (start - 1) + " bottles of beer, take " + 2 + " down, pass them around, " + (start - 3) + " bottles of beer on the wall.");
for (j = 3, i = (start - j); (i - j) >= 0; j++){
	console.log(i + " bottles of beer on the wall, " + i  + " bottles of beer, take " + j + " down, pass them around, " + (i-j) + " bottles of beer on the wall.");
	i = (i - j);
}
console.log("BLEEEEP! Game over fellers, ya'll drank too much! go buy more beer!")