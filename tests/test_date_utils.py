from datetime import datetime

from mizani._core.date_utils import (
    ceil_month,
    expand_datetime_limits,
    round_month,
    shift_limits_down,
)


def test_shift_limits_down():
    lo = (1973, 1998)
    lc = (1973, 2023)
    assert shift_limits_down(lc, lo, 10) == (1970, 2020)

    lo = (1973, 2021)
    lc = (1973, 2023)
    assert shift_limits_down(lc, lo, 10) == lc


def test_expand_datetime_limits():
    limits = (
        datetime(2000, 1, 1, microsecond=100),
        datetime(2000, 1, 1, microsecond=1300),
    )
    assert expand_datetime_limits(limits, 200, "microsecond") == limits


def test_ceil_month():
    d = datetime(2020, 1, 11)
    assert ceil_month(d) == datetime(2020, 2, 1)

    d = datetime(2020, 1, 1)
    assert ceil_month(d) == d


def test_round_month():
    d = datetime(2000, 4, 23)
    assert round_month(d) == datetime(2000, 5, 1)

    d = datetime(2000, 4, 14)
    assert round_month(d) == datetime(2000, 4, 1)
