#this project is implementation of fat tree topology

#import k from user's input
k = int(input("K?"))

#open the output file
f = open("output.txt","w")
#Calculating the pods, servers, core switches, aggregation switches

pods_Count = int(k)
Servers_Count = int(pods_Count * ((k / 2) ** 2))
AggrSwitch_Count = int((k ** 2) / 2)
EdgeSwitch_Count = AggrSwitch_Count
CoreSwitch_Count = int((k / 2) ** 2)
AllSwitch_Count = CoreSwitch_Count + EdgeSwitch_Count + AggrSwitch_Count
Elements_Count = AllSwitch_Count + Servers_Count

# print(pods_Count, Servers_Count, EdgeSwitch_Count, AggrSwitch_Count, CoreSwitch_Count, AllSwitch_Count, Elements_Count)

#Each Element has connection to itself, First we add those connections to output
for i in range(Elements_Count):
    out = str(i)+ "\t" + str(i) + "\t" +"1" + "\n"
    f.write(out)