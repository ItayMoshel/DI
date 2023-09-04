const fs = require('fs');

function readFile(filename, callback) {
    fs.readFile(filename, 'utf8', (err, data) => {
      if (err) {
        callback(err, null);
        return;
      }
      callback(null, data);
    });
  }
  
  // Write content to a specified file
  function writeFile(filename, content, callback) {
    fs.writeFile(filename, content, 'utf8', (err) => {
      if (err) {
        callback(err);
        return;
      }
      callback(null);
    });
  }
  
  module.exports = { readFile, writeFile };
