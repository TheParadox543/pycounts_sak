from pycount_sak.pycount_sak import count_words
from pycount_sak.datasets import get_flatland
from collections import Counter

def test_count_words():
    """Test word counting from a file."""
    expected = Counter({'insanity': 1, 'is': 1, 'doing': 1,
                        'the': 1, 'same': 1, 'thing': 1,
                        'over': 2, 'and': 2, 'expecting': 1,
                        'different': 1, 'results': 1})
    actual = count_words("tests/einstein.txt")
    assert actual == expected, "Einstein quote counted incorrectly!"

def test_count_flatland():
    """Test flatland function."""
    expected = Counter({'to': 3, 'call': 2, 'i': 1, 'our': 1,
                        'world': 1, 'flatland': 1, 'not': 1,
                        'because': 1, 'we': 1, 'it': 1, 'so': 1,
                        'but': 1, 'make': 1, 'its': 1, 'nature': 1,
                        'clearer': 1, 'you': 1, 'my': 1, 'happy': 1,
                        'readers': 1, 'who': 1, 'are': 1,
                        'privileged': 1, 'live': 1, 'in': 1,
                        'space': 1})
    actual = count_words(get_flatland())
    assert actual == expected, "Flatland quote counted incorrectly!"