# a="Mukul Kumar Sharma"
# print(a)
# # Upper case lower case related
# print(a.upper())
# print(a.lower())
# print(a.title())
# print(a.swapcase())
# print(a.capitalize())
#
# # Searching and Checking
# print(a.count("u"))
# print(a.find("Q"))
# print(a.index("K"))
# print(a.startswith("Mukul"))
# print(a.endswith("ar"))
#
# # Checking string type
# a="  New  12  "
# print(a.isalnum())
# print(a.isnumeric())
# print(a.isdigit())
# print(a.islower())
# print(a.isspace())
# print(a.isupper())
# print(a.isalpha())
#
# # Modifying strings
#
# print(a.lstrip())
# print(a.rstrip())
# print(a.strip())
# print(a.replace(" New","Neww"))
# # print(a)
#
# fruits="Mango,Orange,Pineapple"
# print(fruits)
# print(fruits.split(","))
# print("|".join(['Mulli','Aloo','Gajar']))
#
# #  Slicing
#
# name="Mukul Kumar Sharmaa"
# print(name[0],name[1],name[-1],name[::-1],name[0:5])
#
# #  More Useful ones len,sorted
# print(len(name))
# print(sorted(name))

#  Lists and some func
# cars=['Alto','Fararri','Tata']
# print(cars)
# cars.append('Toyota')
# print(cars)
# cars.extend(['Neww','All New'])
# print(cars)
# cars.insert(3,'eicher')
# print(cars)
# cars.remove('Alto')
# print(cars)
# cars.pop()
# print(cars)
# print(cars.pop(2)) # pop from index 2
# print(cars)
#
# marks=[13,14,15,13,12,12,12,12,12]
# print(marks)
# print(len(marks))
# print(marks.index(15))
# print(marks.count(12))
# marks.reverse()
# print(marks)
# marks.sort()
# print(marks)
# marks.sort(reverse=True)
# print(marks)
#
# marksd=marks
# print(marksd)
# marks.insert(3,11)
# print(marksd)
# marksf=marks.copy()
# print(marksf)
# marks.insert(4,9)
# print(marksf)
#
# print(marksf[::-1])
# print(len(marksf))
# print(sum(marksf))
# print(min(marksf))
# print(max(marksf))
# print(any(marksf))
# print(all(marksf))


# TUPPPPPPPPPPLEEEES

# t=(1,2,3,2,2,3,3,3,3,2)
# print(t)
# t1=(4,)  # , comma is neccessary
# print(t1)
# print(t.count(3))
# print(t.index(3))
# print(len(t))
# print(max(t))
# print(min(t))
# print(sorted(t))
# print(sorted(t,reverse=True))
# t2=t+t1
# print(t2)
#
# a,b,*c,d=t
# print(a)
# print(b)
# print(c)
# print(d)
# t.append(10)
# print(t)

# Dictionary on Python

# student={
#     "Name":"Mukul",
#     "Batch": "2022",
#     "Height":"1.67 m",
#
# }
# print(student["Batch"])
# print(student.get("Batch"))  # Safer Way
# print(student.get("b",1)) # Default Value after att if val no present
# student["Marks"]="78"
# print(student)
# student["Marks"]="87"
# print(student)
# print(student.pop("Batch"))
# print(student.popitem())
# print(student)
#  # More of these like delete, clear(to clear all values)
# print(student.keys())
# print(student.values())
# print(student.items())
# print("Marks" in student)
# print("Name" in student)
#
# squares={x:x * x for x in range(10)}
# print(squares)
# even_squares={x:x * x for x in range(10) if x%2==0}
# print(even_squares)





# 🔥 Important Interview Concepts
# ✅ 1. Dictionary is unordered (before Python 3.7)
#       Now (3.7+) → maintains insertion order.
#
# ✅ 2. Keys must be immutable
#
# Valid keys:
        # {1: "a"}
        # {"name": "Rahul"}
        # {(1,2): "tuple key"}
# Invalid:
        # {[1,2]: "list"}   ❌
#
# ✅ 3. Use Case: Frequency Counter 🔥🔥
#
# Very common:
#
            # arr = [1,2,2,3,3,3]
            #
            # freq = {}
            # for num in arr:
            #     freq[num] = freq.get(num, 0) + 1
            #
            # print(freq)
            #
            #
            # Output:
            #
            # {1:1, 2:2, 3:3}
# Sets in Python
# s={1,2,3,4,4,4}
# print(s)  # No Duplicates in Sets
#
# s1 = set()   # Correct  #  {} creates a dictionary, not a set.
# print(s1)
# s1.add(1)
# print(s1)
# s1.update([4,5,5,6])
# print(s1)
# s1.remove(1)
# print(s1)
# s1.discard(4)
# print(s1)
# s1.clear()
# print(s1)
# s.pop()
# print(s)

# Set Operations ***
s1={1,2,3,4}
s2={3,4,5,6}
print("S1 =",s1)
print("S2 =",s2)
print("Intersection",s1.intersection(s2))
print("Union",s1.union(s2))
print("Difference s1-s2 = ",s1.difference(s2))
print("Difference s2-s1 = ",s2.difference(s1))
print("Difference  ",s1.symmetric_difference(s2))
print(s1.issubset(s2))
print(s1.issuperset(s1.difference(s2)))
print((s1.difference(s2)).issubset(s1.union(s2)))