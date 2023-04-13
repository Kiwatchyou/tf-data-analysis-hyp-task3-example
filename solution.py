import pandas as pd
import numpy as np
import scipy.stats as stats



chat_id = 390760498 


def solution(x: np.array, y: np.array) -> bool: 
    
    return stats.ttest_ind(x, y)[1] < 0.03 
