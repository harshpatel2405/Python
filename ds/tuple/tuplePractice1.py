'''
A travel company stores the seat numbers of passengers in a tuple because confirmed reservations should not change accidentally.

Current reserved seats:
(1, 3, 5, 7, 9, 11, 13, 15)
A passenger cancels seat 7, and a new passenger books seat 8.

Requirements
    Store reserved seats in a tuple.
    Remove seat 7.
    Add seat 8.
    Convert the tuple into a list to perform updates.
    Convert it back to a tuple after modification.
    Display:
    Original tuple
    Updated tuple
    Total reserved seats
    Whether seat 8 is successfully reserved.
'''
seats = (1, 3, 5, 7, 9, 11, 13, 15)

seats = list(seats)
print("Original Tuple :",seats)

for i in range(len(seats)):
    if(seats[i] == 7):
        seats[i] = 8

seats = tuple(seats)
print("Updated Tuple :",seats)
