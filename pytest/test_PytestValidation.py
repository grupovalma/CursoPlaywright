#Fixtures, es para reutilizarse en todos los casos de pruebas.
import pytest


@pytest.fixture(scope="function")
def preWork():
    print("I setup browser instance")

#Necesita iniciar con test, si la clase tiene test inicialmente se puede ver una flecha al lado, sino no.
def test_initialCheck(preWork):
    print("This is first test")

def test_SecondCheck(preSetupWork):
    print("This is Second test")


#Notas:
## En el fixture(scope="function") function, significa que se va a correr siempre antes de todos los casos de prueba
## En el fixure (score="module") module, significa que el fixture solo se va a correr una sola vez.
## En el scope, tambien existe una funcion que se llama "class", y es para correrlo una sola vez como module.