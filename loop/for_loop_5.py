
# * patterns
'''
1. Filled Square 
row = 4 , column = 4 
* * * *
* * * *
* * * *
* * * *
'''
row = 4
column = 4

for i in range(row):  # * will start from 0 and end at row-1 (3)
    for j in range(column):  # * will start from 0 and end at column-1 (3)
        print("* ", end="")
    print()

print()

'''
2. Left Aligned Right Angle Triangle
row = 4          i
*         -> row 1    
* *       -> row                      
* * *     -> row 3            
* * * *   -> row 4          
'''
row = 4

for i in range(row):
    for j in range(i+1):
        print("* ", end="")
    print()

print()

'''
3. Inverted Left Aligned Right Angle Triangle
row = 4          i
* * * *   -> row 4         
* * *     -> row 3            
* *       -> row 2                        
*         -> row 1    
'''
row = 4

for i in range(row, 0, -1):
    for j in range(i):  # * will start from 0 and end at i-1
        print("* ", end="")
    print()

'''
4. Left Aligned Right Angle Triangle
row = 4          i
1         -> row 1    
2 2       ->                       
3 3 3     -> row 3            
4 4 4 4   -> row 4
'''

'''
5. Left Aligned Right Angle Triangle
row = 4          i
1         -> row 1    
1 2       -> row 2                 
1 2 3     -> row 3            
1 2 3 4   -> row 4
'''

'''
6. Upper Pyramid  -> Space + left aligned right angle triangle 
row = 5                           row - i
    *      -> row 1   ->   4 ->   5 - 1 
   * *     -> row 2   ->   3 ->   5 - 2          
  * * *    -> row 3   ->   2 ->   5 - 3    
 * * * *   -> row 4   ->   1 ->   5 - 4    
* * * * *  -> row 5   ->   0 ->   5 - 5  
'''

row = 5

for i in range(1, row+1):
    # * space
    for k in range(1, row-i+1):  # * 0 to row-i-1
        print(" ", end="")

    # * stars
    for j in range(1, i+1):
        print("* ", end="")
    print()

print()

'''
7. Lower Pyramid  -> Space + left aligned right angle triangle 
row = 5                           row - i
* * * * *  -> row 5   ->   0 ->   5 - 5  
 * * * *   -> row 4   ->   1 ->   5 - 4    
  * * *    -> row 3   ->   2 ->   5 - 3    
   * *     -> row 2   ->   3 ->   5 - 2          
    *      -> row 1   ->   4 ->   5 - 1 
'''

row = 5

for i in range(row, 0, -1):
    # * space
    for k in range(row-i):  # * 0 to row-i-1
        print(" ", end="")

    # * stars
    for j in range(i):
        print("* ", end="")
    print()

print()

# * 8. diamond - UPPER PYRAMID + LOWER PYRAMID 
# * 9. HOUR GLASS - LOWER PYRAMID + UPPER PYRAMID

