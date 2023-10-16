import sys

def classify_triangle(a,b,c):
    orderedsides=[a,b,c]
    orderedsides.sort(reverse=True)    
    if  (orderedsides[-1]<=0) or (orderedsides[0]>(orderedsides[1]+orderedsides[2])):
        return "Not a triangle"
    if a==b==c:
        return "Equilateral"
    elif a==b or b==c or c==a:
        return "Isosceles"
    elif (orderedsides[0]**2)==((orderedsides[1]**2)+(orderedsides[2]**2)):
        return "Right"
    else:
        return "Scalene"
    
def runClassifyTriangle(a,b,c):
    print(classify_triangle(a,b,c))


runClassifyTriangle(0,5,5)
runClassifyTriangle(10,10,10)
runClassifyTriangle(5,6,7)
runClassifyTriangle(2,3,3)