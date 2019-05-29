def even_number_of_evens(numbers):
    if numbers == []:
        return False
    else: 
        evens = 0
        for number in numbers:
            if number % 2 == 0:
                evens += 1
                
    if evens == 0:
        return False
    else:
        return evens % 2 == 0
    
    
assert even_number_of_evens([]) == False, "No Numbers"
assert even_number_of_evens([2]) == False, "One even number"
assert even_number_of_evens([2, 4]) == True, "two even numbers"
assert even_number_of_evens([2, 3]) == False, "Two numbers, 1 even"
assert even_number_of_evens([2,3,9,10,13,7,8]) == False, "Multiple odd numbers"
assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8, 5, 12]) == True, "4 Evens, all even"
assert even_number_of_evens([1, 3 ,9]) == False, "No Evens"

print("All tests passed!") 