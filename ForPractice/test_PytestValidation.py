import pytest

@pytest.fixture(scope="module")
def preWork():
    print("I setup module Instance")
    return "pass"

@pytest.fixture(scope="function")
def secondWork():
    print("I setup2 module Instance")
    yield
    print("tear down validation")

def test_InitialCheck(preWork, secondWork):
    print("This is first test")
    assert preWork == "pass"

def test_SecondCheck(preSetupWork, secondWork):
    print("This is Second test")