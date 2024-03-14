'''
Given an array of integers numbers, compare the sum of elements on even positions against the sum of elements on odd positions (o-based) 
Retum "even" if the sum of elements on even positions is greater, 
return "odd" if the sum of elements on odd positions is greater, or "equal" if both sums are equal.

Note: You are not expected to provide the most optimal solution, but a solution 
with time complexity not worse than o(numbers.length); will fit within the execution time limit
'''

def solution(numbers):

    sum_even = 0
    sum_odd = 0


    for index in range(len(numbers)):

        if index % 2 == 0:
            sum_even += numbers[index]
        elif index % 2 !=0:
            sum_odd += numbers[index]

        '''
        second approach to use sum with itterator: 
        sum_even = (numbers[i] for i in range(len(numbers)) if i % 2 == 0)
        sum_odd = (numbers[i] for i in range(len(numbers)) if i % 2 != 0)
        '''

    if sum_even > sum_odd:
        return "even"
    elif sum_odd > sum_even:
        return "odd"
    else:
        return "equal"



numbers = [2,5,6,8,9,10,12,14]

print(solution(numbers))

