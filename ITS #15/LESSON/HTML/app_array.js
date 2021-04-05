// Arrays

const carsArray = ['VW', 'BMW', 'Mercedes', 'Honda']

console.log(carsArray)
console.log(typeof carsArray)
console.dir(carsArray)

carsArray.push('Acura') // add element to the end of array
carsArray.unshift('Seat') // add element to the start of array

const lastElement = carsArray.pop() // remove last elemen from array
const firsElement = carsArray.shift() // remove first elemen from array

const carsReversedArray = carsArray.reverse()
const thirdElement = carsArray[2]