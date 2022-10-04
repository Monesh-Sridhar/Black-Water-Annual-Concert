while True:
    print("Blackwater Annual Music Concert")
    print("-------------------------------")
    choice = int(input("1. Adding performers\n2. Generate concert details\n3. Quit\nPlease select a number between 1 and 3:"))
    if choice ==1:
        datafile = open("performers.txt", "a")
        i = 1
        performance_1 = "Musical"
        performance_2 = "Singer"
        performance_3 = "Dancer"
        count_1 = 0
        count_2 = 0
        count_3 = 0
        total_time = 0
        max = 0
        HOUR = 60
        line_3 = ""
        cline = ""
        print(f"({choice}) Adding Performers")
        print("------------------------------")
        performers = int(input("How many performers are you adding:"))
        while i <= performers:
            print(f"Booking {i}/{performers}:")
            name = input("Enter your name:")
            sur_name = input("Enter your surname:")
            print("Type of Performance")
            menu = int(input("1. Musical\n2. Singer\n3. Dancer\n Please enter a number between 1 and 3:"))
            if menu == 1:
                performance_type = performance_1
                count_1 = count_1 + 1
            elif menu == 2:
                performance_type = performance_2
                count_2 = count_2 + 1
            elif menu == 3:
                performance_type = performance_3
                count_3 = count_3 + 1
            time = int(input("Time slot required (mins):"))
            if time > max:
                max = time
                performance_type_1 = performance_type
                name_1 = name
                sur_name_2 = sur_name
            line_1 = (f"The longest act added is {name_1} {sur_name_2}({performance_type_1}) {max} minutes.")
            total_time = total_time + time
            time_in_hour = (total_time // HOUR)
            time_in_miutes = (total_time % HOUR)
            line = (f"{i}. {sur_name},{name:15}{performance_type:6}{time:5} minutes")
            cline = cline + line
            line_2 = (f"{sur_name} {name} {performance_type} {time}")
            line_3 = line_3 + line_2
            if i != performers:
                cline = cline + "\n"
                line_3 = line_3 + "\n"
            i = i + 1
        print(line_3, file=datafile)
        datafile.close()
        print("The following information has been added.")
        print(cline)
        print("Summary Notes:")
        print("--------------")
        print(f"{count_1} Musicians")
        print(f"{count_2} Singer")
        print(f"{count_3} Dancer")
        print(f"Total time required: {time_in_hour} hour(s), {time_in_miutes} min(s)")
        print(line_1)
    elif choice == 2:
     myfile = open("performers.txt", "r")
     num = 1
     for line in myfile:
         if len(line.strip()) != 0:

             data = line.split(' ')
             sur_name = data[0]
             name = data[1]
             performance_type = data[2]
             time = int(data[3])
             if time > 15:
                 sur_name = sur_name + "*"
             print(f"{num}: {name} {sur_name} ({performance_type}) {time} minutes ")
             num = num + 1
     myfile.close()
    elif choice == 3:
        break
    else:
        print("Please select a option between 1 and 3")
