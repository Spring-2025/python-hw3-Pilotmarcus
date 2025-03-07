import inspect
import pandas as pd
import numpy as np
import pytest

import WhoAmI_File
def test_WhoAmI():
    assert WhoAmI_File.WhoAmI() != ''


import YFinance_File
def test_YahooData2returns():
    d = {   'Open': [100, 102, 101, 103],
            'High': [105, 104, 103, 105],
            'Low': [98, 100, 99, 101],
            'Close': [101, 103, 102, 104],
            'Adj Close': [101, 103, 102, 104],
            'Volume': [1000, 1200, 900, 1100]}

    index = pd.to_datetime(['2023-10-26', '2023-10-27', '2023-10-28', '2023-10-29'])
    tempdata = pd.DataFrame(d, index=index)
    returns = YFinance_File.YahooData2returns(tempdata)
    assert np.isclose(returns[0],  0.01980198, atol=0.01)
    assert np.isclose(returns[1], -0.00970874, atol=0.01)
    assert np.isclose(returns[2],  0.01960784, atol=0.01)
    

