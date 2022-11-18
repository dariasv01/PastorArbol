class Arbol:
    def __init__(self,padre, estado):
        self.padre = padre
        self.estado = estado
        self.hijos = []


    def getEstado(self):
        return self.estado

    def setEstado(self, estado):
        self.estado = estado

    def getPadre(self):
        return self.padre

    def setPadre(self, padre):
        self.padre = padre

    def getHijos(self):
        return self.hijos

    def setHijos(self, hijos):
        self.hijos = hijos

    def mostrar(self):
        if (self.padre != None):
            self.padre.mostrar()
        print(f"\n<<<<<<<<<<<<\tNodo a Desarrollar\t>>>>>>>>>>>>")
        self.estado[0].mostrar(self.getEstado()[1])
        if len(self.getHijos()) != 0:
            print(f"\nN hijos: {len(self.getHijos())}")
            for item in self.getHijos():
                item.estado[0].mostrar(not self.getEstado()[1])
        else:
            print(f"\n\t\t\t\tEste es el resultado\n")
        print(f"<<<<<<<<<<<<\t\t\t\t\t\t>>>>>>>>>>>>\n")

    def mostrarOrilla(self):
        if (self.padre != None):
            self.padre.mostrarOrilla()

        print(f"\nN hijos: {len(self.getHijos())}")
        print(f"Canibales: {self.estado[0].nCanibal}\nMisioneros: {self.estado[0].nMisioneros}\nBarca:{self.estado[1]}")