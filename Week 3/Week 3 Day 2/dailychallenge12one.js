var div = document.querySelector("div");
console.log(div);
div.addEventListener('mouseover', one);
div.addEventListener('mouseout', two);
div.addEventListener('click', three);
div.addEventListener('dblclick', four);
div.addEventListener('fullscreenchange', five);
// div.addEventListener('keydown', six);
// div.addEventListener('keyup', seven);
// div.addEventListener('mousemove', eight);
// div.addEventListener('wheel', nine);


function one(){
	div.style.backgroundColor = "orange";

}
function two(){
	
	div.style.fontSize = "6em";
	div.style.backgroundColor = "green";


}
function three(){
	div.style.border = "pink 30px dashed";

}
function four(){
	
	div.style.borderRadius = "50%";
	div.style.fontSize = "4em";
}
function five(){
	div.innerHTML = "Full Screen!";

}
function six(){

}
function seven(){

}
function eight(){

}
function nine(){

}


