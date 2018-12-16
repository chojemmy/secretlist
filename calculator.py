#!/usr/bin/env python3
import sys

def gongzi():
    l = [i.split(':') for i in sys.argv[1:]]
    for id, salary in l:
        salary = int(salary)
        jiao = salary * 0.165 
        x = salary - jiao - 3500
        if x <= 0:
            tax = 0
        elif x <= 1500:
            tax = x * 0.03
        elif x <= 4500:
            tax = x * 0.1 - 105
        elif x <= 9000:
            tax = x * 0.2 - 555
        elif x <= 35000:
            tax = x * 0.25 - 1005
        elif x <= 55000:
            tax = x * 0.3 - 2755
        elif x <= 80000:
            tax = x * 0.35 - 5505
        else:
            tax = x * 0.45 - 13505
        print("{}:{:.2f}".format(id, tax))
    
if __name__ == '__main__':
    gongzi()
