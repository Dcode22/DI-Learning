var sentence = ('This dinner is not that bad!');
var array = sentence.split(" ");
console.log(array);
let notnum = array.indexOf("not");
console.log(notnum);
if (array[notnum + 1] != "bad!") {
	 console.log("bad dinner");
} 
else {
	console.log("bonapetit");
}
// var not = array.indexOf("not");
// var bad = array.indexOf("bad");
// console.log(not);
// console.log(bad);
// if (not < bad) {
// 	sentence = sentence.substr(0, not);
// 	console.log(sentence + "good");
// }
// else {
// 	console.log(sentence);
// }
// console.log(array.findIndex("dinner"));