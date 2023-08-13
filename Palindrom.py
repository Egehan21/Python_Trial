import random
def palindrome(a):
    b=str(a)
    reverse_b=b[::-1]
    if reverse_b == b:
        return True
    else: 
        return False

def prime(number):
   if number <=1:
       return False
       
   for i in range(2,number):
       
       if number %i == 0:return False
       
       else:return True
       
def factorial(number):
    result=1
    if number <= -1:
        return False
    for i in range(1,number+1):
        result = result*i
    return result

def substring(large_word, small_word):
    for i in large_word:
        if len(small_word) < len(large_word) and small_word in large_word:
            return True
        else:
            return False

def stock():
    stock_prices=[]
    for i in range(11):
        rrandom_stock = random.randint(100,200)
        stock_prices.append(rrandom_stock)
    max_profit=0
    min_price=stock_prices[0]

    for prices in stock_prices[1:]:
        if prices < min_price:

            min_price = prices

        potential_profit= (prices - min_price)

        if potential_profit > max_profit:

            max_profit = potential_profit

    return max_profit

        
  


    
