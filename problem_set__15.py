"""### Title: Merge Intervals

**Difficulty:** Medium

**Problem Statement:**  
Given a collection of intervals, merge all overlapping intervals and return the resulting list of intervals. An interval is defined by a start and an end value, and two intervals overlap if the start of one interval is less than or equal to the end of the other interval.

**Input Format:**  
- A list of tuples, where each tuple contains two integers representing the start and end of an interval.  
  Example: `[(1, 3), (2, 6), (8, 10), (15, 18)]`

**Output Format:**  
- A list of merged intervals, where each interval is represented as a tuple, and the intervals are sorted by their starting values.  
  Example: `[(1, 6), (8, 10), (15, 18)]`

**Constraints:**  
- The input list will have at least one interval.  
- The start and end of each interval will be non-negative integers.  
- The maximum number of intervals is 10^4.

**Example Test Cases:**

1. **Input:** `[(1, 3), (2, 6), (8, 10), (15, 18)]`  
   **Output:** `[(1, 6), (8, 10), (15, 18)]`

2. **Input:** `[(1, 4), (4, 5)]`  
   **Output:** `[(1, 5)]`

**Additional Notes:**  
- Consider how to handle intervals that do not overlap and how to sort them effectively before merging.
- Think about the time complexity of your approach and aim to achieve O(n log n) due to sorting, followed by a single pass to merge intervals."""


def merge_intervals(intervals: list) -> list:
    # Handle empty or single interval case
    if not intervals or len(intervals) == 1:
        return intervals
    
    # Sort intervals by start time
    intervals.sort()
    
    merged = [intervals[0]]  # Initialize with first interval
    
    for current in intervals[1:]:  # Start from second interval
        last_merged = merged[-1]  # Get the last merged interval
        
        # If current interval overlaps with last merged interval
        if current[0] <= last_merged[1]:
            # Update the end time of last merged interval if needed
            merged[-1] = (last_merged[0], max(last_merged[1], current[1]))
        else:
            # No overlap, add current interval to merged list
            merged.append(current)
    
    return merged