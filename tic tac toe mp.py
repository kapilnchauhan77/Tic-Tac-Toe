'''
       |       |
   O   |   X   |   O
_ _ _ _|_ _ _ _|_ _ _ _
       |       |
   O   |   X   |   O
_ _ _ _|_ _ _ _|_ _ _ _
       |       |
   X   |   O   |   X
       |       |
'''
a1=a2=a3=b1=b2=b3=c1=c2=c3=' '
print ('')
print ('TIC-TAC-TOE \n')
play1=input('Player 1 : ')
play2=input('Player 2 : ')
print ('')
print (play1,', your symbol is : O \nSo,',play2,'your symbol is : X \n')
a=input('Press enter to continue... \n')
print ('Here is the grid of TIC-TAC-TOE')

def base():
    print (' _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n|       |                       | \n|   *   |  ','A','     ','B','     ','C','  | \n|_ _ _ _|_ _ _ _ _ _ _ _ _ _ _ _| \n|       |       |       |       | \n|   1   |  ',a1,'  |  ',b1,'  |  ',c1,'  | \n|       |_ _ _ _|_ _ _ _|_ _ _ _| \n|       |       |       |       | \n|   2   |  ',a2,'  |  ',b2,'  |  ',c2,'  | \n|       |_ _ _ _|_ _ _ _|_ _ _ _| \n|       |       |       |       | \n|   3   |  ',a3,'  |  ',b3,'  |  ',c3,'  | \n|_ _ _ _|_ _ _ _|_ _ _ _|_ _ _ _| \n')
                     
base()

print ('You need to locate the position by its COLUMN-ROW \nFor example: a1 \n')
b=input('Press enter to begin !!!')

def p1():
    space()
    base()
    check1()
 
def p2():
    space2()
    base()
    check2()
    
def space():
    print ('')
    print (play1,',')
    global x
    x=input('Your turn : ')
    if x=='a1':
        if a1=='O':
            print ('THAT SLOT ISN\'T VACCANT !')
            print ('')
            space()
        elif  a1=='X':
            print ('THAT SLOT ISN\'T VACCANT !')
            print ('')
            space()
        else:
            con()
    elif x=='a2':
        if a2=='O':
            print ('THAT SLOT ISN\'T VACCANT !')
            print ('')
            space()
        elif  a2=='X':
            print ('THAT SLOT ISN\'T VACCANT !')
            print ('')
            space()
        else:
            con()
    elif x=='a3':
        if a3=='O':
            print ('THAT SLOT ISN\'T VACCANT !')
            print ('')
            space()
        elif  a3=='X':
            print ('THAT SLOT ISN\'T VACCANT !')
            print ('')
            space()
        else:
            con()
    elif x=='b1':
        if b1=='O':
            print ('THAT SLOT ISN\'T VACCANT !')
            print ('')
            space()
        elif  b1=='X':
            print ('THAT SLOT ISN\'T VACCANT !')
            print ('')
            space()
        else:
            con()
    elif x=='b2':
        if b2=='O':
            print ('THAT SLOT ISN\'T VACCANT !')
            print ('')
            space()
        elif  b2=='X':
            print ('THAT SLOT ISN\'T VACCANT !')
            print ('')
            space()
        else:
            con()
    elif x=='b3':
        if b3=='O':
            print ('THAT SLOT ISN\'T VACCANT !')
            print ('')
            space()
        elif  b3=='X':
            print ('THAT SLOT ISN\'T VACCANT !')
            print ('')
            space()
        else:
            con()
    elif x=='c1':
        if c1=='O':
            print ('THAT SLOT ISN\'T VACCANT !')
            print ('')
            space()
        elif  c1=='X':
            print ('THAT SLOT ISN\'T VACCANT !')
            print ('')
            space()
        else:
            con()
    elif x=='c2':
        if c2=='O':
            print ('THAT SLOT ISN\'T VACCANT !')
            print ('')
            space()
        elif  c2=='X':
            print ('THAT SLOT ISN\'T VACCANT !')
            print ('')
            space()
        else:
            con()
    elif x=='c3':
        if c3=='O':
            print ('THAT SLOT ISN\'T VACCANT !')
            print ('')
            space()
        elif  c3=='X':
            print ('THAT SLOT ISN\'T VACCANT !')
            print ('')
            space()
        else:
            con()
    else :
        print ('ENTER A VALID LOCATION !')
        print ('(CAPS LOCK must be OFF)')
        print ('')
        space()

