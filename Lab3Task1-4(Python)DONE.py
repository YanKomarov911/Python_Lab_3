import timeit
import sys
#Task 1
print("=" * 16, "Task 1", "=" * 16, "\n")
sp = [1, 2, 3, 4, 5, 6]
kort = (1, 2, 3, 4, 5, 6)
print(type(sp), type(kort), id(sp), id(kort))
sp.remove(4)
sp.append(67)
print(id(sp), id(kort))
kort2 = (1, 2, 3, 4, 52, 6)
print(id(kort), id(kort2), "\n")

#Task 2
print("=" * 16, "Task 2", "=" * 16, "\n")
Bell = [1, 2, 2, 7, 5, 5, 78, 56, 13, 13, 24, 45]
Setted_Bell = set(Bell)
print(len(Bell), len(Setted_Bell))
print(Bell)
print(Setted_Bell)
print()

#Task 3
print("=" * 16, "Task 3", "=" * 16, "\n")
SP, SP2 = [4, 5, 6], [1, 2, 3, 4, 5, 6, 7 ,8]
MN, MN2 = {4, 5 ,6}, {1, 2, 3, 4, 5, 6, 7 ,8}
SP3 = [x for x in range(1001)]
MN3 = set([])
k = 0
def Adder():
    global k
    MN3.add(k)
    k += 1
    if k < 1001:
        Adder()
    return 0
Adder()
print(timeit.timeit(stmt ='4 in SP', globals=globals(), number=1000000))
print(timeit.timeit(stmt ='1 in SP', globals=globals(), number=1000000))
print(timeit.timeit(stmt ='4 in MN', globals=globals(), number=1000000))
print(timeit.timeit(stmt ='1 in MN', globals=globals(), number=1000000))
print()
print(timeit.timeit(stmt ='4 in SP2', globals=globals(), number=1000000))
print(timeit.timeit(stmt ='10 in SP2', globals=globals(), number=1000000))
print(timeit.timeit(stmt ='4 in MN2', globals=globals(), number=1000000))
print(timeit.timeit(stmt ='10 in MN2', globals=globals(), number=1000000))
print()
print(timeit.timeit(stmt ='4 in SP3', globals=globals(), number=1000000))
print(timeit.timeit(stmt ='1004 in SP3', globals=globals(), number=1000000))
print(timeit.timeit(stmt ='4 in MN3', globals=globals(), number=1000000))
print(timeit.timeit(stmt ='1004 in MN3', globals=globals(), number=1000000))
print()

#Task 4
print("=" * 16, "Task 4", "=" * 16, "\n")
GoldLaneSetup = dict([("main", "Lesley"), ("build", "Critical DMG")])
print(GoldLaneSetup["main"], "\n")
Spis = ["farm", "Lesley"]
Kort5 = ("towers", "bind")
Setting = {"towers", "line"}
print(sys.getsizeof(GoldLaneSetup))
print(sys.getsizeof(Spis))
print(sys.getsizeof(Kort5))
print(sys.getsizeof(Setting))



















