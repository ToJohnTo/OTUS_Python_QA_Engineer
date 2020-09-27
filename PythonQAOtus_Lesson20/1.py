
from collections import Counter

arr = [1 , 1, 1, 2, 2, 3, 3, 3, 3, 3, 4,5]


a = Counter(arr)
print(a.most_common(3))