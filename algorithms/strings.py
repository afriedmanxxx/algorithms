string_a = "Hello World!"


def remove_exclpoint_from_end_of_str(x):
    return x[0:-1] if x.endswith("!") else x


print(remove_exclpoint_from_end_of_str(string_a))


 # Palindrome
def palindrome(w1,w2):
    return w1 == w2[::-1]


print(palindrome('hello', 'olleh'))


def anagram(w1,w2):
    if len(w1) == len(w2):
        if sorted(w1) == sorted(w2):
            return f"The word {w1} and word {w2} are anagrams."
    return "Words are not anagrams"


def anagram2(w1,w2):
    letters_w1 = [l for l in w1]
    for l2 in w2:
        if l2 in letters_w1:
            letters_w1.remove(l2)
        else:
            letters_w1.append(l2)
    return len(letters_w1) == 0


w1 = "kayak"
w2 = 'kayak'
print(anagram(w1, w2))
print(anagram2(w1, w2))


def remove_first_last(x):
    return x[1:-1]


print(remove_first_last(string_a))