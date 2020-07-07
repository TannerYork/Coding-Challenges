# Merge Overlapping Intervals from CTI-ISP 2020 #

# Given a collection of intervals, merge all overlapping intervals.
# For example:
# Given [1,3],[2,6],[8,10],[15,18],
# return [1,6],[8,10],[15,18].
# Make sure the returned intervals are sorted.

def merge_overlapping_intervals(intervals):
  # Remove Intervals overlapping elements
  for i in range(len(intervals)-2):
    interval_comp_i = 1 if len(intervals[i]) > 1 else 0
    nxt_interval_comp_i = 0
    
    if int(intervals[i][interval_comp_i] - intervals[i+1][nxt_interval_comp_i]) == 1:
      intervals[i].pop(interval_comp_i)
      intervals[i+1].pop(nxt_interval_comp_i)
  
  # Remove empty intervals
  intervals = [interval for interval in intervals if len(interval) > 0]
  
  # Combine Single Intervals
  combined_intervals = []
  for i in range(len(intervals)-1):
    if len(intervals[i]) == 1 and len(intervals[i+1]) == 1:
        intervals[i].extend(intervals[i+1])
        combined_intervals.append(intervals[i])
    elif len(intervals[i]) == 2:
        combined_intervals.append(intervals[i])
  combined_intervals.append(intervals[len(intervals)-1])
  return combined_intervals


result = merge_overlapping_intervals([[1,3],[2,6],[8,10],[15,18]])
print(result)