def nuclear_core_unstable():
    print "NUCLEAR CORE UNSTABLE!!! \n" \
          "Quarantine is in effect \n" \
          "Surrounding hamlets will be evacuated. \n" \
          "Anti-radiationsuits and iodine pills are mandatory."

nuclear_core_unstable()


def hello_func(greeting):
    return '{}'.format(greeting)

print (hello_func("hi"))


def hello_func2(greeting, name="you"): #to print even without the argument
    return '{}, {}'.format(greeting, name)

print (hello_func2("hello", name="Corey"))
print (hello_func2("hello"))

def student_info(*args, **kwargs): #convention
    print(args)
    print(kwargs) #keyword argument

student_info('math', 'art', name='john', age=22)

courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}

student_info(*courses, **info)