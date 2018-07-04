import sys
if __name__ == '__main__':
    n = int(input())
    if(n>10 or n<2):
        sys.stderr.write("Input data n out of range")
        sys.exit()
  
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    
    scores = student_marks.__getitem__(query_name)
    
    count = 0.00
    total = 0.00
    for i in scores:
        if(i<0 or i > 100):
            sys.stderr.write("Marks out of range")
            sys.exit()
        total = total + i
        count = count + 1
    
    per = total/count
    
   # print(round(per,2))
    print("%.2f" % per)