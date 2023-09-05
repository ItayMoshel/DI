const chalk = require('chalk');

function displayColorfulMessage() {
    console.log(chalk.blue('The message is in blue color!'));
}

module.exports = displayColorfulMessage;