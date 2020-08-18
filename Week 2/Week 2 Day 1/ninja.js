 // console.log(5 >= 1); //true
 // console.log(0 === 1);//false
 //  console.log( 4 <= 1);//false
 //   console.log( 1 != 1); //false
 //    console.log("A" > "B"); //false
 //     console.log("B" < "C");//true
 //      console.log("a" > "A");//true
 //       console.log("b" < "A");//false
 //        console.log(true === false);//false
 //    	console.log(true != true);//false
 //    
  // let c;
  //   let a = 34;
  //   let b = 21;
  //   a = 2;
  //   console.log(a + b);
  //   console.log(c);
  //   console.log(3 + 4 + '5');
 //  var a = prompt("enter two numbers separated by a comma and a space: ")

 //  var asplit = a.split(", ");
 //  console.log(asplit);
 // alert(asplit[0] * asplit[1]);
//  Ask the user for a number, return a string of the word “Boom”, which varies in the following ways:
// The string should include n number of “o”s, unless n is below 2 (in that case, return “boom”).
// If n is evenly divisible by 2, add an exclamation mark to the end.
// If n is evenly divisible by 5, return the string in ALL CAPS.
// If n is evenly divisible by both 2 and 5, return the string in ALL CAPS and add an exclamation mark to the end.
// The example below should help clarify these instructions.
 var num = parseInt(prompt("enter a number: "));
 if (num < 2) {
	console.log("boom");
}
 else if ((num % 2 != 0) && (num % 5 != 0)) {

	console.log("b"+"o".repeat(num) +"m");
}
else if ((num % 2 == 0) && (num % 5 !=0)) {

	console.log("b"+"o".repeat(num) +"m!");
} 
else if ((num % 2 == 0) && (num % 5 == 0)) {
	console.log("B" + "O".repeat(num) + "M!");
}
else if ((num % 2 != 0) && (num % 5 == 0)) {
	console.log("B" + "O".repeat(num) + "M");
}
else {
	console.log("b" + "o".repeat(num) + "m");
}
