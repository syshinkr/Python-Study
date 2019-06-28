import random

def testing():
    result = [random.randrange(1, 5, 1) for i in range(6)]
    print(str(result))

if __name__ == "__main__":
    testing()
