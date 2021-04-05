// Function
// Function declaration

function doWork() {
	console.log('Yes, I do!')
}

doWork()

// Function expression

const greet2 = function greet2() {console.log('Great!')}

greet2()

// console.log(typeof doWork)
// console.dir(doWork)

// Anonymous function

// let counter  = 0
// const interval = setInterval(function() {console.log(++counter)}, 1000)

// Arrow function
const arrow = () => {console.log('Hi, I am arrow function')}
arrow()

// Default parameters

// const sum = (a = 40, b = a * 2) => console.log(a + b)
// sum()

// function summAll (...all) {
// 	let result = 0
// 	for (let num of all) {
// 		result += num
// 	}
// 	return result
// }

// const res = summAll(1, 2, 3, 4, 5, 6 ,7 , 8)
// console.log(res)

function createMember (name) {
	return function(lastName) {
		console.log(name + ' ' + lastName)
	}
}

const member = createMember('Oleh')
// member('Perlovskiy')