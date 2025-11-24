class item:
    def __init__(self,p,w):
        self.weight=w
        self.profit=p
        self.ratio=p/w
def knack_sack(arr,limit):
    arr.sort(key=lambda x: x.ratio,reverse=True)
    total_profit=0
    weight=0
    for i in arr:
        if (limit-weight)>=i.weight:
            total_profit+=i.profit
            weight+=i.weight
        else:
            total_profit+=(limit-weight)*i.ratio
            break
    return total_profit
limit_weight=int(input("enter the limit of weight:"))
arr=[]
n=int(input("no.of items:"))
for i in range(n):
    arr.append(item(int(input(f"enter the profit of item{i+1}:")),int(input(f"enter the weight of item{i+1}:"))))

print(f"maximum profit made is {knack_sack(arr,limit_weight):.2f}")

