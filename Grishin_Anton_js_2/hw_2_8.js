/* Задача 8: С помощью рекурсии организовать функцию возведения числа в степень. Формат: function power(val, pow), где val — заданное число, pow –— степень. */

function pow(x, n) {
    if (n != 1) {
        return x *= pow(x, n - 1);
    } else {
        return x;
    }
}
alert(pow(2, 3)); // 8