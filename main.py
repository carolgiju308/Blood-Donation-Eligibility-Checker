#Blood donation eligibility checker
age=int(input('Enter your age:'))

if age>=18:
    weight=float(input('Enter your weight:'))
  
    if weight>=50:
       print('You are eligible!!')
    else:
       print('You do not meet the minimum weight requirement.')
else:
    print('You do not fit into the required age criteria.')
    
    

