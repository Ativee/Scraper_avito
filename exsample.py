def method_for_simple(self, x, y):
 return x + y

class Simple:
 f = method_for_simple



def main():
    s = Simple()
    print(s.f(1,2))

if __name__ == '__main__':
    main()