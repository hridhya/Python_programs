def lonelyinteger(a):
    answer = 0
    for integer in a:
        answer = answer^integer
        
    return answer
if __name__ == '__main__':
    a = input()
    b = map(int, raw_input().strip().split(" "))
    print lonelyinteger(b)
