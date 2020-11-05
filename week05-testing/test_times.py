from times import compute_overlap_time, time_range
import pytest

def test_no_overlap():
    time1 = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    time2 = time_range("2010-01-12 13:30:00", "2010-01-12 14:00:00")

    result = compute_overlap_time(time1, time2)
    expectation = None

    assert result == expectation

def test_several_time_ranges():
    time1 = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00", 2)
    time2 = time_range("2010-01-12 10:30:00", "2010-01-12 12:30:00", 2)

    #10:30-11:00,  11:00-11:30, 11:30-12:00

    result = compute_overlap_time(time1, time2)
    expectation = [('2010-01-12 10:30:00', '2010-01-12 11:00:00'), ('2010-01-12 11:00:00', '2010-01-12 11:30:00'), ('2010-01-12 11:30:00', '2010-01-12 12:00:00')]

    assert result == expectation

def test_backwards_time_range():
    with pytest.raises(ValueError):
        time = time_range("2010-01-12 12:00:00", "2010-01-12 11:00:00")