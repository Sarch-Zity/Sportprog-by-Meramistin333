const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
  });
  
  readline.question("Enter a number:", (number) => {
    const result = number * number;
    console.log("The square of " + number + " is " + result);
    readline.close();
  });