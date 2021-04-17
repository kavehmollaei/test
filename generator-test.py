
from itertools import islice
from os import name
import time,random
import memory_profiler as mem_profile

names = ["A","B","C","D","e","f"]
majors = ["egg","monday","Com","thursday","bot"]


print(f'Memory (Before) do func: {mem_profile.memory_usage()}Mb')

@mem_profile.profile
def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
            "id":i,
            "name":random.choice(names),
            "major":random.choice(majors)

        }


        result.append(person)
    return result    


# @mem_profile.profile
def people_generator(num_people):
    for i in range(num_people):
        person = {
            "id":i,
            "name":random.choice(names),
            "major":random.choice(majors)
        }

        yield person    
@mem_profile.profile
def my_func():
    a = [1] * (10 ** 6)
    b = [2] * (2 * 10 ** 7)
    del b
    return a



t1=time.time()
people_list(10000)
t2=time.time()

# t1=time.time()
# people_generator(10000000)
# t2=time.time()
# my_func()


print('Memory (After): {} MB'.format(mem_profile.memory_usage()))
print ('Took {} seconds'.format(t2-t1))











"""


def show (num):
    print("Starting")
    while num > 0:
        yield num
        num -=1



even_nums = (x for x in range(100000) if x %2 ==0)
# print(next(even_nums))
print(list(even_nums))


# lst = [ part for part in islice(even_nums,3)]
    
# print(lst)
# lst.append(next(even_nums))
# lst.append(next(even_nums))
# lst.append(next(even_nums))
# print(lst)

def 

"""


