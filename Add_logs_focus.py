import os  # important for file management

for x in os.listdir():
    if x.endswith(".txt"):
        fr = open(x, "r")
        file = ""
        lines = fr.readlines()
        for line in lines:
			#Searches for the line that begins with "id" and then splits it into parts to use
            if line.find("id") == 1:
                start_log = line.strip()
                start_log, log_id = line.split(" = ",1)
                log_id = log_id.strip()
			#Combines the lines together to insert logs
            if line.find("completion_reward") == 1:
                completion_reward_id = line
                #pos = find_population(line)
                #number = int(line[pos:])
                #population = int(number * total_growth)
                #line = line[:pos] + str(population) + "\n"
                #line = line.replace(' ', '')
                line = line + "\t\t" + 'log = "[GetDateText]: [Root.GetName]: Focus ' + str(log_id) + '"\n'
                print(line)
            file = file + line
        fr.close()
        fw = open(x, "w")
        fw.write(file)
        fw.close()
