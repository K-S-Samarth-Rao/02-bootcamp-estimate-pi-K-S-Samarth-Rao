import math
import random
import unittest

def wallis(n):                                   # Function to use wallis formula
    product = 1
    for i in range(1,n+1):
        product*= (4*(i**2))/((4*(i**2))-1)     
    return(product*2)                            # Here product will be pi/2
               
    
def monte_carlo(n):
    Points_Circle = 0                            # No. of points inside Circle
    Points_Square = 0                            # No. of points inside Square
    for i in range(1,n+1):
        x = random.random()
        y = random.random()
         
        Dist = x**2 + y**2                       # Distance of point (x,y) from origin (0,0)  
        if ( Dist<=1 ):
           Points_Circle+=1
          
        Points_Square+=1
    pi = 4*(float(Points_Circle)/float(Points_Square))          # Estimating the value of pi
    return pi 
 

class TestWallis(unittest.TestCase):
    def test_low_iters(self):
        for i in range(0, 5):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) > 0.15, msg=f"Estimate with just {i} iterations is {pi} which is too accurate.\n")
            
    def test_high_iters(self):
        for i in range(500, 600):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) < 0.01, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")


class TestMC(unittest.TestCase):
    def test_randomness(self):
        pi0 = monte_carlo(15000)
        pi1 = monte_carlo(15000)
        
        self.assertNotEqual(pi0, pi1, "Two different estimates for PI are exactly the same. This is almost impossible.")

        self.assertFalse(abs(pi0 - pi1) > 0.05, "Two different estimates of PI are too different. This should not happen")

    def test_accuracy(self):
        for i in range(500, 600):
            pi = monte_carlo(i)
            self.assertTrue(abs(pi - math.pi) < 0.4, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")
        
    
if __name__ == "__main__":
    unittest.main()

