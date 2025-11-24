# 1. შექმენით სია num_list [44, 23, 11, 8, 20, 56, 33, 55], in-ის გამოყენებით დაწერეთ პროგრამა რომელიც შეამოწმებს თქვენს მიერ შეტანილი რიცხვი არის თუ არა სიაში.
# მაგ.:
# Enter a number: 56
# The number in list
# #===========================
# Enter a number: 45
# The number not in list

# სიის შექმნა
num_list = [44, 23, 11, 8, 20, 56, 33, 55]

# მომხმარებლისგან რიცხვის შეყვანა
user_input = int(input("Enter a number: "))

# შემოწმდეს არის თუ არა რიცხვი სიაში
if user_input in num_list:
    print("The number in list")
else:
    print("The number not in list")



# 2. დაწერეთ პროგრამა რომელიც შეამოწმებს თქვენს მიერ შეყვანილი რიცხვის ლუწობასა და კენტობას. თუ რიცხვი ლუწია გამოიტანეთ ტექსტი 'even' თუ კენტია 'odd'.
# მაგ.:
# Enter an integer: 25
# The number is odd
# #===========================
# Enter an integer: 36
# The number is even

# მთელი რიცხვის შეყვანა
number = int(input("Enter an integer: "))

# ლუწობის ან კენტობის შემოწმება
if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")



# 3. შექმენით ორი სტრინგის ტიპის ცვლადი st1 და st2, შეადარეთ ისინი is-ის გამოყენებით, თუ ემთხვევა გამოიტანეთ ტექსტი "Same object", წინააღმდეგ შემთხვევაში "Different object"

# ორი სტრინგის ტიპის ცვლადის შექმნა
st1 = "hello"
st2 = "hello"

# ობიექტების იდენტურობის შემოწმება
if st1 is st2:
    print("Same object")
else:
    print("Different object")



# 4. შექმენით სია num_list [44, 23, 11, 8, 20, 56, 33, 55], შეიტანეთ რიცხვი და დაწერეთ შემდეგი პირობა:

# * თუ შეტანილი რიცხვი მეტია სიაში არსებულ მე-3 ელემენტზე და ნაკლებია ბოლო ელემენტზე გამოიტანეთ ტექსტი "More than list elements";
# * თუ შეტანილი რიცხვი უდრის სიის მე-6 ელემენტს გამოიტანეთ ტექსტი "Equal";
# * სხვა ნებისმიერ შემთხვევაში გამოიტანეთ ტექსტი "None of the conditions were met".
# რიცხვის შეტანის ოპერაციისთვის გამოიყენეთ input მეთოდი.
# მაგ.:
# Enter a number: 105
# None of the conditions were met
# #===========================
# Enter a number: 40
# More than list elements
# #===========================
# Enter a number: 56
# Equal

# სიის შექმნა
num_list = [44, 23, 11, 8, 20, 56, 33, 55]

# რიცხვის შეყვანა მომხმარებლისგან
number = int(input("Enter a number: "))

# პირობის შემოწმება
if number > num_list[2] and number < num_list[-1]:
    print("More than list elements")
elif number == num_list[5]:
    print("Equal")
else:
    print("None of the conditions were met")
