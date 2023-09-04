const products = require("./products");

function findProductByName(productName) {
    const product = products.find((p) => p.name === productName);
    return product;
}

console.log('Product 1:', findProductByName('Product 1'));
console.log('Product 2:', findProductByName('Product 2'));
console.log('Product 3:', findProductByName('Product 3'));
