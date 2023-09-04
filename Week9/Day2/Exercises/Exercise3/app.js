const { readFile, writeFile } = require('./fileManager');

readFile('HelloWorld.txt', (readErr, content) => {
  if (readErr) {
    console.error('Error reading file:', readErr);
    return;
  }

  writeFile('ByeWorld.txt', 'Writing to the file', (writeErr) => {
    if (writeErr) {
      console.error('Error writing to file:', writeErr);
      return;
    }
    console.log('File writing successful!');
  });
});