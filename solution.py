import pandas as pd
import numpy as np
from scipy.stats import anderson_ksamp

chat_id = 516575251 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    p_val = stats.anderson_ksamp([x, y])[2]
    alpha = 0.03
    return p_val <= alpha
