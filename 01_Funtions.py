def percent(marks):
    return(sum(marks)/400 *100)
# return ((marks[0]+marks[1]+marks[2]+marks[3])/400)*100  these statement can also be used 



marks = [45,75,86,77]
percentage1 = percent(marks)


marks2 = [75,98,88,78] 
percentage2 = percent(marks2)
print (percentage1, percentage2)