class Orilla:
    def __init__(self,cabra,col,lobo):
        self.cabra = cabra
        self.col = col
        self.lobo = lobo

    def getCabra(self):
        return self.cabra

    def getCol(self):
        return self.col

    def getLobo(self):
        return self.lobo

    def setCabra(self,cabra):
        self.cabra = cabra

    def setCol(self,col):
        self.col = col

    def setLobo(self,lobo):
        self.lobo = lobo

    def llevarCabra(self):
        self.setCabra(False)

    def llevarCol(self):
        self.setCol(False)

    def llevarLobo(self):
        self.setLobo(False)

    def traerCabra(self):
        self.setCabra(True)

    def traerCol(self):
        self.setCol(True)

    def traerLobo(self):
        self.setLobo(True)

    def mostrar(self, barca):
        # print(f"Lobo:{self.lobo}, Cabra:{self.cabra}, Col:{self.col}")
        orIzq = "\n\t"
        orDer = ""
        if self.getCabra():
            orIzq += " Cabra "
        else:
            orDer += " Cabra "

        if self.getLobo():
            orIzq += " Lobo "
        else:
            orDer += " Lobo "

        if self.getCol():
            orIzq += " Col "
        else:
            orDer += " Col "

        if barca:
            orIzq += " Pastor -\__/----"
        else:
            orDer = "----\__/- Pastor " + orDer + "\n"

        print(f"{orIzq+orDer}")