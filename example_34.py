#题目：练习函数调用

def hello_world():
    print('Hello world')

def three_hello():
    for i in range(3):
        hello_world()

if __name__ == '__main__':
    three_hello()
