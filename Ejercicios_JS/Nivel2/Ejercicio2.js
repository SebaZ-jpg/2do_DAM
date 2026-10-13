class Almacen {
#datos = {};

#oyentes = [];
observar(fn) {
this.#oyentes.push(fn);
}
set(clave, valor) {
if (this.#datos[clave] === valor) return false;
const anterior = this.#datos[clave];
this.#datos[clave] = valor;
for (const fn of this.#oyentes) fn(clave, valor, anterior);
return true;
}

leer(clave) {
return this.#datos[clave];
}
}
const modelo = new Almacen();
const registro = [];
modelo.observar((k, v, a) => registro.push(`${k}: ${a === undefined ? "-" : a} =>
${v}`));
modelo.observar((k, v) => console.log(`[vista] ${k} = "${v}"`));
console.log(Almacen.set("tema", "claro"));
console.log(Almacen.set("tema", "claro"));
console.log(Almacen.set("tema", "oscuro"));
console.log(Almacen.set("fuenten", 14));
console.log(bitacora.join(" | "));
console.log(Almacen.leer("idioma"));