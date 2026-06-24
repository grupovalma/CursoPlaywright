import pytest


@pytest.fixture(scope="function")
def preSetupWork():
    print("I setup browser instance")


### Notas: Quitamos el @pytest fixture del test1PytestValidation, y usamos conftest.py, para hacerlo global.
### scope="session" : Corre una sola vez, en el total de los casos de prueba, module lo hace pero solo dentro de un archivo de pruebas. Este en total.
### Como ahora conftest.py se usa en el total de los casos de prueba.

