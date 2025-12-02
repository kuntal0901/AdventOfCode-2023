const fs = require('fs');

let input;
try {
    input = fs.readFileSync('input.txt', 'utf-8');

    const directions = input.split('\n');
    let current_pos = 50;
    let result_0 = 0;
    directions.forEach(direction => {
        let distance = parseInt(direction.slice(1));
        distance = distance % 100;
        if (direction.startsWith('L')) {
            if (current_pos - distance < 0) {
                current_pos = 100 - (distance - current_pos) % 100;
            } else {
                current_pos = current_pos - distance;
            }
        } else {
            current_pos = (current_pos + distance) % 100;
        }
        if (current_pos == 0) {
            result_0 += 1;
        }
    });
    console.log("the number of times the dial is left pointing at 0 after any rotation in the sequence ->", result_0);
} catch (err) {
    console.error('Error reading file:', err);
}
