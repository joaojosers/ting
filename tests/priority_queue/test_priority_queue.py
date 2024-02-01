from ting_file_management.priority_queue import PriorityQueue
import pytest

# def test_basic_priority_queueing():
#     """Aqui irá sua implementação"""


def test_basic_priority_queueing():
    prefer = PriorityQueue()
    assert len(prefer) == 0
    prefer.enqueue({"qtd_linhas": 1})
    assert len(prefer) == 1
    prefer.enqueue({"qtd_linhas": 6})
    assert len(prefer) == 2
    prefer.enqueue({"qtd_linhas": 7})
    assert len(prefer) == 3
    prefer.enqueue({"qtd_linhas": 4})
    assert len(prefer) == 4
    elem_fila = prefer.dequeue()
    assert elem_fila == {"qtd_linhas": 1}
    assert len(prefer) == 3
    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        prefer.search(5)
    elem_search = prefer.search(2)
    assert elem_search == {"qtd_linhas": 7}
