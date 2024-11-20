from random import randint
problems = []
score=0

def main():
    get_level()
    solve_problems(problems,score)
    print(score)
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
    return problems

def solve_problems(arr,tracker):
    for prob in arr:
        num1,num2 = prob.split("+")
        results=int(num1)+int(num2)
        print(prob)
        tracker =get_answer(results,tracker)
    return tracker

def get_answer(a,tracker):
    x=0
    while True:
       
        answer = int(input("answer: "))
        if answer == a:
                tracker +=1
                break
        else:
                print("EEE")
                x+=1
                print(x)
                if x==3:
                    print(f"the answer is : {a}")
                    break
        return tracker
    


if __name__ == "__main__":
    main() 