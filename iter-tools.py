import itertools



counter = itertools.count(start=5,step=5)
data  = [100,200,300,400]


# for i in counter:
    # print(i)
daily_data = list(zip(itertools.count(start=5,step=3),data))

print(daily_data)

counter2  = itertools.repeat(2,times=3)
print(counter2)

for i in counter2:
    print(i)


first    