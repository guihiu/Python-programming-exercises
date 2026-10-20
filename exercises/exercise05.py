if __name__ == "__main__":

    def Fatorial(num):
        fatorial=1
        for i in range(1,num+1):
            fatorial=fatorial*(i)
            print(fatorial)
        return fatorial
    
    print((Fatorial(5)))

