# 1. დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს და აბრუნებს სტრიქონის UTF-8 დაშიფრულ ვერსიას.

# მომხმარებლისგან სტრიქონის მიღება
text = input("შეიყვანეთ სტრიქონი: ")

# UTF-8 ენკოდინგი
encoded_text = text.encode("utf-8")

print("UTF-8 დაშიფრული ვერსია:", encoded_text)



# 2. დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს.
# ჩამოაშორეთ ზედმეტი ინტერვალები.
# ყველა სიმბოლო გადაიყვანეთ პატარა ასოებში და
# დაუმატეთ ქვესტრიქონი 'Python'.
# თუ შეყვანილ სტრიქონში არსებობს სიტყვა "python", ჩაანაცვლეთ "Python"-ით.
# მინიშნება: ზედმეტი ინტერვალების ჩამოსაშორებელი მეთოდია `.strip()`.
# მაგ.: "  Python is funny     ".strip()   ====>  "Python is funny"

# სტრიქონის მიღება
text = input("შეიყვანეთ სტრიქონი: ")

# ზედმეტი ინტერვალების მოცილება
text = text.strip()

# ყველა სიმბოლოს პატარა ასოებად გადაყვანა
text = text.lower()

# დავამატოთ ქვესტრიქონი "Python"
text = text + " Python"

# თუ არსებობს "python", ჩაანაცვლოს "Python"-ით
text = text.replace("python", "Python")

print("მიღებული სტრიქონი:", text)



# 3. დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს.
# პროგრამამ უნდა დააბრუნოს ახალი სტრიქონი,
# რომელიც შედგება შეყვანილი სტრიქონის პირველი ნახევრისაგან.

# სტრიქონის მიღება
text = input("შეიყვანეთ სტრიქონი: ")

# სტრიქონის სიგრძის ნახევარი
half_len = len(text) // 2

# პირველი ნახევრის ამოღება
new_text = text[:half_len]

print("ახალი სტრიქონი:", new_text)



# 4. დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს.
# string მოდულის გამოყენებით დაწერეთ შემოწმება.
# სტრიქონი ვალიდურია მაშინ, როდესაც ის შეიცავს მინიმუმ ერთ ლათინურ ასოსა და
# მინიმუმ ერთ ციფრს და ამავე დროს არ შეიცავს დამატებით სიმბოლოებს: '!', '~', '#', '$' და ა.შ.

import string

# სტრიქონის მიღება
text = input("შეიყვანეთ სტრიქონი: ")

allowed_chars = string.ascii_letters + string.digits

has_letter = False
has_digit = False
only_allowed = True

# სიმბოლოების შემოწმება ციკლით
for ch in text:
    if ch in string.ascii_letters:
        has_letter = True
    if ch in string.digits:
        has_digit = True
    if ch not in allowed_chars:
        only_allowed = False

# საბოლოო შემოწმება
if has_letter and has_digit and only_allowed:
    print("სტრიქონი ვალიდურია")
else:
    print("სტრიქონი არავალიდურია")



# 5. დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს,
# სტრიქონი გადაყავს ბაიტებში, ბეჭდავს მნიშვნელობას და შემდეგ კი
# გადაყავს ბაიტებიდან სტრიქონში და ბეჭდავს სტრიქონს.

import base64

# სტრიქონის მიღება
text = input("შეიყვანეთ სტრიქონი: ")

# სტრიქონის გადაყვანა ბაიტებში (UTF-8)
bytes_text = text.encode("utf-8")
print("სტრიქონი ბაიტებში:", bytes_text)

# ბაიტების დაბრუნება სტრიქონში (UTF-8)
decoded_text = bytes_text.decode("utf-8")
print("ბაიტებიდან დაბრუნებული სტრიქონი:", decoded_text)

# Base64 ენკოდირება
base64_encoded = base64.b64encode(bytes_text)
print("Base64 ენკოდირებული სტრიქონი:", base64_encoded)

# Base64 დეშიფრაცია
base64_decoded = base64.b64decode(base64_encoded)
decoded_from_base64 = base64_decoded.decode("utf-8")
print("Base64-დან დაბრუნებული სტრიქონი:", decoded_from_base64)
