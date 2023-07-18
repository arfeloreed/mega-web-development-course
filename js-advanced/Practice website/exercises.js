// How Much is True?
// Create a function that returns the number of true values there are in an array.

// Examples:

// countTrue([true, false, false, true, false]) ➞ 2
 
// countTrue([false, false, false, false]) ➞ 0
 
// countTrue([]) ➞ 0

// function countTrue(arr) {
//     // add your code below this line:
//         var count = 0;
//         for (var i = 0; i < arr.length; i++) {
//             if (arr[i] == true) {
//                 count += 1;
//             }
//         }
//         // console.log(count);
//         return count
//     // add your code above this line:
//     }
// var arr1 = [true, false, false, true, false];
// var arr2 = [false, false, false, false];
// var arr3 = [false, true, true, true, false];


// [Medium] Fibonacci Sequence
// Objective

// The main objective of this exercise is to write a program that generates the first n numbers of the Fibonacci sequence.

// Instructions

// Write a program that performs the following tasks:

// Define a function fibonacci that takes an integer n as an argument and returns an array of the first n numbers of the Fibonacci sequence.

// The Fibonacci sequence is defined as follows: the first two numbers are 0 and 1, and each subsequent number is the sum of the two preceding numbers. For example, the first 10 numbers of the Fibonacci sequence are 0, 1, 1, 2, 3, 5, 8, 13, 21, and 34.

// If n is less than or equal to 0, return an empty array.

// Print the resulting array to the console.

// Input
// const n = 10;

// function fibonacci(n) {
//     var arr = [];
//     for (var i = 0; i < n; i++) {
//         if (arr.length < 2) {
//             arr.push(i);
//         }
//         else {
//             arr.push(arr[arr.length - 2] + arr[arr.length - 1]);
//         }
//     }
//     return arr
// }

// // Output
// console.log(fibonacci(n)); // Prints "[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]" to the console



// [Hard] Counting Vowels and Consonants
// Objective

// The main objective of this exercise is to write a program that counts the number of vowels and consonants in a given string.

// Instructions

// Write a program that performs the following tasks:

// Define a function countVowelsAndConsonants that takes a string as an argument and returns an object with two properties: vowels and consonants. The value of each property is the number of vowels and consonants in the string, respectively.

// A vowel is any of the following letters: 'a', 'e', 'i', 'o', 'u'. A consonant is any letter that is not a vowel.

// The program should ignore case, so both uppercase and lowercase vowels and consonants should be counted.

// Print the resulting object to the console.

// Input
const str = 'The quick brown fox jumps over the lazy dog';
var str1 = str.toLowerCase();
var vowelsArr = ["a", "e", "i", "o", "u"];

function countVowelsAndConsonants(str) {
    var vowels = 0;
    var consonants = 0;
    
    for (var i = 0; i < str1.length; i++) {
        if (vowelsArr.includes(str1[i])) {
            vowels++;
        }
        else if (str1[i] == " ") {
            continue
        }
        else {
            consonants++;
        }
    }
    return {"vowels": vowels, "consonants": consonants};
}
// Output
console.log(countVowelsAndConsonants(str)); // Prints "{vowels: 11, consonants: 24}" to the console
