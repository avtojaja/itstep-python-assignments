# 1. დაწერეთ პითონის ფუნქცია, რომელიც იღებს პარამეტრად ერთიდაიგივე ზომის სიას (list) და zip ფუნქციის გამოყენებით დააჯგუფეთ სიების ელემენტები.

# params: [1, 2, 3], ['a', 'b', 'c']
# outputs: ["(1, 'a')", "(2, 'b')", "(3, 'c')"]

def zip_to_strings(list1, list2):
    return [str(t) for t in zip(list1, list2)]

# მაგალითი
print(zip_to_strings([1, 2, 3], ['a', 'b', 'c']))
# Output: ["(1, 'a')", "(2, 'b')", "(3, 'c')"]



# 2. დაწერეთ პითონის ფუნქცია, რომელიც პარამეტრად იღებს რიცხვების სიას და აბრუნებს ელემენტების ნამრავლს. ფუნქციაში გაითვალისწინეთ გამონაკლისები (Exceptions), თუ მიიღეთ არასწორი ტიპის პარამეტრს (TypeError).
# ფუნქციის დასაწერად გამოიყენეთ lambda და functools-ის reduce მეთოდი.

# params: [1, 2, 3, 4, 5]
# output: 120

from functools import reduce

def product_of_list(numbers):
    try:
        return reduce(lambda x, y: x * y, numbers)
    except TypeError:
        return "Error: Input must be a list of numbers"

# მაგალითი
print(product_of_list([1, 2, 3, 4, 5])) # 120

# არასწორი ტიპის მაგალითი
print(product_of_list("hello")) # Error: Input must be a list of numbers



# 3. დაწერეთ lambda ფუნქცია, რომელიც იღებს მთელი რიცხვების სიას (list) და აბრუნებს მხოლოდ სიის კენტ ელემენტებს.

# params: [1, 2, 3, 4, 5, 6, 7]
# outputs: [1, 3, 5, 7]

nums = [1, 2, 3, 4, 5, 6, 7]
odd_numbers = list(filter(lambda x: x % 2 != 0, nums))
print(odd_numbers) # [1, 3, 5, 7]



# 4. დაწერეთ პითონის ფუნქცია, რომელიც იღებს ორ პარამეტრს, სტრიქონების სიასა და სტრიქონს (ending). დააბრუნეთ მხოლოდ სიის ის ელემენტები, რომელიც მთავრდება, მეორე პარამეტრად მიწოდებული სტრიქონით. გამოიყენეთ lambda და filter ფუნქცია. გაითვალისწინეთ გამონაკლისები (TypeError), თუ სხვა გამონაკლისიც აღმოჩნდა, ისიც გაითვალისწინეთ.

# მინიშნება: გადაავლეთ თვალი string მეთოდებს, მონახეთ ისეთი მეთოდი, რომელიც აბრუნებს სიტყვას, რომელიც მთავრდება რაღაც სიმბოლოებით...

# params: ['hello', 'world', 'coding', 'nod'], 'ing'
# outputs: ['coding']

def filter_ending(strings: list, ending: str):
    try:
        return list(filter(lambda s: s.endswith(ending), strings))
    except TypeError:
        return "TypeError: Check input types. 'strings' must be a list of strings and 'ending' must be a string."
    except Exception as e:
        return f"Error: {e}"

# მაგალითი
params = ['hello', 'world', 'coding', 'nod']
ending = 'ing'
print(filter_ending(params, ending)) # ['coding']

# მაგალითი არასწორ პარამეტრზე
print(filter_ending(123, ending)) # TypeError
