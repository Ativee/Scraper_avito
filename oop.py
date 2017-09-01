#
class A:
    def __init__(self):
        self.a = 0

    def set_a(self,new_a):
        self.a = new_a




def main():
    obj_A = A()
    print(obj_A.a)

    obj_A.set_a(3)

    print(obj_A.a)

if __name__ == '__main__':
    main()