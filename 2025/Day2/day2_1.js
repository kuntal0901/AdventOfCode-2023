const fs = require('fs');

let input;
try {
    let input = fs.readFileSync('input.txt', 'utf-8');

    const ranges = input.split(',');
    let result = 0
    ranges.forEach(range => {
        let [start, end] = range.split('-');
        if (start.length % 2 !== 0 && end.length % 2 !== 0) {
            result += 0
        }
        else {
            for(let i = parseInt(start); i<= parseInt(end);i++){
                const string_i = i.toString()
                if(string_i.length%2 == 0){
                    if(string_i.substring(0,string_i.length/2) === string_i.substring(string_i.length/2, string_i.length)){
                        result += i
                    }
                }
            }
        }
    });

    console.log("the number of times the dial is left pointing at 0 after any rotation in the sequence ->", result);
} catch (err) {
    console.error('Error reading file:', err);
}
