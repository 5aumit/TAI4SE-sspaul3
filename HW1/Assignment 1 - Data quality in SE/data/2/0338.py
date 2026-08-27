#!/root/ysy/python/bin/python3
'''myerror
trigger error
'''

def age_fun1(name,age):
    if not 1 < age < 120:
        raise ValueError("age out of range")
    print("%s is %s years old"%(name,age))

def age_fun2(name,age):
    assert 1 < age < 120,"age out of range too"
    print("%s is %s years old" % (name, age))

if __name__ == '__main__':
    name = input('name:')
    age = int(input('age:'))
    age_fun1(name,age)
    age_fun2(name,age)