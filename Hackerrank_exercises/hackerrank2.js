'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();    
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Complete the reverseString function
 * Use console.log() to print to stdout.
 */
function reverseString(s) {
    try {
        // Step 1. Use the split() method to return a new array
        let splitString = s.split("");
    
        // Step 2. Use the reverse() method to reverse the new created array
        let reverseArray = splitString.reverse();
    
        // Step 3. Use the join() method to join all elements of the array into a string
        let joinArray = reverseArray.join("");
        
        //Step 4. Return the reversed string
        console.log(joinArray);
    }
    catch {
        console.log("s.split is not a function");
        console.log(s);
    }
}


function main() {
    const s = eval(readLine());
    
    reverseString(s);
}