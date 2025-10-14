class Libro:
    def __init__(self, titulo, autor, paginas, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.disponible = disponible

    def prestar(self):
        if self.disponible:
            self.disponible = False
            return f"El libro '{self.titulo}' ha sido prestado."
        else:
            return f"El libro '{self.titulo}' no está disponible actualmente, lo siento."

    def devolver(self):
        if not self.disponible:
            self.disponible = True
            return f"El libro '{self.titulo}' ha sido devuelto recientemente."
        else:
            return f"El libro '{self.titulo}' ya está disponible actualmente."

    def informacion(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"Título: {self.titulo}\nAutor: {self.autor}\nPáginas: {self.paginas}\nEstado: {estado}"


# --- PRUEBAS ---
libro1 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", 863)
libro2 = Libro("Crónicas de una muerte anunciada", "Gabriel García Márquez", 144)

print("=== Información inicial ===")
print(libro1.informacion())
print()
print(libro2.informacion())
print()

print("=== Préstamo de libros ===")
print(libro1.prestar())
print(libro2.prestar())
print()

print("=== Intento de préstamo repetido ===")
print(libro1.prestar())
print()

print("=== Después del préstamo ===")
print(libro1.informacion())
print()

print("=== Devolución de libros ===")
print(libro1.devolver())
print(libro2.devolver())
print()

print("=== Devolución repetida ===")
print(libro1.devolver())
print()

print("=== Información final ===")
print(libro1.informacion())
print()
print(libro2.informacion())
