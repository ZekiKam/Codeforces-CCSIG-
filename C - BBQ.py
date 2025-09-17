#k - initial temp
#a - required temp for cooking burger
#b - required temp for cooking sausage
#x - temp drop after cooking burger
#y - temp drop after cooking sausage
#1≤𝑘,𝑎,𝑏,𝑥,𝑦≤10^9

t = int(input())
for i in range(t):
    k,a,b,x,y = map(int, input().split())

   
    def cook(k,a,b,x,y):
        count = 0
        if k >= a:
            count = (k-a)//x
            k = k-count*x
            if k >= a:
                count += 1
                k-=x
                
        if k >= b:
            count += (k-b)//y
            k = k-(k-b)//y*y
            if k >= b:
                count += 1
                k-=y
        
        return count
    

    if x<y: #If burger drop time is less than sausage's, make burgers first
        print(cook(k,a,b,x,y))
        
    else:
        print(cook(k,b,a,y,x))

#     count1 = cook(k,a,b,x,y)
#     count2 = cook(k,b,a,y,x)

#     if count1 > count2:
#         print(count1) 
#     else:
#         print(count2)

