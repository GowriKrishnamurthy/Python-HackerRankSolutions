def computeCoins(amount,coinsList):
    result = ''
    
    for c in coinsList: 
        coinsUsed = (amount // c)
        amount = amount - (c * coinsUsed)
        if coinsUsed > 0:
            result = str(result) + str(c) + "s used:" + str(coinsUsed) + ", " 
            
    result = result.rstrip(', ')        
    return result
    
amount = int(input('Enter amount: '))
coinsList=[500,200,100,50]

print(computeCoins(amount,coinsList))