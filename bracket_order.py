dic  = {'(':')','{':'}','[':']'}

# input validation
def is_valid_input(text):

    chars = ['{','}','(',')','[',']']  
    if not text:
        return False
    for char in text:
        if char not in chars:
            return False
    return True

# bracket order control

def bracket_order_control(text):

    stack = []
    for char in text:
        if char  in  dic.keys(): 
            stack.append(char)
        elif not stack:
            return False
        else: 
            if char != dic[stack.pop()] :
                return False

    if stack:
         return False
    else: 
        return True


