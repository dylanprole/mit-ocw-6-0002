class Food(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.calories = w

    def getValue(self):
        return self.value

    def getCost(self):
        return self.calories
    
    def density(self):
        return self.getValue() / self.getCost()

    def __str__(self):
        return self.name + ': <' + str(self.value) + ', ' + str(self.calories) + '>'
    
def buildMenu(names, values, calories):
    '''
    names, values, calories lists of same length.
    name is a list of strings
    values and calories lists of numbers
    returns list of foods
    '''
    menu = []
    for i in range(len(values)):
        menu.append(Food(names[i], values[i],
                         calories[i]))
    return menu

def greedy(items, maxCost, keyFunction):
    '''
    Assumes items a list, maxCost >= 0, 
        keyFunction maps elements of items to numbers
    Overall complexity = n*log(n) + n = O(n*log.n); where n = len(items)
    '''
    # Flexible because we use keyFunction to sort item from best to worst
    # we can determine which is best and which is worst.
    # Note: sorted() will create a .copy() of the list
    itemsCopy = sorted(items, key = keyFunction, 
                       reverse = True) 
    ''' Complexity for sorting list (uses tims sort, variant of quick <-> merge sort)
        = n*log.n; where n = len(items)'''

    results = list()
    totalValue, totalCost = 0.0, 0.0

    for i in range(len(itemsCopy)):
        if (totalCost + itemsCopy[i].getCost()) <= maxCost:
            results.append(itemsCopy[i])
            totalCost += itemsCopy[i].getCost()
            totalValue += itemsCopy[i].getValue()
    ''' Complexity for looping through a list once
        = n; where n = len(n)
    '''
    
    return (results, totalValue, totalCost)

def testGreedy(items, constraint, keyFunction):
    taken, val, cost = greedy(items, constraint, keyFunction)
    print('Total value of items taken =', val)
    print('Total calories taken =', cost)
    print('    item: <value, calories>')
    for item in taken:
        print('   ', item)

def testGreedys(foods, maxUnits):
    print('Use greedy by value to allocate', maxUnits,
          'calories')
    testGreedy(foods, maxUnits, Food.getValue)

    print('\nUse greedy by cost to allocate', maxUnits,
          'calories')
    testGreedy(foods, maxUnits,
               lambda x: 1/Food.getCost(x)) # Use 1/cost to reverse list
    
    print('\nUse greedy by density to allocate', maxUnits,
          'calories')
    testGreedy(foods, maxUnits,
               lambda x: 1/Food.getCost(x))

## ---------------- Test code ----------------

food_names = ['wine', 'beer', 'pizza', 'burger', 'fries', 'coke', 'apple', 'donut']
food_values = [89, 90, 30, 50, 90, 79, 90, 10]
food_calories = [123, 154, 258, 354, 365, 150, 95, 195]

my_menu = buildMenu(food_names, food_values, food_calories)

testGreedys(my_menu, 1000)

## ------ lambda tutorial ------
'''
Used to create an anonymous function
    - lambda <id1, id2, ... idn>: <expression>
    - returns a function of n arguments
    - allows us to write a function inline
'''