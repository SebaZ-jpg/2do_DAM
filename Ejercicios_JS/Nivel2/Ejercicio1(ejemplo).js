
/* ESTE ES EL EJERCICIO DEFINITIVO, NO MODIFICARLO. */

class PaginadorComponent {
    #pagina;
    constructor(inicial = 1, total = 4) {
        this.#pagina = inicial;
        this.maximo = total;
}

get pagina() {
    return this.#pagina;
}

siguiente() {
    if (this.#pagina < this.maximo) {
        this.#pagina++;
        return true;
}
return false;
}


render() {
    return `<nav>Página: ${this.#pagina}/${this.maximo}</nav>`;
}
}

const c = new PaginadorComponent(2);

console.log(c.render());
for (let i = 0; i < 3; i++) {
    const cambio = c.siguiente();
    console.log(`${cambio ? "avanza" : "se queda"} -> ${c.render()}`);
}

console.log(c.pagina);
console.log(typeof c.pagina);

