from Encapsulation import Person


class Main:

    if __name__=="__main__":
        p = Person(30000000, 400, True)
        p.networth
        print(p.networth)
        p.__networth = 3423
