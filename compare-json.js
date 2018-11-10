/* 
This program compares two json files...

usage example: 
node compare-json.js freq-1.json freq-2.json
*/

const file_1 = require(`./${process.argv[2]}`);
const file_2 = require(`./${process.argv[3]}`);

let diff_count = 0;

console.log(`The length of file 1 is ${file_1.length}`);
console.log(`The length of file 2 is ${file_2.length}`);

for (let i = 0; i < file_1.length; i++){
  if (file_1[i] !== file_2[i]){
    diff_count++;
  }
}

if (diff_count === 0){
  console.log('the files appear to be identical');
} else {
  console.log(`There appear to be ${diff_count} discrepancies between the files`);
  console.log(`That means ${100*diff_count/file_1.length}% is different`);
}
