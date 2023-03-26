#  Three Main Models:

## Optimization Models

- Using an objective function to minimize or maximise, e.g:
    - minimize travel time getting from point A to point B (transport)
- Layerting constraints (sometimes empty), e.g:
    - we only have $500 to spend on travel
    - We have to arrive before 2pm

### Knapsack Problem
We have a burgler that has a backpack with a finite amount of space, 
they are tryting to maximise the value of goods they steal.

- objective function = maximise $$ of goods
- constraints = limited space in backpack

#### Two types of knapsack problems:
- 0/1 knapsack (we either take it or don't) - 1 gold bar, 2 silver bars
- Continuous or fractional (we can cut a gold bar in half)
    - This is usually not interesting, we just use greedy thinking where we take the most
    expensive thing until it runs out, then move to the second most expensive thing.

### 0/1 Knapsack Problem
- Each item represented by a pair, $<$ $value, weight$ $>$
- Knapsack can accomodate items with a total weight of no more than $w$
- A vector, $L$, of length $n$, represents the set of available itmes. each element of the 
vector is an item
- A vector, $V$, of length $n$, represents whether or not items are taken, e.g.:
    - if $V[i]$ == 1: $L[i]$ is selected
    - if $V[i]$ == 0: $L[i]$ is not selected

#### Objective function:
- $Maximise: \sum_{i=0}^^{N-1} V[i]*L[i].value$
- $Constraint: \sum_{i=0}^{N-1} V[i]*L[i].weight \leq w$

#### Brute Force solving (usually not the best):
1) Generate all subsets of the items (known as powerset)
2) Remove subsets where total units exceed the allowed weight
3) From the remaining subsets, chooise those with the highest value
Note - A powerset with 100 items will be HUUUUUUUGE ~12,000,000,000,000,000

#### Good Solution? NONE
- All optimization problems are inherently exponential

#### Greedy Algorithm - A practical alternative
```
while knapsack is not full
    put best available item into knapsack
```
- But what does "best" mean? Highest value? Best ration between value and weight?
- Sit down for a meal, you have a calorie budget = 800 cal
- Choosing between menu items to find what you want to eat

<<< See `food_knapsack.py` for code >>>
```
food_names = ['wine', 'beer', 'pizza', 'burger', 'fries', 'coke', 'apple', 'donut']
food_values = [89, 90, 30, 50, 90, 79, 90, 10]
food_calories = [123, 154, 258, 354, 365, 150, 95, 195]
```
video time = 33 min

#### Why is greedy not optimal?
- Greedy works by finding a series of local optima.
- This does not mean that a golbal optima is found!
```
       . global maximum
      /\
 /\  /  \
/  \/    \
  . local maximum
```
