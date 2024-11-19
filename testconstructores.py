from televisores.TV import TV
from televisores.marca import Marca
from televisores.Control import Control


def testConstructorMarca():

    marca = Marca("Semsung")

    assert True, "Hay un problema con el constructor de Marca"


def testConstructorTV():

    marca = Marca("Xiomi")

    tv = TV(marca, True)

    assert True, "Hay un problema con el constructor de TV"


def testConstructorControl():

    control = Control()

    assert True, "Hay un problema con el constructor por defecto de Control"
