price = [0]*5
for i in range(5):
    price[i] = int(input())

burger = 2000
beverage =2000
for i in range(5):
    if i<=2:
        if burger>price[i]:
            burger = price[i]
    else:
        if beverage>price[i]:
            beverage = price[i]

setMenu = burger + beverage - 50
print(int(setMenu))
        
