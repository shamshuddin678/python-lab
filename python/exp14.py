feet = int(input("Enter feet: "))
while(True):
    option = int(input("Enter option to perform conversion: \n1.inches \n2.yards \n3.miles \n4.milli meters \n5.centi meters \n6.meters \n7.kilometers \n"))
    match option:
        case 1:
           r=feet*12
           print(f"the feet to inches is {r}")
        case 2:   
           r=feet/3.0
           print(f"the feet to yards is {r}")
        case 3:   
           r=feet/5280.0
           print(f"the feet to miles is{r}")
        case 4:   
           r=feet*304.8
           print(f"the feet to milli meters is {r}")
        case 5:   
           r=feet*30.48
           print(f"the feet to centi meters is {r}")
        case 6:   
           r=feet*0.3048
           print(f"the feet to meters is {r}")
        case 7:   
           r=feet*0.0003048
           print(f"the feet to kilo meters is {r}")
        case 8:
          break