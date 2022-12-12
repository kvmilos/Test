from homework import take_from_list, calculate
import pytest

@pytest.mark.parametrize("i", ['a',"abc",[[1],[2]],1.0])
def test_take_from_list_type(i):
    with pytest.raises(ValueError, match=f"Indices should be integer or list of integers, not {type(i)}"):
        take_from_list([1,2,3],i)

def test_take_from_list_int():
    assert take_from_list([1,2,3],0) == [1]

def test_take_from_list_list():
    assert take_from_list([1,2,3],[0,2]) == [1,3]

def test_calculateab(tmp_path):
    f = tmp_path / "testing-homework/output.json"
    f.parent.mkdir()
    f.touch()
    with pytest.raises(FileNotFoundError, match="No such file or directory: 'a.txt'"):
        calculate("a.txt", f)


def test_calculateio(tmp_path):
    fo = tmp_path / "testing-homework/output.json"
    fo.parent.mkdir()
    fo.touch()
    calculate("input.json", fo)
