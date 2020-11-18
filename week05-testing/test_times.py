from times import compute_overlap_time, time_range
import pytest

'''
def test_backwards_time_range():
    with pytest.raises(ValueError):
        time = time_range("2010-01-12 12:00:00", "2010-01-12 11:00:00")
'''

test_params = [(time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00"), time_range("2010-01-12 13:30:00", "2010-01-12 14:00:00"), []),

               (time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00", 2), time_range("2010-01-12 10:30:00", "2010-01-12 12:30:00", 2),
               [('2010-01-12 10:30:00', '2010-01-12 11:00:00'), ('2010-01-12 11:00:00', '2010-01-12 11:30:00'), ('2010-01-12 11:30:00', '2010-01-12 12:00:00')])]
               
@pytest.mark.parametrize("time_range1, time_range2, expected", test_params)
def test_times_parametrise(time_range1, time_range2, expected)

    result = compute_overlap_time(time_range1, time_range2)

    assert result == expected
