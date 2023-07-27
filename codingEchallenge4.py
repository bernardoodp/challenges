'''
    [7,1,5,3,6,4]
    [7,6,4,3,1]
    Pegar o index do elemento min e max
    Se o index do elemento max for maior que o min, exclui e procura o proximo elemento max, e faz a comparação novamente
    até encontrar um elemento max em um index maior que o min
    sem encontrar pegar a diferença deles
    se nao encontrar, retornar zero 

'''





# def maxProfit(prices: list[int]) -> int:
#     in_min = prices.index(min(prices))
#     in_max = prices.index(max(prices))
#     print(in_min, in_max)
#     lent = len(prices)
#     for price in range(0,lent):
#         if lent == 1:
#             return 0
#         if lent - 1 == in_min:
#             prices.pop(in_min)
#             in_min = prices.index(min(prices))
#         if in_min > in_max:
#             print(in_min, in_max)
#             prices.pop(in_max)
#             in_max = prices.index(max(prices))
#             in_min = prices.index(min(prices))
#         elif in_max > in_min:
#             result = prices[in_min] - prices[in_max]
#             return result + (abs(result) * 2)
#         else: 
#             return 0
def maxProfit(prices: list[int]) -> int:
    profit = 0
    buy = prices[0]
    for i in prices[1:]:
        if i > buy:
            profit = max(profit, i - buy)
        else: 
            buy = i
    return profit


print(maxProfit([7,6,4,3,17]))

lis = [85] * 2
print([85]*10000)