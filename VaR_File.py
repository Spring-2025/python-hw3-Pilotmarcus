import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def VaR(r,confidence,principal=1):
  
  var_percentile=np.percentile(r,(1-confidence)*100)
  VaR_value=abs(var_percentile)*principal
  return VaR_value

def percent_var(r,confidence):
  
  plt.hist(r,bins=50,alpha=0.75)
  plt.show()

  out=np.percentile(r,(1-confidence)*100)
  return abs(out)
