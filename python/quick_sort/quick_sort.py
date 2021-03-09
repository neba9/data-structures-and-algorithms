
def quick_sort(arr, left, right):
	if left < right:
		pivot = partition(arr, left, right)

		quick_sort(arr, left, pivot - 1)

		quick_sort(arr, pivot + 1, right)


def partition(arr, left, right):
	pivot = arr[right]
	item = left - 1

	for i in range(left, right):
		if arr[i] <= pivot:
			item = item + 1
			(arr[item], arr[i]) = (arr[i], arr[item])

	(arr[item + 1], arr[right]) = (arr[right], arr[item + 1])

	return item + 1



# if __name__ == "__main__":

#   input = [8,4,23,42,16,15]
#   size = len(input)
#   quick_sort(input, 0, size - 1)
#   print(input)