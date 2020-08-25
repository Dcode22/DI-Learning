var input = document.createElement("input");
var div = document.getElementById("root");
div.appendChild(input);
var add = document.createElement("button");
var clearAll = document.createElement("button");
var numberOfItems = document.createElement("button");
div.appendChild(add);
div.appendChild(numberOfItems);
div.appendChild(clearAll);
add.innerHTML = "Add Item";
clearAll.innerHTML = "Clear All";
numberOfItems.innerHTML = "Number Of Items";


var list = document.createElement("ul");
div.appendChild(list);
function addItem(){
	if (input.value !== ""){
		var newItem = document.createElement("li");
		newItem.innerHTML = input.value;
		list.appendChild(newItem);
		input.value = ""; 
	}
	count();
}
add.addEventListener("click", addItem);
numberOfItems.addEventListener("click", count);
var cartCount = document.createElement("p");
function count(){
	div.appendChild(cartCount);
	var items = document.querySelectorAll('li').length;
	cartCount.innerHTML= "You have " +items+ " items in your cart.";
}
function clear(){
	allItems = document.querySelectorAll('li');
	console.log(allItems);
	for (i = 0; i<allItems.length; i ++) {
		allItems[i].remove();
	}
	count();
	
	
}
clearAll.addEventListener("click", clear);