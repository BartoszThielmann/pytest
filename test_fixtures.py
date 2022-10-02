import pytest

# Exercise 2

@pytest.fixture(scope='module')
def return_list():
    """Return example list"""
    return ['list_elem0','list_elem1','list_elem2']

@pytest.fixture()
def return_dictionary():
    """Return example dictionary"""
    return {'key0':'value0', 'key1':'value1', 'key2':'value2'}

@pytest.fixture()
def return_tuple():
    """Return example tuple"""
    return ('tuple_elem0','tuple_elem1', 'tuple_elem2')
    
# Exercise 3
    
def test_return_list(return_list):
    """Use fixture return value in a test"""
    assert return_list == ['list_elem0','list_elem1','list_elem2']
    
def test_return_dictionary(return_dictionary):
    """Use fixture return value in a test"""
    assert return_dictionary == {'key0':'value0', 'key1':'value1','key2':'value2'}
    
def test_return_tuple(return_tuple):
    """Use fixture return value in a test"""
    assert return_tuple == ('tuple_elem0','tuple_elem1', 'tuple_elem2')
    
# Exercise 4

def test_return_list_index_0(return_list):
    """Use same fixture in the first test"""
    assert return_list[0] == 'list_elem0'
    
def test_return_list_index_1(return_list):
    """Use same fixture in the first test"""
    assert return_list[1] == 'list_elem1'

