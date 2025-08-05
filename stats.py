import math

def calculateStats(numbers):
  # implement the computation of statistics here and return the results
  stats = {}
  if numbers:
    stats['avg'] = sum(numbers)/len(numbers)
    stats['min'] = min(numbers)
    stats['max'] = max(numbers)
  else:
    stats['avg'] = float('nan')
    stats['min'] = float('nan')
    stats['max'] = float('nan')
  return stats
