# 1. შექმენით გლობალური ცვლადი int_list = [10,20,30,40] და დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს რიცხვს პარამეტრად და გლობალურ int_list სიაში ჩაამატებს პარამეტრად მიღებულ რიცხვს.

# გლობალური სია
int_list = [10, 20, 30, 40]

def add_to_list(number):
    global int_list # ვიყენებთ გლობალურ ცვლადს
    int_list.append(number)

# მაგალითი
add_to_list(50)
print(int_list) # [10, 20, 30, 40, 50]



# 2. დაწერეთ პითონის ფუნქცია, რომელიც პარამეტრად იღებს რიცხვების სიას (ლისტს) და აბრუნებს რიცხვების ჯამს. პარამეტრად უნდა მიიღოს შემდეგი სია [100, 20, 30, 50, 5323, 3321, 22, 56, 700, 90, 10].

def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# მაგალითი
numbers = [100, 20, 30, 50, 5323, 3321, 22, 56, 700, 90, 10]
print("ჯამი:", sum_list(numbers))



# 3. შექმენით გლობალური ცვლადი gl_str = "Global" და დაწერეთ პითონის ფუნქცია, რომელიც ქმნის ლოკალურ ცვლადს იგივე სახელით, რაც გლობალურ ცვლადს აქვს (gl_str) და აბრუნებს ლოკალური ცვლადის მნიშვნელობას.

# გლობალური ცვლადი
gl_str = "Global"

def local_variable_demo():
    gl_str = "Local" # ლოკალური ცვლადი იგივე სახელით
    return gl_str

# ფუნქციის გამოძახება
print(local_variable_demo()) # დაბეჭდავს: Local

# გლობალური ცვლადის გადამოწმება
print(gl_str) # დაბეჭდავს: Global



# 4. რეკურსიის გამოყენებით დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს ერთ პარამეტრს number და დააბრუნებს ციფრების ჯამს (მაგალითად თუ ფუნქციამ მიიღო რიცხვი 12345, უნდა დააბრუნოს 15. რადგან 1+2+3+4+5 უდრის 15-ს).

def sum_digits(number):
    number = abs(number)
    if number == 0:
        return 0
    return number % 10 + sum_digits(number // 10)

# მაგალითი
print(sum_digits(12345))  # 15
print(sum_digits(9876))   # 30



# 5. რეკურსიის გამოყენებით დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს პარამეტრად სტრიქონს და დააბრუნებს მის შებრუნებულ (reverse) სტრიქონს (მაგალითად input: Hello Output: olleH)

def reverse_string(s):
    if s == "":
        return ""
    return s[-1] + reverse_string(s[:-1])

# მაგალითი
print(reverse_string("Hello"))  # შედეგი: olleH
print(reverse_string("Python")) # შედეგი: nohtyP
print(reverse_string("გამარჯობა")) # შედეგი: აბოჯრამაგ
