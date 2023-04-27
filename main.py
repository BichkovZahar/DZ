#Напишіть функцію, яка приймає рядок та повертає
#True, якщо рядок є паліндромом, та False в іншому випадку.
lst = input("Введіть текст для провірки на паліндром: ")
def lesson_2(lst):
    lst2 = lst[::-1]
    if lst == lst2:
        print("True")
    if lst != lst2:
        print("False")
lesson_2(lst)
