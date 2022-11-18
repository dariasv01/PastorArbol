import Model.Arbol as ar
import Model.Orilla as ori

def checkEstadoDec(estadoAct, estadoHis):
    if ((estadoAct[0][0] is not estadoAct[0][1]) and (estadoAct[0][0] is not estadoAct[0][2])) \
            or ((estadoAct[0][0] == estadoAct[0][1] == estadoAct[1])
                or (estadoAct[0][0] == estadoAct[0][2] == estadoAct[1])):
        if estadoAct not in estadoHis:
            return True
    return False

nodo = ar.Arbol(None, [ori.Orilla(True, True, True), True])
nodos = [nodo]
orIzq = ori.Orilla(True, True, True)
estadoHis = [[[orIzq.getCabra(), orIzq.getCol(), orIzq.getLobo()], True]]

while (nodos[0].getEstado()[0].getCabra() or nodos[0].getEstado()[0].getCol() or nodos[0].getEstado()[
    0].getLobo()) and len(nodos) > 0:

    nodosHijos = []
    barca = nodos[0].getEstado()[1]
    cabra = nodos[0].getEstado()[0].getCabra()
    col = nodos[0].getEstado()[0].getCol()
    lobo = nodos[0].getEstado()[0].getLobo()
    orIzq.setCol(nodos[0].getEstado()[0].getCol())
    orIzq.setCabra(nodos[0].getEstado()[0].getCabra())
    orIzq.setLobo(nodos[0].getEstado()[0].getLobo())
    if barca:
        posicion = not barca
        if cabra:
            orIzq.llevarCabra()
            if checkEstadoDec([[orIzq.getCabra(), orIzq.getCol(), orIzq.getLobo()], posicion], estadoHis):
                nodos.append(ar.Arbol(nodo, [ori.Orilla(orIzq.getCabra(), orIzq.getCol(), orIzq.getLobo()), posicion]))
                nodosHijos.append(
                    ar.Arbol(nodo, [ori.Orilla(orIzq.getCabra(), orIzq.getCol(), orIzq.getLobo()), posicion]))
                estadoHis.append([[orIzq.getCabra(), orIzq.getCol(), orIzq.getLobo()], posicion])
            orIzq.cabra = cabra
            orIzq.col = col
            orIzq.lobo = lobo
        if col:
            orIzq.llevarCol()
            if checkEstadoDec([[orIzq.getCabra(), orIzq.getCol(), orIzq.getLobo()], posicion], estadoHis):
                nodos.append(ar.Arbol(nodo, [ori.Orilla(orIzq.getCabra(), orIzq.getCol(), orIzq.getLobo()), posicion]))
                nodosHijos.append(
                    ar.Arbol(nodo, [ori.Orilla(orIzq.getCabra(), orIzq.getCol(), orIzq.getLobo()), posicion]))
                estadoHis.append([[orIzq.getCabra(), orIzq.getCol(), orIzq.getLobo()], posicion])
            orIzq.cabra = cabra
            orIzq.col = col
            orIzq.lobo = lobo
        if lobo:
            orIzq.llevarLobo()
            if checkEstadoDec([[orIzq.getCabra(), orIzq.getCol(), orIzq.getLobo()], posicion], estadoHis):
                nodos.append(ar.Arbol(nodo, [ori.Orilla(orIzq.getCabra(), orIzq.getCol(), orIzq.getLobo()), posicion]))
                nodosHijos.append(
                    ar.Arbol(nodo, [ori.Orilla(orIzq.getCabra(), orIzq.getCol(), orIzq.getLobo()), posicion]))
                estadoHis.append([[orIzq.getCabra(), orIzq.getCol(), orIzq.getLobo()], posicion])
            orIzq.cabra = cabra
            orIzq.col = col
            orIzq.lobo = lobo
    else:
        posicion = not barca
        if checkEstadoDec([[orIzq.getCabra(), orIzq.getCol(), orIzq.getLobo()], posicion], estadoHis):
            nodos.append(ar.Arbol(nodo, [ori.Orilla(orIzq.getCabra(), orIzq.getCol(), orIzq.getLobo()), posicion]))
            nodosHijos.append(ar.Arbol(nodo, [ori.Orilla(orIzq.getCabra(), orIzq.getCol(), orIzq.getLobo()), posicion]))
            estadoHis.append([[orIzq.getCabra(), orIzq.getCol(), orIzq.getLobo()], posicion])
        if not cabra:
            orIzq.traerCabra()
            if checkEstadoDec([[orIzq.getCabra(), orIzq.getCol(), orIzq.getLobo()], posicion], estadoHis):
                nodos.append(ar.Arbol(nodo, [ori.Orilla(orIzq.getCabra(), orIzq.getCol(), orIzq.getLobo()), posicion]))
                nodosHijos.append(
                    ar.Arbol(nodo, [ori.Orilla(orIzq.getCabra(), orIzq.getCol(), orIzq.getLobo()), posicion]))
                estadoHis.append([[orIzq.getCabra(), orIzq.getCol(), orIzq.getLobo()], posicion])
            orIzq.cabra = cabra
            orIzq.col = col
            orIzq.lobo = lobo
        if not col:
            orIzq.traerCol()
            if checkEstadoDec([[orIzq.getCabra(), orIzq.getCol(), orIzq.getLobo()], posicion], estadoHis):
                nodos.append(ar.Arbol(nodo, [ori.Orilla(orIzq.getCabra(), orIzq.getCol(), orIzq.getLobo()), posicion]))
                nodosHijos.append(
                    ar.Arbol(nodo, [ori.Orilla(orIzq.getCabra(), orIzq.getCol(), orIzq.getLobo()), posicion]))
                estadoHis.append([[orIzq.getCabra(), orIzq.getCol(), orIzq.getLobo()], posicion])
            orIzq.cabra = cabra
            orIzq.col = col
            orIzq.lobo = lobo
        if not lobo:
            orIzq.traerLobo()
            if checkEstadoDec([[orIzq.getCabra(), orIzq.getCol(), orIzq.getLobo()], posicion], estadoHis):
                nodos.append(ar.Arbol(nodo, [ori.Orilla(orIzq.getCabra(), orIzq.getCol(), orIzq.getLobo()), posicion]))
                nodosHijos.append(
                    ar.Arbol(nodo, [ori.Orilla(orIzq.getCabra(), orIzq.getCol(), orIzq.getLobo()), posicion]))
                estadoHis.append([[orIzq.getCabra(), orIzq.getCol(), orIzq.getLobo()], posicion])
            orIzq.cabra = cabra
            orIzq.col = col
            orIzq.lobo = lobo
    # orIzq.mostrar(barca)
    nodos.pop(0)
    nodo.setHijos(nodosHijos)
    nodo = nodos[0]

nodo.mostrar()
