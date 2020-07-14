# --------------
import pandas as pd
import numpy as np
import math


#Code starts here
class complex_numbers:
    def __init__(self,a,b):
        self.real=a
        self.imag=b
    def __repr__(self):

        if self.real == 0.0 and self.imag == 0.0:
            return "0.00"
        if self.real == 0:
            return "%.2fi" % self.imag
        if self.imag == 0:
            return "%.2f" % self.real
        return "%.2f %s %.2fi" % (self.real, "+" if self.imag >= 0 else "-", abs(self.imag))
    def __add__(self,other):
        ans=complex_numbers((self.real+other.real),(self.imag+other.imag))
        return ans
    def __sub__(self,other):
        ans=complex_numbers((self.real-other.real),(self.imag-other.imag))
        return ans
    def __mul__(self,other):
        ans=complex_numbers((self.real*other.real-self.imag*other.imag),(self.imag*other.real+self.real*other.imag))
        return ans
    def __truediv__(self,other):
        a1=self.real
        b1=self.imag
        a2=other.real
        b2=other.imag
        a=(a1*a2+b1*b2)/(a2**2 + b2**2)
        b=(b1*a2-a1*b2)/(a2**2 + b2**2)
        return complex_numbers(a,b)
    def absolute(self):
        ans=math.sqrt(self.real**2 + self.imag**2)
        return ans
    def argument(self):
        ans=math.degrees(math.atan2(self.imag,self.real))
        return ans
    def conjugate(self):
        if self.imag<0:
            return complex_numbers(self.real,abs(self.imag))
        return complex_numbers(self.real,-(self.imag))
comp_1=complex_numbers(3,5)
comp_2=complex_numbers(4,4)
comp_sum=comp_1+comp_2
comp_diff=comp_1-comp_2
comp_prod=comp_1*comp_2
comp_quot=comp_1/comp_2
comp_abs=comp_1.absolute()
comp_conj=comp_1.conjugate()
comp_arg=comp_1.argument()



