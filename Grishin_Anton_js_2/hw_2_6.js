/* Реализовать функцию с тремя параметрами: function mathOperation(arg1, arg2, operation), где arg1, arg2 — значения аргументов, operation — строка с названием операции. В зависимости от переданного значения выполнить одну из арифметических операций (использовать функции из пункта 5) и вернуть полученное значение (применить switch). */

function mathOperation(x, y, operation) {
    switch (operation) {
        case 'сложение':
            return x + y;
            break;
        case 'вычитание':
            return x - y;
            break;
        case 'умножение':
            return x * y;
            break;
        case 'деление':
            return x / y;
            break;
    }
}

var a = 2
var b = 4
mathOperation(a, b, 'сложение') // 6