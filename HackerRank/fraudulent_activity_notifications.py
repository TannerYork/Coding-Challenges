# Fraudulent Activity Notifications from HackerRank #


# Attempt 3: Single Count Sort and Cumulative Frequency Implementation (Accepted)
def calc_twice_mean(counts, d):
    """Calculates the mean of the given sorted list"""
    count_freq = list(counts)
    for i in range(1, len(count_freq)):
        count_freq[i] += count_freq[i-1]
    
    a, b = 0, 0    
    if d % 2 == 0:
        first = d//2
        second = first + 1
    
        for i in range(201):
            if first <= count_freq[i]:
                a = i
                break
        for i in range(201):
            if second <= count_freq[i]:
                b = i
                break
    else:
        first = d//2+1
        for i in range(201):
            if first <= count_freq[i]:
                a = 2 * i
                break
    return a + b
                
# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    counts = [0] * 201
    for i in range(d):
        counts[expenditure[i]] += 1
        
    alerts = 0
    for i in range(d, len(expenditure)):
        median = calc_twice_mean(counts, d) 
        if expenditure[i] >= median:
            alerts += 1
            
        counts[expenditure[i-d]] -= 1
        counts[expenditure[i]] += 1
    return alerts


# Attempt 2: Single Sort Queue Array Implementation (Not Fast Enough)
# def calc_mean(n, lst):
#     """Calculates the mean of the given sorted list"""
#     if n % 2 != 0:
#         return (lst[n // 2] + lst[(n // 2) - 1]) // 2
#     return lst[n // 2]

# # Complete the activityNotifications function below.
# def activityNotifications(expenditure, d):
#     # Inialize, fill, and sort the trailing day queue
#     queue = []
#     for i in range(d):
#         queue.append(expenditure[i])
#     queue = sorted(queue)
                   
#     # Get the sorted index to add the next price
#     num_notif = 0
#     for i in range(d, len(expenditure) - 1):
#         if expenditure[i] >= calc_mean(d, queue) * 2:
#             num_notif += 1
            
#         index = d - 1
#         for j in range(d):
#             price = expenditure[i]
#             if price < queue[j] and j == 0:
#                 index = j 
#             elif price < queue[j] and price > queue[j - 1]:
#                 index = j
    
#         queue.pop(0)
#         queue.insert(index, expenditure[i])
#     return num_notif


# Attempt 1: Multi Sort Queue Array Implementation (Not Fast Enough) 
# def calc_mean(n, lst):
#     """Calculates the mean of the given sorted list"""
#     sorted_lst = sorted(lst)
#     if n % 2 != 0:
#         return (sorted_lst[n // 2] + sorted_lst[(n // 2) - 1]) // 2
#     return sorted_lst[n // 2]

# # Complete the activityNotifications function below.
# def activityNotifications(expenditure, d):
#     # Inialize, fill, and sort the trailing day queue
#     queue = []
#     for i in range(d):
#         queue.append(expenditure[i])
                   
#     # Get the sorted index to add the next price
#     num_notif = 0
#     for i in range(d, len(expenditure) - 1):
#         if expenditure[i] >= calc_mean(d, queue) * 2:
#             num_notif += 1
#         queue.append(expenditure[i])
#         queue.pop(0)
#     return num_notif

if __name__ == '__main__':
    print(activityNotifications([2, 3, 4, 2, 3, 6, 8, 4, 5], 5), 2)
    print(activityNotifications([1, 2, 3, 4, 4], 4), 0)
    print(activityNotifications([10, 20, 30, 40, 50], 3), 1)