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
 * Complete the vowelsAndConsonants function.
 * Print your output using 'console.log()'.
 */
function vowelsAndConsonants(s) {
    let vowels = [];
    let consonants = [];
    let i;
    
    /* fill the arrays with the characteres */
    for (i = 0; i < s.length; i++) {
        if (s.charCodeAt(i) == 97 || s.charCodeAt(i) == 101 || s.charCodeAt(i) == 105 || s.charCodeAt(i) == 111 || s.charCodeAt(i) == 117) {
            vowels.push(s[i]);
        } else {
            consonants.push(s[i]);
        }
    }
    /* sort the arrays */
    vowels.sort();
    //consonants.sort();
    /* concat the arrays */
    let s_arranged = vowels.concat(consonants);
    /* print the result */
    let j;
    for (j = 0; j < s_arranged.length; j++) {
        console.log(s_arranged[j]);
    }
}


function main() {
    const s = readLine();
    
    vowelsAndConsonants(s);
}