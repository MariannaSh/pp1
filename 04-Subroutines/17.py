def different(n1,n2,n3):
    if n1!=n2!=n3:
        return True
    else:
        return False
    
n1=int(input('Enter first number: '))
n2= int(input('Enter second number: '))
n3= int(input('Enter third number: '))

print(f'Numbers {n1},{n2},{n3} are different {different(n1,n2,n3)}')