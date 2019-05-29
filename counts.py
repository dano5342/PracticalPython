def count_upper_case(message):
    return sum([1 for c in message if c.isupper()])
    
assert count_upper_case("") == 0, "Empty string"
assert count_upper_case("A") == 1, "One upper case"
assert count_upper_case("a") == 0, "One lower case"
assert count_upper_case("£$%^%^") == 0, "special characters"
assert count_upper_case("A B C D E F G") == 7, "7 Upper case"
assert count_upper_case("$%^ A 7 C c 2") == 2, "2 Upper case"


print("All the tests passed")