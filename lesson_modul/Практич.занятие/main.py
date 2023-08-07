#import module_a
#import module_b


#print(module_a.add(23, 34))
#print(module_b.mul(2, 3))


import packade1.module_a as mda1

if __name__=='main':
    print(mda1.add(1, 2))
    print(mda1.mul(1, 2))
    print(__name__)

       