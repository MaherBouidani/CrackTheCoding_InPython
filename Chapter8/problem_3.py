# def find_magic(lis):
#    for i in range(len(lis)):
#       if lis[i] == i:
#          return i

# print (find_magic([1,2,2.5,3,5]))


def find_magic(lis):
   if lis[len(lis)-1] == len(lis)-1:
      return len(lis)-1

   
   return find_magic(lis[:len(lis)-1])

print (find_magic([1,2,2.5,3,5]))