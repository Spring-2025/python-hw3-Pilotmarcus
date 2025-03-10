#should be good code
import numpy as np

def ES(losses, alpha=None, VaR=None, use_PnL=False):
    if VaR is None and alpha is not None:
        VaR = np.percentile(losses, 100 * alpha)

    es_value = np.mean(losses[losses > VaR])
    
    return es_value

