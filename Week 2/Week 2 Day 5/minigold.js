word = prompt("Player 1: Enter a word of at least 8 letters: ");
if (word.length < 8) {
	word = prompt("try again: ");
}

var asterik = "*"
letter = prompt("word = " + asterik.repeat(word.length) + "   Player 2: guess a letter:");
word.substring(0, word.indexOf(letter))



// if (word.search(letter) >= 0) {
// 	prompt("word = " + asterik.repeat(word.substring(0, word.indexOf(letter).length) + letter + asterik.repeat(word.length() - (word.indexOf(letter) + 1)) + " guess another letter: ");
// }
