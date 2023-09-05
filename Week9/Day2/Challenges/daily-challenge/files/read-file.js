const fs = require('fs');

function readFile() {
  const filePath = './files/file-data.txt';

  fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) {
      console.error('Error reading the file:', err);
    } else {
      console.log('File content:');
      console.log(data);
    }
  });
}

module.exports = readFile;
