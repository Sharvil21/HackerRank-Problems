#First solution with sorting and set function
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    ans = sorted(set(list(arr).copy()))
    print(ans[-2])

#Second Solution
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    print(sorted(set(arr))[-2])    

