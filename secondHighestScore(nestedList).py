from operator import itemgetter
import sys
if __name__ == '__main__':
    
    nameScore =[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        nameScore.append([name,score])
    if(nameScore.__len__()>5 or nameScore.__len__()<2):
            sys.stderr.write("Input length exceeded")
            sys.exit()   
            

     
    output = sorted(nameScore,key = itemgetter(1))
    
    gotTheSecondMin = False
    score = 0
    final=[]
    
    y = min(output, key =lambda p:p[1])
   
    for item in output:
        
        if(item[1] == y[1]):
            continue  
        if(gotTheSecondMin == False or item[1] == score):
            final.append((item[0]))
            score = item[1]
            gotTheSecondMin =True
        
    
    final.sort()
    
    for items in final:
      print(items)
        