def insertion_sort(input):
  for i in range(len(input)):
    j = i -1 
    temp = input[i]

    while j >= 0 and temp < input[j]:
      input[j + 1] = input[j]
      j = j-1
    
    input[j+1] = temp
  return input

# if __name__ == "__main__":
#   print(insertion_sort([8,4,23,42,16,15]))
