
#Roman numerals are: [i v x l c d m]

def stringer (x):
  number_string = str(x)
  a = number_string[0]
  b = number_string[1] 
  c = number_string[2] 
  d = number_string[3] 


a_list = [ "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
b_list = [ "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
c_list = [ "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
d_list = [ "M", "MM", "MMM"]


x = int(input("Your Number(up to 3999):  "))
stringer
print (d_list[d-1] + c_list[c-1] + b_list[b-1] + a_list[a-1] )





 
    
    
    

