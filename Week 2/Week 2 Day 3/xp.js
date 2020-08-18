// ex1

// var colors = ["platinum", "gold", "silver", "copper"];
// for (var i=0; i < colors.length; i++) {
// 	console.log("My #" + (i+1) + " choice is " + colors[i]);
// }
// // ex2 
// let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"]
// let	namesSort = names.sort();
// console.log(namesSort);
// var finalName = "";

// for (i=0 ; i<namesSort.length ; i++){
//     finalName = finalName+namesSort[i].charAt(0); 
// }
// console.log(finalName);



// // ex3 
// var num = prompt("enter a number: ");

// while (num < 10) {
// 	num = prompt("enter a number: ")
// }


// ex4
let people = ["Greg", "Mary", "Devon", "James"];

for (i = 0; i < people.length; i++) {
	console.log(people[i]);
}

people.shift();
console.log(people);
people[2] = "Jason";
console.log(people);
people.push("Dovid");
console.log(people);
for (i = -1; i < 1; i++) {
	console.log(people[i]);
	
}