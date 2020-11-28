// https://leetcode.com/problems/happy-number/

function happyNumber(number) {
    let original_number = number;
    while (number !== 1) {
        let stringNumber = number.toString();
        number = 0;
        for (char of stringNumber) {
            number += parseInt(char) ** 2;
        }
        if (number == original_number) {
            return false;
        }
    }
    return true;
}

console.log(happyNumber(20));
