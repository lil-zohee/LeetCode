// https://leetcode.com/problems/palindrome-number/

function palindromeNumber(number) {
    let reverseNumber = '';
    number = number.toString();
    for (let i = number.length - 1; i > -1; i--) {
        reverseNumber += number[i];
    }
    console.log(reverseNumber);
    return number === reverseNumber;
}

console.log(palindromeNumber(1234321));
console.log(palindromeNumber(4569874));