def space2():
    print ('')
    print (play2,',')
    global y
    y=input('Your turn : ')
    if y=='a1':
        if a1=='O':
            print ('THAT SLOT ISN\'T VACCANT !')
            print ('')
            space2()
        elif  a1=='X':
            print ('THAT SLOT ISN\'T VACCANT !')
            print ('')
            space2()
        else:
            con2()
    elif y=='a2':
        if a2=='O':
            print ('THAT SLOT ISN\'T VACCANT !')
            print ('')
            space2()
        elif  a2=='X':
            print ('THAT SLOT ISN\'T VACCANT !')
            print ('')
            space2()
        else:
            con2()
    elif y=='a3':
        if a3=='O':
            print ('THAT SLOT ISN\'T VACCANT !')
            print ('')
            space2()
        elif  a3=='X':
            print ('THAT SLOT ISN\'T VACCANT !')
            print ('')
            space2()
        else:
            con2()
    elif y=='b1':
        if b1=='O':
            print ('THAT SLOT ISN\'T VACCANT !')
            print ('')
            space2()
        elif  b1=='X':
            print ('THAT SLOT ISN\'T VACCANT !')
            print ('')
            space2()
        else:
            con2()
    elif y=='b2':
        if b2=='O':
            print ('THAT SLOT ISN\'T VACCANT !')
            print ('')
            space2()
        elif  b2=='X':
            print ('THAT SLOT ISN\'T VACCANT !')
            print ('')
            space2()
        else:
            con2()
    elif y=='b3':
        if b3=='O':
            print ('THAT SLOT ISN\'T VACCANT !')
            print ('')
            space2()
        elif  b3=='X':
            print ('THAT SLOT ISN\'T VACCANT !')
            print ('')
            space2()
        else:
            con2()
    elif y=='c1':
        if c1=='O':
            print ('THAT SLOT ISN\'T VACCANT !')
            print ('')
            space2()
        elif  c1=='X':
            print ('THAT SLOT ISN\'T VACCANT !')
            print ('')
            space2()
        else:
            con2()
    elif y=='c2':
        if c2=='O':
            print ('THAT SLOT ISN\'T VACCANT !')
            print ('')
            space2()
        elif  c2=='X':
            print ('THAT SLOT ISN\'T VACCANT !')
            print ('')
            space2()
        else:
            con2()
    elif y=='c3':
        if c3=='O':
            print ('THAT SLOT ISN\'T VACCANT !')
            print ('')
            space2()
        elif  c3=='X':
            print ('THAT SLOT ISN\'T VACCANT !')
            print ('')
            space2()
        else:
            con2()
    else:
        print ('ENTER A VALID LOCATION !')
        print ('(CAPS LOCK must be OFF)')
        print ('')
        space2()

def con():
    global x
    if x=='a1':
        global a1
        a1='O'
    elif x=='a2':
        global a2
        a2='O'
    elif x=='a3':
        global a3
        a3='O'
    elif x=='b1':
        global b1
        b1='O'
    elif x=='b2':
        global b2
        b2='O'
    elif x=='b3':
        global b3
        b3='O'
    elif x=='c1':
        global c1
        c1='O'
    elif x=='c2':
        global c2
        c2='O'
    elif x=='c3':
        global c3
        c3='O'
  
def con2():
    global y
    if y=='a1': 
        global a1
        a1='X'
    elif y=='a2':
        global a2
        a2='X'
    elif y=='a3':
        global a3
        a3='X'
    elif y=='b1':
        global b1
        b1='X'
    elif y=='b2':
        global b2
        b2='X'
    elif y=='b3':
        global b3
        b3='X'
    elif y=='c1':
        global c1
        c1='X'
    elif y=='c2':
        global c2
        c2='X'
    elif y=='c3':
        global c3
        c3='X'

def check1():
    if a1==a2==a3=='O'or b1==b2==b3=='O'or c1==c2==c3=='O'or a1==b1==c1=='O'or a2==b2==c2=='O'or a3==b3==c3=='O'or a1==b2==c3=='O'or a3==b2==c1=='O':
        print (play1,' wins !!!')
    else:
        p2()
def check2():
    if  a1==a2==a3=='X'or b1==b2==b3=='X'or c1==c2==c3=='X'or a1==b1==c1=='X'or a2==b2==c2=='X'or a3==b3==c3=='X'or a1==b2==c3=='X'or a3==b2==c1=='X':
        print (play2,' wins !!!')
    else:
        p1()

p1()
