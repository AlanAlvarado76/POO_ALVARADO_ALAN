class Persona: #Clase principal
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def describir(self):
        return f"{self.nombre}, {self.edad} años"

class Estudiante(Persona):#Clases derivadas de la clase persona (Herencia)
    def __init__(self, nombre, edad, matricula):
        super().__init__(nombre, edad)
        self.matricula = matricula #Atributos

    def describir(self): #Metodos
        return f"Estudiante: {self.nombre}, {self.edad} años, Matrícula: {self.matricula}"

class Profesor(Persona):
    def __init__(self, nombre, edad, asignatura):
        super().__init__(nombre, edad)
        self.asignatura = asignatura #Atributos

    def describir(self):#Metodos
        return f"Profesor: {self.nombre}, {self.edad} años, Asignatura: {self.asignatura}"
    
class Curso: #Agregacion
    def __init__(self, nombre):
        self.nombre = nombre
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)
    
    def describir(self):
        descripcion = f"Curso: {self.nombre}\n"
        for estudiante in self.estudiantes:
            descripcion += f"- {estudiante.describir()}\n"
        return descripcion
    
class Escuela: #Composicion
    def __init__(self, nombre):
        self.nombre = nombre
        self.cursos = []
    
    def agregar_curso(self, curso):
        self.cursos.append(curso)
    
    def describir(self):
        descripcion = f"Escuela: {self.nombre}\n"
        for curso in self.cursos:
            descripcion += f"{curso.describir()}\n"
        return descripcion

class Asignacion:#Asociacion
    def __init__(self, profesor, curso):
        self.profesor = profesor
        self.curso = curso

    def describir(self):
        return f"{self.profesor.describir()} enseña el curso {self.curso.nombre}"
    

# Crear personas
estudiante1 = Estudiante("Ana", 20, "A123")
estudiante2 = Estudiante("Luis", 22, "B456")
profesor1 = Profesor("Carlos", 45, "Matemáticas")

# Crear cursos y agregar estudiantes (Agregación)
curso1 = Curso("Matemáticas")
curso1.agregar_estudiante(estudiante1)
curso1.agregar_estudiante(estudiante2)

# Crear escuela y agregar cursos (Composición)
escuela = Escuela("Escuela de Ciencias")
escuela.agregar_curso(curso1)

# Crear asignación (Asociación)
asignacion = Asignacion(profesor1, curso1)

# Describir todo
print(escuela.describir())
print(asignacion.describir())







