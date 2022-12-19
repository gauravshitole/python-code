class Demo:
    Value=0
    def __init__(self):
        self.no1=0
        self.no2=0
    def Fun(self):
        print(self.no1)
    def Gun(self):
        print(self.no2)


def main():

    obj1=Demo(11,21)
    obj2=Demo(51,101)
    obj1.Fun()

if __name__ == "__main__":
    main()