#this project is implementation of fat tree topology
import GraphVisualization
G = GraphVisualization.GraphVisualization()


#import k from user's input
k = int(input("K?"))

#open the output file
f = open("output.txt","w")
#Calculating the pods, servers, core switches, aggregation switches
connected= []
pods_Count = int(k)
Servers_Count = int(pods_Count * ((k / 2) ** 2))
Servers_In_Pod = (k / 2) ** 2
AggrSwitch_Count = int((k ** 2) / 2)
EdgeSwitch_Count = AggrSwitch_Count
CoreSwitch_Count = int((k / 2) ** 2)
AllSwitch_Count = CoreSwitch_Count + EdgeSwitch_Count + AggrSwitch_Count
Elements_Count = AllSwitch_Count + Servers_Count
EdgeSwitch_Count_In_Pods = k//2
AggrSwitch_Count_In_Pods=EdgeSwitch_Count_In_Pods
# print(pods_Count, Servers_Count, EdgeSwitch_Count, AggrSwitch_Count, CoreSwitch_Count, AllSwitch_Count, Elements_Count)

# Each Element has connection to itself, First we add those connections to output
for i in range(Elements_Count-1):
    out = str(i)+ "\t" + str(i) + "\t" +"1" + "\n"
    f.write(out)



# counter is way that we address number of edge switches
# counter starts at number of servers because 0 should be included in server counts
counter = Servers_Count

# server counter is a way to address the server for mapping between edge switches and servers
Server_counter = 0

# program goes stage by stage bottom up, first we create links between edge and servers

for i in range(pods_Count):

    for j in range(EdgeSwitch_Count_In_Pods):

        for l in range (k//2):

            out = str(counter)+"\t"+str(Server_counter)+"\t"+"1"+"\n"
            f.write(out)
            connected.append((counter,Server_counter))
            G.addEdge(counter, Server_counter)

            out = str(Server_counter) + "\t" + str(counter) + "\t" + "1" + "\n"
            f.write(out)
            connected.append((Server_counter,counter ))
            G.addEdge(Server_counter,counter )

            Server_counter+=1

        counter += 1

#Handling connection between Aggregation switches and edge switches

for i in range(pods_Count):

    for j in range(AggrSwitch_Count_In_Pods):

        for l in range (k//2):

            out = str(counter)+"\t"+str(Server_counter)+"\t"+"1"+"\n"
            f.write(out)
            connected.append((counter,Server_counter ))
            G.addEdge(counter,Server_counter )

            out = str(Server_counter) + "\t" + str(counter) + "\t" + "1" + "\n"
            f.write(out)
            connected.append((Server_counter,counter ))
            G.addEdge(Server_counter,counter )
            Server_counter+=1

        Server_counter-=k//2
        counter += 1
    Server_counter+=k//2




#Implementing link between aggregation switches and core switches

# we create core because when link reaches the end of cores we want to reset cores
core = []
for i in range(CoreSwitch_Count):
    core.append(counter)
    counter+=1


p = 0
for i in range(pods_Count):
    for j in range(AggrSwitch_Count_In_Pods):
        for l in range(k // 2):
            counter=counter-k+1
            out = str(Server_counter) + "\t" + str(core[p]) + "\t" + "1" + "\n"
            f.write(out)

            connected.append((Server_counter,core[p] ))
            G.addEdge(Server_counter,core[p] )
            out = str(core[p]) + "\t" + str(Server_counter) + "\t" + "1" + "\n"
            f.write(out)
            connected.append((core[p],Server_counter ))
            G.addEdge(core[p],Server_counter )
            p+=1
            if(p==(k//2)**2):
                p=0
        Server_counter+=1
    p = p+1


# implementing the zero connections
counter = 0

for i in range (Elements_Count):
    for j in range(Elements_Count):
        if (i,j) not in connected:
            f.write(str(i)+"\t"+ str(j)+"\t"+"0"+"\n")
            counter+=1

G.visualize()
