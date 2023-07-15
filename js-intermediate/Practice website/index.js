// var made = 40;
// var spent = 65;

// function dailyBattle(){
//     console.log("Today I made $" + made)
//     console.log("Today I spent $" + spent)
//     var totalMoney = made - spent

//     if (totalMoney >= 0){
//         console.log("Total money for today $" + totalMoney)
//         console.log("I won today's battle.")
//     }
//     if (totalMoney < 0){
//         totalMoney = totalMoney * -1
//         console.log("Total money for today - $" + totalMoney)
//         console.log("I failed today's battle.")
//     }
// }


// random

// var randomNumb = Math.round((Math.random()) * 100);

// console.log(randomNumb)

// randomize numbers from 1 to 6
// var random1to6 = Math.ceil(Math.random() * 6)
// console.log(random1to6)

// var random1to6 = Math.floor(Math.random() * 6);
// console.log(random1to6)

// var random1to6 = Math.round(Math.random() * 6);
// console.log(random1to6)


// randomize score from 0 to 100 with if/else and else if
// var score = Math.floor(Math.random() * 101);
// console.log(score)

// if (score < 50) {
//     console.log("I failed the exam :( .")
// }
// else if (score < 75) {
//     console.log("I passed the exam with average mark.")
// }
// else {
//     console.log("I passed the exam with a great mark :D .")
// }


// function with output
// make a prompt for first and second number
// function multiply(a , b) {
//     return a * b
// }

// var firstNumb = prompt("Enter your first number: ")
// var secondtNumb = prompt("Enter your second number: ")

// console.log(firstNumb)
// console.log(secondtNumb)
// alert("The answer is " + multiply(firstNumb, secondtNumb))
// console.log(multiply(firstNumb, secondtNumb))


// Array ->
// list
// var friends = ["jim", "luna", "tom"];

// console.log(friends.includes("luna"))

// var friends = ["jim", "luna", "tom"];
// var userName = prompt("Enter your name: ");
// console.log(userName);

// if (friends.includes(userName)) {
//     console.log("You can view the content.");
// } else {
//     console.log("You don't have access.");
// }

//  updating the array
// var friends = ["jim", "luna", "tom"]
// friends[2] = "jerry"
// console.log(friends)
// friends.push("tom")
// console.log(friends)
// friends.pop()
// friends.pop()
// console.log(friends)
// friends.unshift("jerry", "tom")
// console.log(friends)
// friends.shift()
// console.log(friends)


// pomodoro
// var breaktime = [];
// var count = 1;

// function pomodoro() {
//     if (count < 4) {
//         console.log(count)
//         breaktime.push(5);
//         count += 1;
//         console.log(breaktime)
//     }
//     else {
//         console.log(count)
//         breaktime.push(15);
//         count = 1;
//         console.log(breaktime)
//     }
// }

// better solution
// var breaktime = []
// var count = 1;

// function pomodoro() {
//     if (count % 4) {
//         breaktime.push(5);
//     }
//     else {
//         breaktime.push(15);
//     }
//     count++;
//     console.log(breaktime)
// }

//  add while loop into pomodoro
// var breaktime = []
// var count = 1;

// function pomodoro() {
//     if (count % 4) {
//         breaktime.push(5);
//     }
//     else {
//         breaktime.push(15);
//     }
//     count++;
// }

// while (count < 13) {
//     pomodoro();
// }

// for loop
// for (var counter = 1; counter<13; counter++) {
//     pomodoro();
// }

// console.log(breaktime)


//  exercise find even numbers
// var numbers = [ 13, 23, 12, 45, 22, 48, 66, 100, 1, 2, 3]

// function findEven() {
//     for (var i = 0; i < numbers.length; i++) {
//         if (!(numbers[i] % 2)) {
//             console.log(numbers[i])
//         }
//     }
// }

// findEven()

// special array, if every even and odd index is even and odd number respectively
var arr = [0, 1, 3, 3, 4, 5, 8]

function isSpecialArray(arr) {
    for (var i = 0; i < arr.length; i++) {
        if (arr[i] % 2 == i % 2) {
            continue
        }
        else {
            return false
        }
    }
    return true
}

console.log(isSpecialArray(arr))
