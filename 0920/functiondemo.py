def calc_sum(start, end):
    sum = 0

    for i in range(start, end+1):
        sum += i
    
    print(' %d부터 %d까지의 합은 %d 입니다.'%(start,end, sum))
    
    
start = 50
end = 100000

calc_sum(start, end) #인자, 인수, Argument    
calc_sum(2, 7989)   #함수의 호출, Call by Name
calc_sum(45, 8989)
