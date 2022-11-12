#max num

def max_num(a,b,c):
    return max([a,b,c])

print (max_num(14, 18, 13))
print (max_num(54, 9, 22))
print (max_num(227, 328, 814))

#multiplication

def mult_list(lst):
    if len(lst) == 0:
        return 0

    prod = lst[0]

    if len(lst) > 1:
        for i in lst[1:]:
            prod = prod * i

    return prod

print(mult_list([10, 8, 2]))
print(mult_list([]))
print(mult_list([18]))

#reverse

def rev_string(my_str):
    return my_str[::-1]

print(rev_string("dachshunds"))
print(rev_string("pizza"))
print(rev_string("summer"))

#number falls within a certain range

def num_within(x, a, b):
    return x in range (a, b + 1)

print(num_within(2, 3, 4))     
print(num_within(3, 1, 3))     
print(num_within(15, 10, 5))

# Pascal

triangle = [[1],[1,1]]
def pascal(n):
  #base case
  if n < 1:
    print("invalid number of rows")
  elif n == 1:
    print(triangle[0])
  else:
    row_number = 2

    #fill up correct number of rows in triangle
    while len(triangle) < n:
      row = []
      row_prev = triangle[row_number - 1]
      
      #create correct row, then add to triangle (this row will be 1 longer than row before it)
      length = len(row_prev)+1
      for i in range(length):
        #first number is 1
        if i == 0:
          row.append(1)
        #intermediate nunmbers get added from previous rows
        elif i > 0 and i < length-1:
          row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
        #last number is 1
        else:
          row.append(1)
      triangle.append(row)
      row_number += 1

    #print triangle
    for row in triangle:
      print(row)

pascal(2)
pascal(5)