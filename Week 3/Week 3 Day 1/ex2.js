var firstUl = document.getElementsByTagName("ul")[0];
var secondUl = document.getElementsByTagName("ul")[1];
var nameChange = firstUl.lastElementChild;
nameChange.innerHTML = "Richard";
console.log(firstUl.lastElementChild.innerHTML);
firstUl.firstElementChild.innerHTML = "Dovid";
secondUl.firstElementChild.innerHTML = "Dovid";
var li1 = document.createElement("li");
var li2 = document.createElement("li");
li1.innerHTML = "Hey Students";
li2.innerHTML = "Hey Students";
firstUl.appendChild(li1);
secondUl.appendChild(li2);

secondUl.childNodes[3].remove();
var list = document.querySelectorAll("ul");
console.log(list);
for (var i = 0; i < list.length; i++) {
	list[i].classList.add("student_list");
	}
list[0].classList.add("university", "attendance");
console.log(list[0]);