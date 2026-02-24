import pytest


@pytest.mark.benchmark
def test_sorting_performance():
    """Benchmark sorting a list of integers."""
    data = list(range(1000, 0, -1))
    sorted_data = sorted(data)
    assert sorted_data[0] == 1


def test_list_comprehension(benchmark):
    """Benchmark list comprehension performance."""

    def compute():
        return [x**2 for x in range(500)]

    result = benchmark(compute)
    assert len(result) == 500


def test_string_concatenation(benchmark):
    """Benchmark string join performance."""

    def build_string():
        return "".join(str(i) for i in range(500))

    result = benchmark(build_string)
    assert isinstance(result, str)


def test_dict_construction(benchmark):
    """Benchmark dictionary construction performance."""

    def build_dict():
        return {i: i * 2 for i in range(500)}

    result = benchmark(build_dict)
    assert len(result) == 500
