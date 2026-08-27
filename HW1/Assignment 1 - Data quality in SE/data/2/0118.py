def sumDigits(n):
    result = 0
    
    while(n != 0):
        result += n % 10
        n //= 10
    
    return result

def main():
    n = int(input('Enter a number between 0 and 1000 : '))
    result = sumDigits(n)
    print('The sum of the digits is', result)

if __name__ == "__main__":
    main()