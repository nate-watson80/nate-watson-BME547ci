import pytest

@pytest.mark.parametrize("string_input,expected",[
    ("tachycardia", True),
    ("Tachycardia", True),
    (" Tachycardia", True),
    ("tachycardia ", True),
    ("tachYcaRdia", True),

])
def test_is_tachycardia(string_input, expected):
from tachycardia import is_tachycardia

result = is_tachycardia(string_input)

assert result == expected
