// https://leetcode.com/problems/roman-to-integer/

function romanToInteger(romanNum) {
    let number = 0;
    let i = 0;
    const romanNumValues = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000};
    const specialNums = {'I': ['V', 'X'], 'X': ['L', 'C'], 'C': ['D', 'M']};
    while (i < romanNum.length) {
        if (i < romanNum.length - 1) {
            if (Object.keys(specialNums).includes(romanNum[i]) && specialNums[romanNum[i]].includes(romanNum[i + 1])) {
                number += romanNumValues[romanNum[i + 1]] - romanNumValues[romanNum[i]];
                i += 2;
                continue;
            }
        }
        number += romanNumValues[romanNum[i]];
        i++;
    }
    return number;
}

console.log(romanToInteger('III'));
console.log(romanToInteger('IV'));
console.log(romanToInteger('IX'));
console.log(romanToInteger('LVIII'));
console.log(romanToInteger('MCMXCIV'));
