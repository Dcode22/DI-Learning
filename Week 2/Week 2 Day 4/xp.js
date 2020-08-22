// ex1
// let age = prompt("What is your age?");
// function checkid(age) {

// 	if (Number(age) < 18) {
// 	    alert("Sorry, you are too yound to drive this car. Powering off");
// 	} else if (Number(age) > 18) {
// 	    alert("Powering On. Enjoy the ride!");
// 	} else if (Number(age) === 18) {
// 	    alert("Congratulations on your first year of driving. Enjoy the ride!");
// 	}
// }
// checkid(age);
// ex2
// amazonBasket = {
//     glasses: 1,
//     books: 2,
//     floss: 100
// }
// function checkBasket() {
// 	var item = prompt("select an item: ");
// 	if (item in amazonBasket) {
// 		console.log("your item is in the basket");
// 	}
// 	else {
// 		console.log("your item is missing");
// 	}
// }
// checkBasket();


// // ex3
// function changeEnough (change, price) {

// 	// Quarters  = 0.25
// 	// Dimes = 0.10
// 	// Nickels = 0.5
// 	// Pennies = 0.01

// 	var sum = 0
// 	sum = (sum + change[0]*0.25 + change[1]*0.1 +change[2]*0.05 + change[3]*0.01)
// 	if (sum >= price) {
// 		alert("you got da dough");
// 	}

// 	else {
// 		alert("you d*** broke n****!")
// 	}
// }

// changeEnough([4,4,4,4], 1.63);


// ex4

var shoppingList = ["banana", "orange", "apple"];
let stock = { 
    "banana": 6, 
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}  

let prices = {    
    "banana": 4, 
    "apple": 2, 
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
} 
var sumofprices = 0
function myBill() {
	for(item of shoppingList) {
		if(stock[item] > 0) {
			sumofprices = sumofprices + prices[item];
		} 
	}
	return sumofprices; 
}
console.log(myBill());
