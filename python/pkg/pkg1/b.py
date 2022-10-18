from unicodedata import name


def func2() :
    print('func2')

class Person : 
    national = 'korea'

    #생성자
    def __init__(self,name,age) :
        print('생성자 호출2')
        self.name = name
        self.age = age

    def study(self) :
        print('{}이(가) 공부하다 나이:{}'.format(self.name,self.age))

    def eat(self) :
        print('먹다')

    def print_info(self) :
        print('이름:{}, 나이:{}'.format(self.name,self.age))

    #소멸
    def __del__(self) :
        print('Person 객체 소멸')

class Student(Person) :
    def __init__(self,name,age,no) :
        #self.name = name
        #self.age = age
        Person.__init__(self,name,age) #부모생성자 호출
        self.no = no

    def sleep(self) :
        print('잠자다')

    #메소드 재정의
    def print_info(self) :
        super().print_info()    #부모 멤버 접근시 super().
        print('학번:{}'.format(self.no))
        #print('이름:{}, 나이:{}, 학번:{}'.format(self.name,self.age,self.no))

    #소멸
    def __del__(self) :
        print('Student 객체 소멸')    

