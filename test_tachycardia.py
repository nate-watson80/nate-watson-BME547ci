import pytest
from tachycardia import is_tachycardia


@pytest.mark.parametrize("string_input,expected", [
    # Basic functionality - Everything spelled correctly
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


@pytest.mark.parametrize("string_input,expected", [
    # Enhanced functionality - One or two letters incorrect
    ("tachycarAic", True),  # One wrong letter
    ("tachycard1c", True),  # Letter is a number
    ("TABhyBarBic      ", False),  # Three wrong characters
    ("  tachycardiR", True),  # One wrong characters
    ("    MacHYcaFdic", True),  # Two wrong characters
])
def test2_is_tachycardia(string_input, expected):
    result = is_tachycardia(string_input)

    assert result == expected


@pytest.mark.parametrize("string_input,expected", [
    # Enhanced functionality - Check if letters are accidently omitted
    ("tahycadic", True),  # One letter omitted
    ("tachyardi", True),  # Two letters ommitted
    ("    aCHyardc ", False),  # Three letters ommitted
    ("    7ach6cari  ", False),  # Two ommitted letters and two wrong lets
    ("tachycrdic", True),  # Example provided
])
def test3_is_tachycardia(string_input, expected):
    result = is_tachycardia(string_input)

    assert result == expected
