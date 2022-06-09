from BracketOrder import is_valid_input, bracket_order_control




print('Enter Brackets : ')
text = input()

if is_valid_input(text):
    if bracket_order_control(text):
        print('YES')
    else:
        print('NO')
else:
    print("invalid input, input should be  in these ['{','}','(',')','[',']'] brackets" )




            

