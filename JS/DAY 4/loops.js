// for loop

// EXAMPLE 1: print 1 to 5
//   for (let i = 1; i <= 5; i++) {
//       console.log(i);
//   }
//   // 1 2 3 4 5

// EXAMPLE 2: print 5 to 1 (decrement)
//   for (let i = 5; i >= 1; i--) {
//       console.log(i);
//   }
//   // 5 4 3 2 1

// EXAMPLE 3: step of 2 (even numbers)
//   for (let i = 2; i <= 10; i += 2) {
//       console.log(i);
//   }
//   // 2 4 6 8 10

// EXAMPLE 4: sum of numbers 1 to 10
//   let sum = 0;
//   for (let i = 1; i <= 10; i++) {
//       sum += i;
//   }
//   console.log("Sum = " + sum);     // Sum = 55

// EXAMPLE 5: multiplication table
//   let n = 7;
//   for (let i = 1; i <= 10; i++) {
//       console.log(n + " x " + i + " = " + n * i);
//   }

// EXAMPLE 6: loop through an array using the index
//   let fruits = ["apple", "banana", "mango"];
//   for (let i = 0; i < fruits.length; i++) {
//       console.log(i + ": " + fruits[i]);
//   }

//while


// EXAMPLE 1: basic
//   let i = 1;
//   while (i <= 5) {
//       console.log(i);
//       i++;
//   }

// EXAMPLE 2: count digits of a number
//   let n = 12345, count = 0;
//   while (n > 0) {
//       n = Math.floor(n / 10);
//       count++;
//   }
//   console.log(count);              // 5

// EXAMPLE 3: sum of digits
//   let num = 1234, sum = 0;
//   while (num > 0) {
//       sum += num % 10;
//       num = Math.floor(num / 10);
//   }
//   console.log(sum);                // 10

// EXAMPLE 4: reverse a number
//   let x = 1234, rev = 0;
//   while (x > 0) {
//       rev = rev * 10 + (x % 10);
//       x = Math.floor(x / 10);
//   }
//   console.log(rev);                // 4321

// EXAMPLE 5: keep asking until valid input
//   let age = Number(prompt("Enter age (1-100)"));
//   while (age < 1 || age > 100 || isNaN(age)) {
//       age = Number(prompt("Invalid. Enter age (1-100)"));
//   }
//   console.log("Age accepted: " + age);

// EXAMPLE 6: halving until 1 (unknown number of steps)
//   let value = 100, steps = 0;
//   while (value > 1) {
//       value = value / 2;
//       steps++;
//   }
//   console.log(steps);              // 7

// EXAMPLE 7: body does not run if condition is false at the start
//   let k = 10;
//   while (k < 5) {
//       console.log("never prints");
//   }

//do while


// EXAMPLE 1: basic
//   let i = 1;
//   do {
//       console.log(i);
//       i++;
//   } while (i <= 5);
//   // 1 2 3 4 5

// EXAMPLE 2: runs once even if condition is false
//   let x = 10;
//   do {
//       console.log("x = " + x);
//       x++;
//   } while (x < 5);
//   // x = 10

// EXAMPLE 3: menu that repeats
//   let choice;
//   do {
//       choice = prompt("1. Hello  2. Bye  3. Exit");
//       if (choice === "1") alert("Hello!");
//       else if (choice === "2") alert("Bye!");
//   } while (choice !== "3");

// EXAMPLE 4: PIN check
//   let pin;
//   do {
//       pin = prompt("Enter PIN");
//   } while (pin !== "1234");
//   alert("Access granted");
