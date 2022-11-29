class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight
def fractionalKnapsack(W, arr):
    arr.sort(key=lambda x: (x.profit/x.weight), reverse=True)   
    res = 0
    for item in arr:
        if item.weight <= W:
            W -= item.weight
            res += item.profit
        else:
            res += item.profit * W / item.weight
            break 
    return res
if __name__ == "__main__":
    # W = 50
    # arr = [Item(60, 10), Item(100, 20), Item(120, 30)]
    W = int(input("Enter the weight of bag:- "))
    n = int(input("Enter the no of items in bag:- "))
    arr = []
    for i in range(n):
        profit,weight = map(int,input(f"Enter the profit and weight of {i+1}th element:- ").split()) 
        arr.append(Item(profit,weight))
    max_val = fractionalKnapsack(W, arr)
    print(max_val)