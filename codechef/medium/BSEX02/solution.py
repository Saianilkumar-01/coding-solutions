import math

def main():
    
    # Write your code here
    t = int(input())
    for _ in range(t):
        n = int(input())
        k = int((math.sqrt(1 + 8 * n)-1)/2)
        print(k)
if __name__ == "__main__":
    main()
