if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    query_list = student_marks[query_name]
    ans = round(sum(query_list)/3,3)
    print(f"{ans:.2f}")
