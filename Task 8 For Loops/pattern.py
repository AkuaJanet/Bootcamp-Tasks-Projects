# Create a variable called 'star' and assign it the symbol '*'

star = "*"

'''Determine the condition for the star pattern. 
In each iteration, i assumes the values 1,2, 3.....9 respectively
and follows the if condition accordingly. 
When i assumes the value 6, it skips the if condition because it is no longer true 
and follows the else condition instead''' 

for i in range(1,10):

    if i <= 5:                
        print(i * star)
    
    else:
        print((10 - i) * star) 
