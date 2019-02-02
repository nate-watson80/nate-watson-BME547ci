import pytest
from tachycardia import is_tachycardia


@pytest.mark.parametrize("string_input,expected", [  # Basic functionality
    ("tachycardic", True),
    ("Tachycardic", True),
    (" tachycardic", True),
    ("tachycardic ", True),
    ("tachYcaRdic", True),
    ("          tachycardic", True),
    (1234, False),
    ("Wrong-word", False),
    ("%$#", False),
])
def test_is_tachycardia(string_input, expected):
    result = is_tachycardia(string_input)

    assert result == expected


@pytest.mark.parametrize("string_input,expected", [  # Enhanced functionality
    ("tachycarAic", True),  # One wrong letter
    ("tachycard1c", True),  # Letter is a number
    ("TABhyBarBic      ", False),  # Three wrong characters
    ("  tachycardiR", True),  # One wrong characters
    ("    aacHYcaFdic", True),  # Two wrong characters
])
def test2_is_tachycardia(string_input, expected):
    result = is_tachycardia(string_input)

    assert result == expected
