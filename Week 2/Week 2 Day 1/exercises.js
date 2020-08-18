// //exercise1:
// var x = 12;
// var y = 11; 
// if (x > y) {
// 	document.write(x);
// }
// else if (y > x) {
// 	document.write(y);
// }
// else {
// 	document.write("x and y are equal")
// }
// // exercise 2:
// var newDog = "Chihuahua";
// 	console.log(newDog.length);
// console.log(newDog.toUpperCase());
// console.log(newDog.toLowerCase());
// if (newDog == "Chihuahua") {
// console.log("I LOVE Chihuahua, it's my favorite dog.");
// }
// else {
// 	console.log("I prefer CATS");
// }
//exercise 3:
// var num = parseInt(prompt("please enter a number: "));
// if (num % 2 == 0) {
// 	console.log("even number");
// }
// else {
// 	console.log("odd number");
// }
//exercise 4:
let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"];
let numUsers = users.length;
console.log(numUsers);
switch(numUsers) {
	case 0: console.log("no one is online");
	break; 
	case 1: console.log(users[0] + " is online."); 
	break;
	case 2: console.log(users[0] + " and " + users[1] + " are online." );
	break; 
	default: console.log(users[0] + ", " + users[1] + " and " + (numUsers - 2) + " more are online.");
	break;
}