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
get(clave) {
return this.#datos[clave];
}
}
const modelo = new Modelo();
const registro = [];
modelo.suscribir((k, v, a) => registro.push(`${k}: ${a === undefined ? "-" : a} =>
${v}`));
modelo.suscribir((k, v) => console.log(`[vista] ${k} = "${v}"`));
console.log(modelo.set("nombre", "Ana"));
console.log(modelo.set("nombre", "Ana"));
console.log(modelo.set("nombre", "Ana María"));
console.log(modelo.set("edad", 30));
console.log(registro.join(" | "));
console.log(modelo.get("apellido"));