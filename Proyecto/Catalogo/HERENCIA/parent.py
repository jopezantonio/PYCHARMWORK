class Persona:
    def __init__(self, nombre, apellido, edad, nacionalidad, sexo):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.nacionalidad = nacionalidad
        self.sexo = sexo


class Empleado(Persona):
    def __init__(self, nombre, apellido, edad, nacionalidad, sexo, cargo, salario, antiguedad):
        super().__init__(nombre, apellido, edad, nacionalidad, sexo)
        self.cargo = cargo
        self.salario = salario
        self.antiguedad = antiguedad

    def __str__(self):
        return f"La persona se llama {self.nombre} {self.apellido}, tiene {self.edad} años de edad, es de nacionalidad {self.nacionalidad}, su sexo es {self.sexo}, su cargo es {self.cargo}, su sueldo es de {self.salario} y tiene {self.antiguedad} en la empresa"
