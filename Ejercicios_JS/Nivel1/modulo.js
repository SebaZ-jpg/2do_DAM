const ajustes = {
    modulo: "Login",
    version: 3,
    habilitado: false,
    descripcion: null,
    etiqueta: undefined
}

for (const clave of ["modulo", "version", "habilitado", "descripcion", "etiqueta"])
{
    const valor = ajustes[clave];
    const texto = valor ?? "(sin valor)";
    const tipo = typeof valor;

    console.log(`${clave}: ${texto} -> ${tipo}`);

}

console.log(`${ajustes.version == "3"}`);
console.log(`${ajustes.version == "3"}`);