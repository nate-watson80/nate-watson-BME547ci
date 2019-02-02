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
    ("tachyardic", True),
    ("tachycard1c", True),
    ("achycardIc", True),
    ("  TacHcard1c", True),
])
def test2_is_tachycardia(string_input, expected):
    result = is_tachycardia(string_input)

    assert result == expected
