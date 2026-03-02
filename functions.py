def add(a, b):
    return a + b

def is_even(n):
    return n % 2 == 0

def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

def count_vowels(s):
    # أضفنا الـ a والـ y لتكتمل القائمة المطلوبة
    return sum(1 for ch in s if ch in "aeiouy")

def first_word(sentence):
    # استخدمنا 0 للحصول على الكلمة الأولى
    return sentence.split()[0]
