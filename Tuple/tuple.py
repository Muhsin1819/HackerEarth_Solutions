import builtins as built

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    
    t = tuple(integer_list)
    print(built.hash(t))
