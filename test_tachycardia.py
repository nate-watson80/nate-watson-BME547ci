import pytest


@pytest.mark.parametrize("string_input,expected", [  # Basic functionality
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
