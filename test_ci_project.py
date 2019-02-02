import pytest

# Unit test for basic function functionality:
@pytest.mark.parametrize("string_input,expected",[
    ("tachycardic", True),
    ("Tachycardic", True),
    (" tachycardic", True),
    ("tachycardic ", True),
    ("tachYcaRdic", True),

])
def test_is_tachycardia(string_input, expected):
    from tachycardia import is_tachycardia
    result = is_tachycardia(string_input)

    assert result == expected
