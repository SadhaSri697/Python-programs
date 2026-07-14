s = set()
s.add(20) 
s.add(20.0)
s.add("20")
print(s)  #out put is 20 , '20' 
          # because 20==20.0
print(len(s))          
