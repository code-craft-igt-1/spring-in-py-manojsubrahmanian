
import math

def calculateStats(numbers):
    if len(numbers) > 0:
        return {
            'avg': sum(numbers) / len(numbers),
            'min': min(numbers),
            'max': max(numbers)
        }
    return {
        'avg': math.nan,
        'min': math.nan,
        'max': math.nan
    }
