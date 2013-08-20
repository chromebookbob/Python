print (5 * '-' ),
print ( " WELCOME ")
print (5 * '-' )

print ("""
Please fill in the numbers when prompted:
We 1. sports and we don't 2. who knows.
A 3. by lonely 4.

""")
a1 = raw_input( "1." )

b1 = raw_input( "2." )

c1 = raw_input( "3." )
 
d1 = raw_input( "4." )

print ( """

Thanks!
You said:
We %s sports and we don't %s who knows.
A %s by lonely %s

Well Done! 

""" ) % ( a1, b1, c1, d1 )