#def string_test(s):
 #    if len(s)>2:
  #      print('True')
   #     if 0==-1:
    #        print('True')

    #else:
     #   print('False')

def string_test(s):
    if len(s) > 2 and s[0] == s[-1]:
        return True
    else:
        return False
    
def add_x(s):
    x='1'
    x=x+s
    return x
        
    
       
