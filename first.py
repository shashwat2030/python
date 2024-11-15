#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Shashwat Choudhary
#
# Created:     25-07-2024
# Copyright:   (c) Shashwat Choudhary 2024
# Licence:     <your licence>
#-----------------------------------------------------------------------------
print("enter basic pay")

basic_pay=int(input())

hra =0.4*basic_pay
da=0.2*basic_pay
ga=basic_pay+hra+da
print(ga)

