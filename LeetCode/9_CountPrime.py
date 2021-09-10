def count_prime(n):
    count = 0
    count1=0
    if n == 2:
      return 0
    for j in range(2,n):
      for i in range(1, (j+1)): 
          if j % i == 0: 
              count += 1
      if count > 2:
        count=0
      else:
        count1 += 1
        count = 0

    return count1
      

num=int(input("Enter number: "))
print(is_prime(num))