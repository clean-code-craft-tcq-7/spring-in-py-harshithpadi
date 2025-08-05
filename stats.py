
def calculateStats(numbers):
  # implement the computation of statistics here and return the results
  stats = {}
  stats['avg'] = sum(numbers)/len(numbers)
  stats['min'] = min(numbers)
  stats['max'] = max(numbers)                                
  return None
