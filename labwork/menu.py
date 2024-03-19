count_in = 0
count_speeding = 0
count_not_speeding = 0
fine = 0
while(True):
    u_in = input("Enter the speed or 'end'")

    if u_in.upper() == 'END':
        break
    else:
        count_in = count_in + 1
        if float(u_in) <= 60:
            count_not_speeding = count_not_speeding + 1
        elif float(u_in) <= 65:
            count_speeding = count_speeding + 1
        elif float(u_in) <= 70:
            count_speeding = count_speeding + 1
            fine = fine + 100
        elif float(u_in) <= 80:
            count_speeding = count_speeding + 1
            fine = fine + 200
        else:
            count_speeding = count_speeding + 1
            fine = fine + 500

per_speed = (float(count_speeding())/count_in) * 100
print('The percentage of speeding vehicle : ' + str(per_speed) + '%')
print('Fine : ' + fine)




