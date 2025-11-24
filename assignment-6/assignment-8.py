# 1. დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს პარამეტრად n, და გამოიტანს ფიბონაჩის n რაოდენობის მიმდევრობას.

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()

# მაგალითი
fibonacci(10)



# 2. დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს პარამეტრად ორ სტრიქონს და შეამოწმებს არის თუ არა სტრიქონები ანაგრამები (ანაგრამი არის სიტყვა ან შესიტყვება, რომელიც წარმოიქმნება სხვა სიტყვის ან შესიტყვების ასოების გადაადგილებით). მაგ.: race და care ანაგრამებია.

def is_anagram(str1, str2):
    # ვშლით space-ებს და ვაქცევთ lowercase-ში (Unicode-ის სრული მხარდაჭერით)
    s1 = "".join(str1.split()).casefold()
    s2 = "".join(str2.split()).casefold()
    return sorted(s1) == sorted(s2)

# მაგალითი
print(is_anagram("race", "care"))      # True (ინგლისური)
print(is_anagram("Listen", "Silent"))  # True (Case insensitive)
print(is_anagram("სალამი", "მასალი"))  # True (ქართულიც მუშაობს)
print(is_anagram("თავი", "თივა"))      # True
print(is_anagram("hello", "world"))    # False



# 3. დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს n რიცხვს და დააბრუნებს მის ფაქტორიალს.

def factorial(n):
    if n < 0:
        return None
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# მაგალითი
print(factorial(5))  # 120
print(factorial(0))  # 1



# 4. დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს ორ პარამეტრს, პირველს სტრიქონს და მეორეს სიმბოლოს. ფუნქციამ უნდა მოძებნოს სტრიქონში რამდენჯერ მეორდება პარამეტრად მიღებული სიმბოლო და დააბრუნოს მისი რაოდენობა.

def count_char(string, char):
    count = 0
    for c in string:
        if c == char:
            count += 1
    return count

# მაგალითი
print(count_char("გამარჯობა", "ა"))  # 3
print(count_char("hello", "l"))      # 2
