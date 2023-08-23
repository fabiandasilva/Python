let valor1=  10;
let valor2= " casa";

const suma = (valor1, valor2) => {
    return valor1 + valor2;
}

if (valor1 === 10) {
    console.log("es igual a 10");
} else {
    console.log("no es igual a 10");
}


(valor1 === 10) ? console.log("es igual a 10") : console.log("no es igual a 10");


console.log("hola como estas" + suma(valor1, valor2));