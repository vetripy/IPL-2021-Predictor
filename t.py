# x,y,z
# x,y = 72
# x,z = 600
# y,z = 900

def compute_lcm(x, y):

   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm


def lcm_factors(n):
    list1 = []
    for i in range(1,n+1):
        if (n%i)==0:
            list1.append(i)
    return(list1)

for i in lcm_factors(72):
    
    for k in lcm_factors(600):
    
        for j in lcm_factors(900):
        #     if i==8 and j==300 and k==9:
        #         print(i,j,k)
        #         print(compute_lcm(i,j))
        #         print(compute_lcm(i,k))
        #         print(compute_lcm(j,k))

            if compute_lcm(i,j)==72 and compute_lcm(i,k)==600 and compute_lcm(j,k)==900:
                print(i,j,k)

