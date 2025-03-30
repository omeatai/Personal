## +LinkedIn - Level Up Python

## [COURSE](https://www.linkedin.com/learning/level-up-python/put-your-python-skills-to-the-test?resume=false)

<details>
<summary>Challenge 1: Find Prime Factors </summary>

# Find Prime Factors

![image](https://github.com/user-attachments/assets/b798789f-2e75-4f86-abb6-f6ede2b94079)
![image](https://github.com/user-attachments/assets/970f05c3-43f7-43f8-85a6-1aff2ce245cd)
![image](https://github.com/user-attachments/assets/2f118f58-bd07-4eb3-9a1e-356bfb5601cf)


# #END</details>

<details>
<summary>Solution 1: Find Prime Factors </summary>

# Find Prime Factors

```py
def get_prime_factors(value):
    factors = []
    divisor = 2

    while divisor <= value:
        if value % divisor == 0:
            factors.append(divisor)
            value = value // divisor
        else:
            divisor += 1
    return factors


print(get_prime_factors(630))

```

```py
def get_prime_factors(value):
    factors = []

    while value > 2:
        for x in range(2, value + 1):
            if value % x == 0:
                factors.append(x)
                value = value//x

    return (sorted(factors))


print(get_prime_factors(630))

```

# #END</details>

<details>
<summary>Challenge 2: Identify a Palindrome </summary>

# Identify a Palindrome

![image](https://github.com/user-attachments/assets/c86dc625-488c-4388-9cba-476b816a163f)
![image](https://github.com/user-attachments/assets/9089b019-6c42-480c-80a3-05b8aca046cf)
![image](https://github.com/user-attachments/assets/48507f2c-3ac6-4b07-9bbb-c750a9ea64b3)
![image](https://github.com/user-attachments/assets/26327c2d-827d-41f6-9110-c5a8d604a9c2)

# #END</details>

<details>
<summary>Solution 2: Identify a Palindrome </summary>

# Identify a Palindrome

```py
import re


def is_palindrome(word):
    cleaned_word = re.findall(r"[a-z]", word.lower())
    forwards = ''.join(cleaned_word)
    backwards = forwards[::-1]
    return forwards == backwards


print(is_palindrome("Go hang a salami - I'm a lasagna hog."))

```

```py
def is_palindrome(word):
    cleaned_word = [char for char in word.lower() if char.isalnum()]

    left = 0
    right = len(cleaned_word) - 1

    while left <= right:
        if cleaned_word[left] != cleaned_word[right]:
            return False
        left += 1
        right -= 1
    return True


print(is_palindrome("Go hang a salami - I'm a lasagna hog."))

```

# #END</details>

<details>
<summary>Challenge 3: Sort a String </summary>

# Sort a String

![image](https://github.com/user-attachments/assets/f35ac470-a36e-4ab6-af07-71fc8b6b58ac)
![image](https://github.com/user-attachments/assets/a3c94885-6fe4-4748-999b-09fd31e01789)
![image](https://github.com/user-attachments/assets/0d244dc3-f78f-4c31-a1a0-539b92b56761)
![image](https://github.com/user-attachments/assets/b17b9eae-2e37-4d03-a69c-4604660bdd29)


# #END</details>

<details>
<summary>Solution 3: Sort a String </summary>

# Sort a String

```py
def sort_words(word):
    word_list = word.split(" ")
    return " ".join(sorted(word_list, key=lambda x: x.lower()))
    # return " ".join(sorted(word_list, key=str.casefold))

print(sort_words("banana ORANGE apple"))
print(sort_words("string of words"))
```

```py
def sort_words(input):
    words = input.split()
    print(words)
    words = [w.lower() + w for w in words]
    words.sort()
    words = [w[len(w)//2:] for w in words]
    return ' '.join(words)

print(sort_words("banana ORANGE apple"))
print(sort_words("string of words"))

```

# #END</details>

<details>
<summary>Challenge 4: Fill all List Items </summary>

# Fill all List Items

![image](https://github.com/user-attachments/assets/040ec54e-d80a-4b99-8dc6-39dc45382a43)
![image](https://github.com/user-attachments/assets/f698433d-41f6-4b3c-9742-0dc289a0b2e4)
![image](https://github.com/user-attachments/assets/d81fd556-7f7e-4b5a-a770-ae2f7f6f425e)
![image](https://github.com/user-attachments/assets/ef59b0bb-581c-4a48-a57f-2e7c57b6d1ec)
![image](https://github.com/user-attachments/assets/c1821a0a-58b9-4d33-a354-763091435646)
![image](https://github.com/user-attachments/assets/238d32d6-0a97-4ee6-bbb7-264144756c9e)


# #END</details>

<details>
<summary>Solution 4: Fill all List Items </summary>

# Fill all List Items

```py

```

```py

```

```py

```

```py

```

```py

```

```py

```

```py

```

```py

```


# #END</details>
