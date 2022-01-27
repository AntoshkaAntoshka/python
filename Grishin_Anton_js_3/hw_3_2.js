const cart = [
    ['Футболка', 999],
    ['Джинсы', 7900],
    ['Кроссовки', 10990],
];

const total = getTotalPrice(cart);
console.log(total);

function getTotalPrice() {
    let result = 0;
    for (let item of cart) {
        result += item[1]
    }
    return result
}