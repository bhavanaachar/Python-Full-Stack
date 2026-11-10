
// 1. NAMED FUNCTION
// A function that has a name.

function add(a, b) {
    return a + b;
}

console.log("1. Named Function:");
console.log(add(10, 20)); 
// Output: 30



// 2. ANONYMOUS FUNCTION
// A function without a name, stored in a variable.

const multiply = function(a, b) {
    return a * b;
};

console.log("2. Anonymous Function:");
console.log(multiply(5, 4));
// Output: 20



// 3. ARROW FUNCTION
// A shorter way of writing a function.

const square = (n) => {
    return n * n;
};

console.log("3. Arrow Function:");
console.log(square(5));
// Output: 25

// Arrow function with implicit return
const subtract = (a, b) => a - b;

console.log(subtract(20, 10));
// Output: 10



// 4. CALLBACK FUNCTION
// A function passed as an argument to another function.

function greet(name, callback) {
    console.log("Hello " + name);
    callback();
}

function message() {
    console.log("Welcome to JavaScript!");
}

console.log("4. Callback Function:");
greet("Ravi", message);

// Output:
// Hello Ravi
// Welcome to JavaScript!



// 5. HIGHER-ORDER FUNCTION (HOF)
// A function that accepts another function
// as an argument or returns another function.

// Example 1: Accepting a function as argument

function calculate(a, b, operation) {
    return operation(a, b);
}

console.log("5. Higher-Order Function:");

console.log(calculate(10, 5, (x, y) => x + y));
// Output: 15

console.log(calculate(10, 5, (x, y) => x * y));
// Output: 50


// Example 2: Returning a function

function multiplier(factor) {
    return function(number) {
        return number * factor;
    };
}

const double = multiplier(2);

console.log(double(5));
// Output: 10



// ==========================================
// BUILT-IN HIGHER-ORDER ARRAY FUNCTIONS
// ==========================================

let numbers = [1, 2, 3, 4, 5, 6];


// 1. map() - Returns a new array after modification

console.log("Map:");
console.log(numbers.map(n => n * 2));
// Output: [2, 4, 6, 8, 10, 12]


// 2. filter() - Returns elements satisfying a condition

console.log("Filter:");
console.log(numbers.filter(n => n % 2 === 0));
// Output: [2, 4, 6]


// 3. reduce() - Reduces array into a single value

console.log("Reduce:");
console.log(numbers.reduce((sum, n) => sum + n, 0));
// Output: 21


// 4. forEach() - Executes a function for each element

console.log("ForEach:");
numbers.forEach(n => console.log(n));

// Output:
// 1
// 2
// 3
// 4
// 5
// 6


// 5. find() - Returns the first matching element

console.log("Find:");
console.log(numbers.find(n => n > 3));
// Output: 4


// 6. some() - Checks whether at least one element passes

console.log("Some:");
console.log(numbers.some(n => n > 5));
// Output: true


// 7. every() - Checks whether all elements pass

console.log("Every:");
console.log(numbers.every(n => n > 0));
// Output: true


// 8. sort() - Sorts array elements

let nums = [40, 10, 30, 20];

console.log("Sort:");
console.log(nums.sort((a, b) => a - b));
// Output: [10, 20, 30, 40]
