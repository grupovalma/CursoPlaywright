#Fixtures, es para reutilizarse en todos los casos de pruebas.
import pytest


@pytest.fixture(scope="module")
def preWork():
    print("I setup browser instance")
    return "pass"

@pytest.fixture(scope="function")
def secondWork():
    print("I setup secondWork instance")
    yield
    print("Tear Down Validation")

#Necesita iniciar con test, si la clase tiene test inicialmente se puede ver una flecha al lado, sino no.
def test_initialCheck(preWork, secondWork):
    print("This is first test")
    assert preWork == "pass"

#@pytest.mark.skip ##Funcion skip, pytest no lo corre.
def test_SecondCheck(preSetupWork, secondWork):
    print("This is Second test")


#Notas:
## En el fixture(scope="function") function, significa que se va a correr siempre antes de todos los casos de prueba
## En el fixure (score="module") module, significa que el fixture solo se va a correr una sola vez.
## En el scope, tambien existe una funcion que se llama "class", y es para correrlo una sola vez como module.