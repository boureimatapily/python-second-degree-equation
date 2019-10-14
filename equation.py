#import module
import os
from math import *
# we are going to solve a secind degree equaation in Pyton
#function second_degree

def second_degree_equation(a,b,c):
	if a!=0:
		print("Second degree Equation")
		d=((b*b) - (4*a*c)) 
		print("delta d = ",+d,)
		if d > 0:
			x1 = ((b*b) - sqrt(d)) / 2*a
			x2 = ((b*b) + sqrt(d))/ 2*a
			print("solution x1 = ",+x1," and x2 = ",+x2)
		elif d == 0:
			print("delta d = ", +d)
			x = (b*b) / 2*a
			print(" Solution x = ", +x)
		else :
			print(" Delta is less than 0, no solution")
	elif a==0 and b!=0:
		print("First degree equaation")
		x = (-c) / b
		print(" solution x = ", +x)
	else:
		print("no solution ")

print(" Hello we are going to solve a second degree equation like a(X*X)+bX +c")
print(" Where a,b,c are variable, we are going to ask you to enter them ")
a1=float(input("Enter your variable a "))
b1=float(input("Enter your variable b "))
c1=float(input("Enter your variable c "))

solve = second_degree_equation(a1,b1,c1)

os.system("pause")





	

