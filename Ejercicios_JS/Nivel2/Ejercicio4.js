class ServicioContactos {
  #contactos = [];

  añadir(nombre) {
    this.#contactos.push({ id: this.#contactos.length + 1, nombre });
  }

  listar() {
    return [...this.#contactos];
  }
}

class ServicioSimulado {
  listar() {
    return [{ id: 42, nombre: "contacto de prueba" }];
  }
}

class AgendaComponent {
  constructor(servicio) {
    this.servicio = servicio;
  }

  render() {
    const contactos = this.servicio.listar();
    if (contactos.length === 0) {
      return "Agenda vacía";
    }
    return contactos.map((c) => `#${c.id} ${c.nombre}`).join(" | ");
  }
}

const servicio = new ServicioContactos();
const real = new AgendaComponent(servicio);
console.log(real.render());

servicio.añadir("Lucía");
servicio.añadir("Pablo");
console.log(real.render());

const simulada = new AgendaComponent(new ServicioSimulado());
console.log(simulada.render());

const copia = servicio.listar();
copia.pop();
console.log(servicio.listar().length);