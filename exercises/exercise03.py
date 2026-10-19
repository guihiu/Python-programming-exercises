if __name__ == "__main__":

    num=10
    vet = []
    for i in range(num, 0, -1):
        vet.append(str(i) + "-" + str(i*i))
        print(str(i) + " elevate to 2 is equal to:" + str(i*i))
    print(vet)