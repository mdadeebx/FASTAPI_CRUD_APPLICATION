import pytest


def test_equal_or_not_equal():
    assert 3 == 3
    assert 3 != 1

def test_is_instance():
    assert isinstance('this is a string',str)
    assert not isinstance('10',int)

def test_boolean():
    validated = True
    assert validated is True
    assert ('hello' == 'world') is False

def test_greater_and_less_than():
    assert 3 > 1
    assert 5 < 10

def test_list():
    num_list = [1,2,3,4,5]
    any_list = [False,False]
    assert 1 in num_list
    assert 7 not in num_list
    assert all(num_list)
    assert not any(any_list)


class Student:
    def __init__(self,name:str,age:int,major:str,years:int):
        self.name = name
        self.age = age
        self.major = major
        self.years = years

@pytest.fixture
def default_employee():
    return Student('John',22,'Computer Science',3)

def test_person_initialization(default_employee):
    assert default_employee.name == 'John'
    assert default_employee.age == 22
    assert default_employee.major == 'Computer Science'
    assert default_employee.years == 3

























