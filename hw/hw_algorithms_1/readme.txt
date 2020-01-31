https://www.codewars.com/users/jKTS/completed

#Array.diff
def array_diff(a, b):
    return [i for i in a if i not in b]

#Century From Year
def century(year):
    use = divmod(year,100)
    return use[0]+1 if use[1] > 0 else use[0]

#Reversed sequence
def reverse_seq(n):
    return list(range(n, 0, -1))

#Reversed Strings
def solution(string):
    return string[::-1]

#What's the real floor?
def get_real_floor(n):
    if n < 1:
        return n
    elif n < 14:
        return n-1
    return n-2

#Beginner Series #4 Cockroach
def cockroach_speed(s):
    return(int(s*1000/36))

#Square(n) Sum
def square_sum(numbers):
    return(sum(i**2 for i in numbers))

#The Wide-Mouthed frog!
def mouth_size(animal):
  mouth_size = 'wide' 
  if str.upper(animal) == 'ALLIGATOR':
      mouth_size = 'small'
  return mouth_size

#Remove First and Last Character
def remove_char(s):
    return(s[1:len(s)-1])

#Grasshopper - Messi goals function
def goals(laLiga, copaDelRey, championsLeague):
    return (laLiga+copaDelRey+championsLeague)

#Sum Mixed Array
def sum_mix(arr):
    n = 0
    while n < len(arr):
        arr[n] = int(arr[n])
        n += 1
    return (sum(arr))

#Multiply
def multiply(a, b):
  return a * b