from collections import Counter
from matplotlib.container import BarContainer

from pycount_sak.datasets import get_flatland
from pycount_sak.plotting import plot_words
from pycount_sak.pycount_sak import count_words
from pytest import raises

def test_count_words():
    """Test word counting from a file."""
    expected = Counter({'insanity': 1, 'is': 1, 'doing': 1,
                        'the': 1, 'same': 1, 'thing': 1,
                        'over': 2, 'and': 2, 'expecting': 1,
                        'different': 1, 'results': 1})
    actual = count_words("tests/einstein.txt")
    assert actual == expected, "Einstein quote counted incorrectly!"

# def test_count_flatland():
#     """Test flatland function."""
#     expected = Counter({'to': 3, 'call': 2, 'i': 1, 'our': 1,
#                         'world': 1, 'flatland': 1, 'not': 1,
#                         'because': 1, 'we': 1, 'it': 1, 'so': 1,
#                         'but': 1, 'make': 1, 'its': 1, 'nature': 1,
#                         'clearer': 1, 'you': 1, 'my': 1, 'happy': 1,
#                         'readers': 1, 'who': 1, 'are': 1,
#                         'privileged': 1, 'live': 1, 'in': 1,
#                         'space': 1})
#     actual = count_words(get_flatland())
#     assert actual == expected, "Flatland quote counted incorrectly!"

def test_plot_words():
    """Test plotting of word counts."""
    counts = Counter({'insanity': 1, 'is': 1, 'doing': 1,
                    'the': 1, 'same': 1, 'thing': 1,
                    'over': 2, 'and': 2, 'expecting': 1,
                    'different': 1, 'results': 1})
    fig = plot_words(counts)
    assert isinstance(fig, BarContainer), "Wrong plot type"
    assert len(fig.datavalues) == 10, "Incorrect number of bars plotted"

def test_plot_words_error():
    """Check TypeError raised when Counter not used."""
    with raises(TypeError):
        list_object = ["Pythons", "are", "not", "venomous"]
        plot_words(list_object)

def test_integration():
    """Test count_words() and plot_words workflow."""
    counts = count_words("tests/einstein.txt")
    fig = plot_words(counts)
    assert isinstance(fig, BarContainer), "Wrong plot type"
    assert len(fig.datavalues) == 10, "Incorrect number of bars plotted"
    assert max(fig.datavalues) == 2, "Highest word count should be 2"

def test_regression():
    """Regression test for Flatland."""
    top_word = count_words(get_flatland()).most_common(1)
    assert top_word[0][0] == "the", "Most common word is not 'the'"
    assert top_word[0][1] == 2276, "'the' count has changed"