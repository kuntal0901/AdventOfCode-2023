const fs = require('fs');

let input;
try {
    let input = fs.readFileSync('input.txt', 'utf-8');

    const ranges = input.split(',');
    let result = 0
    ranges.forEach(range => {
        let [start, end] = range.split('-');
        
        for(let i = parseInt(start); i<= parseInt(end);i++){
            const string_i = i.toString()
            const n = string_i.length
            let computed_str = ""

            if(n%2 == 0){
                for(let j = 1; j<= Math.floor(n/2);j++){
                    // console.log(string_i,j,string_i.substring(0,j))
                    computed_str = string_i.substring(0,j).repeat(Math.floor(n/j))
                    // console.log("computed_str", computed_str, string_i)
                    if(computed_str === string_i){
                        console.log("Found -> ", computed_str,string_i)
                        result += i
                        break;
                    }
                } 
            }
            else {
                for(let j = 1; j<= Math.floor(n/2);j+=2){
                    // console.log(string_i,j,string_i.substring(0,j))
                    computed_str = string_i.substring(0,j).repeat(Math.floor(n/j))
                    // console.log("computed_str", computed_str, string_i)
                    if(computed_str === string_i){
                        console.log("Found -> ", computed_str,string_i)
                        result += i
                        break;
                    }
                } 
            }
        }
    });

    console.log("the number of invalid pids->", result);
} catch (err) {
    console.error('Error reading file:', err);
}
