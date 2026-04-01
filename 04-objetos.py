class Car:
    def __init__(self, marca, modelo, valor):
        self.marca = marca
        self.modelo = modelo
        self.valor = valor
        self.en_venta = True

    def vendido(self):
        if self.en_venta:
            self.en_venta = False  
            print(f"El carro {self.marca} {self.modelo} ya está vendido.")
        else:
            print(f"El carro {self.marca} no está en el mercado.")

    def return_car(self):
        self.en_venta = True
        print(f"El carro {self.marca} está de nuevo en venta.")


class Cliente:
    def __init__(self, nombre, celular):
        self.nombre = nombre
        self.celular = celular
        self.carros_comprados = []   

    def comprar_car(self, carro):
        if carro.en_venta:
            carro.vendido()
            self.carros_comprados.append(carro)
            print(f"{self.nombre} ha comprado el carro {carro.marca} {carro.modelo}.")
        else:
            print(f"El carro {carro.marca} {carro.modelo} no está disponible.")

    def return_carro(self, carro):
        if carro in self.carros_comprados:
            carro.return_car()
            self.carros_comprados.remove(carro)
            print(f"{self.nombre} devolvió el carro {carro.marca}.")
        else:
            print(f"El carro {carro.marca} no está en su lista de compras.")


class ListaDeCarros:
    def __init__(self):
        self.carros = []
        self.clientes = []

    def add_carro(self, carro):
        self.carros.append(carro)
        print(f"El carro {carro.marca} está en el mercado.")

    def registro_cliente(self, cliente):
        self.clientes.append(cliente)
        print(f"Hola señor {cliente.nombre}, bienvenido a nuestra agencia.")

    def carros_en_venta(self):
        print("Carros disponibles:")
        for carro in self.carros:
            if carro.en_venta:
                print(f"{carro.marca} {carro.modelo} por {carro.valor}")
carro1 = Car("Toyota", "Corolla", 20000)
carro2 = Car("Ferrari", "F8", 300000)

user1 = Cliente("Maicol", "002")

agencia = ListaDeCarros()

agencia.add_carro(carro1)
agencia.add_carro(carro2)

agencia.registro_cliente(user1)

agencia.carros_en_venta()

user1.comprar_car(carro1)

agencia.carros_en_venta()