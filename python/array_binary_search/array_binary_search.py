


def binary_search(arr, x):
  low = 0
  high = len(arr) - 1
  mid = 0

  while low <= high:
    mid = (high + mid) // 2

    if arr[mid] < x:
      low = mid + 1

    elif arr[mid] > x:
      high = mid - 1

    else:
      return mid or -1
  # return -1  
