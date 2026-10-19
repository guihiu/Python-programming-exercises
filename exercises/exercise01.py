if __name__ == "__main__":

    def DivBy7(num):
        if num % 7 == 0:
            return True
        else:
            return False

    def DivBy5(num):
        if num % 5 == 0:
            return True
        else:
            return False

    vet = []

    for i in range(2000, 3200):
        if DivBy7(i) and not DivBy5(i):
            print("Divisible by both 7 and not 5:", i)
            vet.append(i)

    print("Numbers divisible by both 7 and not 5:", vet)