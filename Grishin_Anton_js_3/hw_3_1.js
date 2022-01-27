let i = 0;
while (i <= 100) {
    if (isPrime(i)) {
        console.log(i)
    }
    i += 1
}

function isPrime(num) {
    if (num < 2) {
        return False
    }

    for (let i = 2; i < num; i++) {
        if (num % i === 0) {
            return False
        }
    }
    return True

}