// Don't forget to npm install the node_modules

jP([167, 1256, 996, 70000, 88]);

function jP(values) {
    for (let n of values) {
        console.log("Additive Persistence of " + n + ": " + aP(n));
    }
    for (let n of values) {
        console.log("Multiplicative Persistence of " + n + ": " + mP(n));
    }
}

function aP(n) {
    let count = 0;
    while (n.toString().length > 1) {
        n = n.toString().split("").reduce((a, b) => parseInt(a) + parseInt(b));
        count++;
    }
    return count;
}

function mP(n) {
    let count = 0;
    while (n.toString().length > 1) {
        n = n.toString().split("").reduce((a, b) => parseInt(a) * parseInt(b));
        count++;
    }
    return count;
}