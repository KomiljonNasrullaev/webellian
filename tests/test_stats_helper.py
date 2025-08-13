import pandas as pd
from stats_helper.core import mean, median, mode

def test_mean_median_mode():
    df = pd.DataFrame({"x": [1, 2, 3, 4, 5]})
    assert mean(df, "x") == 3
    assert median(df, "x") == 3
    assert mode(df, "x") == [1, 2, 3, 4, 5]
