function completar(plantilla, datos) {
    let resultado = "";
    let i = 0;

    while (i < plantilla.length) {
        const inicio = plantilla.indexOf("{{", i);
        if (inicio === -1) {
            resultado += plantilla.slice(i);
            break;
        }

        const fin = plantilla.indexOf("}}", inicio);
        if (fin === -1) {
            resultado += plantilla.slice(i);
            break;
        }

        resultado += plantilla.slice(i, inicio);
        const clave = plantilla.slice(inicio + 2, fin).trim();
        const valor = datos[clave];
        resultado += valor ?? "" ;
        i = fin + 2;
    }

    return resultado;
}

const datos = { usuario: "Marcos", avisos: 7, equipo: null };

console.log(completar("<p>Hola {{ usuario }}</p>", datos));
console.log(completar("Avisos: {{avisos}} | Equipo: [{{ equipo }}] | Extra: [{{ zona }}]", datos));
console.log(completar("Texto fijo", datos));
