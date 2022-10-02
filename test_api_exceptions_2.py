"""Test for expected exceptions from using the API wrong."""

import pytest
import tasks
from tasks import Task

# The following tests are examples from the book (my tests are below)

def test_add_raises():
    """add() should raise an exception with wrong type param."""
    with pytest.raises(TypeError):
        tasks.add(task='not a Task object')


@pytest.mark.smoke
def test_list_raises():
    """list() should raise an exception with wrong type param."""
    with pytest.raises(TypeError):
        tasks.list_tasks(owner=123)


@pytest.mark.get
@pytest.mark.smoke
def test_get_raises():
    """get() should raise an exception with wrong type param."""
    with pytest.raises(TypeError):
        tasks.get(task_id='123')


class TestUpdate():
    """Test expected exceptions with tasks.update()."""

    def test_bad_id(self):
        """A non-int id should raise an excption."""
        with pytest.raises(TypeError):
            tasks.update(task_id={'dict instead': 1},
                         task=tasks.Task())

    def test_bad_task(self):
        """A non-Task task should raise an excption."""
        with pytest.raises(TypeError):
            tasks.update(task_id=1, task='not a task')


def test_delete_raises():
    """delete() should raise an exception with wrong type param."""
    with pytest.raises(TypeError):
        tasks.delete(task_id=(1, 2, 3))


def test_start_tasks_db_raises():
    """Make sure unsupported db raises an exception."""
    with pytest.raises(ValueError) as excinfo:
        tasks.start_tasks_db('some/great/path', 'mysql')
    exception_msg = excinfo.value.args[0]
    assert exception_msg == "db_type must be a 'tiny' or 'mongo'"
    
    
# The following tests are written by me 

@pytest.mark.mine
def test_add_with_id_raises():
    """add() should raise an exeption if attempt to add task with set id"""
    with pytest.raises(ValueError):
        new_task = Task('breathe', 'BRIAN', True, 1)
        tasks.add(new_task)
 
@pytest.mark.mine
def test_add_summary_not_string_raises():
    """add() should raise an exeption if summary is not string type"""
    with pytest.raises(ValueError):
        new_task = Task(5, 'BRIAN', True)
        tasks.add(new_task)
        
@pytest.mark.mine
def test_add_task_owner_raises():
    """add() should raise an exeption if task owner is not string or None"""
    with pytest.raises(ValueError):
        new_task = Task('breathe', 5, True)
        tasks.add(new_task)
