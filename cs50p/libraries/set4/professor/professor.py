from random import randint

problems = []

def main():
    get_level()


def get_level():
    try:
        digits = int(input("Level: "))
        if 0 < digits < 4:
            generate_problems(digits)
        else:
            print("must be a number between 1 and 3")
            get_level()

    except ValueError:
        print("must be a number between 1 and 3")
        get_level()
            

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    rnum1=randint(range_start, range_end)
    rnum2=randint(range_start, range_end)
    prob=(f"{str(rnum1)}+{str(rnum2)}")
    return prob
    
def generate_problems(digit):
    for problem in range(10):
      problems.append(random_with_N_digits(digit))  

    print(problems) 

if __name__ == "__main__":
    main()