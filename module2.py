#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Shashwat Choudhary
#
# Created:     25-07-2024
# Copyright:   (c) Shashwat Choudhary 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import datetime
import calendar
import math
t=datetime.datetime.today();
print(t.date());
print(calendar.calendar(2024,1,1,1));
r=int(input("enter-radius"));
area=math.pi*r*r;
print("Area of circle",area);