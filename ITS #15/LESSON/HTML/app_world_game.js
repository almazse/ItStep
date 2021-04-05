const words = ['top', 'temperature', 'word', 'collaboration', 'python', 'javascript']
const ind = Math.floor(Math.random() * words.length)
const word = words[ind]
let wordLenght = word.length

for (let i = 0; i < wordLenght; i++) {
	document.writeln("<div class='my-char'>" + word[i] + "</div>")
}

document.writeln("<button id='my-btn'>Enter character</button>")
const divs = document.getElementsByClassName('my-char')
const b1 = document.getElementById('my-btn')

b1.addEventListener('click', handler1)

function handler1() {
	let enteredChar = prompt("Your suggestion: ")
	if (word.includes(enteredChar)) {
		for (let i = 0; i < divs.length; i++) {
			if (enteredChar === word[i]) {
				divs[i].style.color = 'red'
			}
		}
		--wordLenght
	} else {
		alert('Such character doesn\'t exist in word')
	}

	if (wordLenght === 0) alert('WIN!')
}