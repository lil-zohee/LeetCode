// https://leetcode.com/problems/reverse-integer/

function reverseInteger(number) {
    let reverseNum = '';
    number = number.toString();
    if (number[0] === '-') {
        reverseNum = '-';
        number = number.replace('-', '');
    }
    for (let i = number.length - 1; i > -1; i--) {
        reverseNum += number[i];
    }
    reverseNum = parseInt(reverseNum);
    if (reverseNum < -2147483648 || reverseNum > 2147483647) {
        return 0;
    }
    return reverseNum;
}

console.log(reverseInteger(-120));
