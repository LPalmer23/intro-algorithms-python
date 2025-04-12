# TT Securities    
# Name: Lydia Palmer
# email: lapalmer@bu.edu
# 
# Stock price analysis simulator with menu-based user input.
# 
# Developed as part of an academic project in CS112 at Boston University


def display_menu():
    """ prints a menu of options
    """  
    print()
    print('(0) Input a new list of prices')
    print('(1) Print the current prices')
    print('(2) Find the latest price')

    print('(3) Find the average price')
    print('(4) Find the min price and its day')
    print('(5) Find the max single-day change and its day')
    print('(6) Test a threshold')
    print('(7) Your investment plan')
    print('(8) Quit')

def get_new_prices():
    """ gets a new list of prices from the user and returns it
    """
    new_price_list = eval(input('Enter a new list of prices: '))
    return new_price_list

def print_prices(prices):
    """ prints the current list of prices
        input: prices is a list of 1 or more numbers.
    """
    if len(prices) == 0:
        print('No prices have been entered.')
        return
    
    print('Day Price')
    print('--- -----')
    for i in range(len(prices)):
        print('%3d' % i, end='')
        print('%6.2f' % prices[i])

def latest_price(prices):
    """ returns the latest (i.e., last) price in a list of prices.
        input: prices is a list of 1 or more numbers.
    """
    return prices[-1]



#Problem 4 Function 1
def avg_price(prices):
    '''takes a list of 1 or more prices and computes and returns the average 
    price.
    prices: input list of prices
    '''
    total = 0
    for i in prices:
        total += i
    return total/(len(prices))

#Probelm 4 Function 2
def min_day(prices):
    '''takes a list of 1 or more prices and computes and returns the day (i.e.,
    the index) of the minimum price.
    prices: input 
    '''
    min_index = 0
    for i in range(len(prices)):
        if prices[i] < prices[min_index]:
            min_index = i
    return min_index

#Problem 4 Function 3
def max_change_day(prices):
    '''takes a list of 2 or more prices and computes and returns the day (i.e.,
    the index) of the maximum single-day change in price.
    prices: input liat of prices
    '''
    max_index = 0
    for i in range(1, len(prices)):
        if (prices[i] - prices[i-1]) > (prices[max_index] - prices[max_index - 1]):
            max_index = i
    return max_index

#Problem 4 Function 4
def any_above(prices, threshold):
    '''takes a list of 1 or more prices and an integer threshold, and uses a 
    loop to determine if there are any prices above that threshold.
    prices: input list of prices
    threshold: input integer
    '''
    for i in prices:
        if i > threshold:
            return True
    else:
        return False

#Problem 4 Function 5
def find_tts(prices):
    '''takes a list of 2 or more prices, and that uses one or more loops to 
    find the best days on which to buy and sell the stock whose prices are 
    given in the list of prices.
    pricess: input prices
    '''
    buy_index = 0
    sell_index = 1
    prices_range = range(len(prices))
    for i in prices_range:
        for j in prices_range[i+1:]:
            if (prices[j] - prices[i]) > (prices[sell_index] - prices[buy_index]):
                    sell_index = j
                    buy_index = i
    profit = prices[sell_index] - prices[buy_index]
    return [buy_index, sell_index, profit]

def tts():
    """ the main user-interaction loop
    """
    prices = []

    while True:
        display_menu()
        choice = int(input('Enter your choice: '))
        print()

        if choice == 0:
            prices = get_new_prices()
        elif choice == 8:
            break
        elif choice < 8 and len(prices) == 0:
            print('You must enter some prices first.')
        elif choice == 1:
            print_prices(prices)
        elif choice == 2:
            latest = latest_price(prices)
            print('The latest price is', latest)
        

        elif choice == 3:
            average = avg_price(prices)
            print('The average price is', average)
        elif choice == 4:
            minimum_day = min_day(prices)
            print('The min price is', prices[minimum_day], 'on day', minimum_day)
        elif choice == 5:
            day = max_change_day(prices)
            print('The max single-day change occurs on day', day)
            print('when the price goes from', prices[day-1], 'to', prices[day])
        elif choice == 6:
            threshold = int(input('Enter the threshold: '))
            result = any_above(prices, threshold)
            if result == True:
                print('There is at least one price above', threshold)
            if result == False:
                print('There are no prices above', threshold)
        elif choice == 7:
            answer = find_tts(prices)
            print('Buy on day', answer[0], 'at price', prices[answer[0]])
            print('Sell on day', answer[1], 'at price', prices[answer[1]])
            print('Total profit:', answer[2])
        else:
            print('Invalid choice. Please try again.')

    print('See you yesterday!')
    
    

