import pytest

from exercise import Employee
@pytest.fixture
def employee():
    return Employee('jon', 'doe', 5000)
def test_give_default_raise(employee):
    employee.give_raise(0)
    assert employee.salary == 5000
def test_give_custom_raise(employee):
    employee.give_raise(2000)
    assert employee.salary == 7000