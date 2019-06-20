opening = "("
closing = ")"

def utility(n,  length, parentheses = "", opened = 0, ):
    if n == 0:
        parentheses = parentheses + closing*(length - len(parentheses))
        print(parentheses)
        return

    if opened:
        utility(n, length, parentheses=parentheses + closing, opened=opened-1)
        utility(n - 1, length, parentheses=parentheses+opening, opened=opened+1)
    else:
        utility(n - 1, length, parentheses=parentheses + opening, opened=opened + 1)

    return

def generate_parentheses(n):
    if n == 0:
        return
    else:
        utility(n, 2*n)

if __name__ == "__main__":
    n = int(input())
    generate_parentheses(n)
