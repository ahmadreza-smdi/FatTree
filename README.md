# Fat Tree topology Imlementation
Implementing and visualizing Fat Three topology powered by python 
### what is Fat Tree topology ?
We have different topologies for arranging servers and switches in dataCenter, topologies 
like FatTree,BCube,Dcell,... . in this repository I implemented FatTree using python and
networkx to visualize the graph.

### How it work?
if we start bottom up approach servers are connected to edge switches and edge switches 
are connected to aggregation switches. then we got core switches that are connected to
aggregation switches.
I did use major commenting for you to get to know this toplogy, but here is some information 
about this topology using k=4:
```
Number of pods = k
```
```
Number of servers in each pod = pods_Count * ((k / 2) ** 2)
```
```
Number of servers in each pod = (k / 2) ** 2
```
```
Number of Aggregation Switches = (k ** 2) / 2
```
```
Number of Edge Switches = (k ** 2) / 2
```
```
Number of Core Switches = (k / 2) ** 2
```
## Prerequisites

What things you need to install the software and how to install them

the project is based on python, first step is installing python

#### Ubuntu
```
sudo apt-get update
sudo apt-get install python3.6
```
#### CentOS
```
sudo yum update
sudo yum install yum-utils
```
#### Fedora
```
sudo dnf install python36
```
#### Arch linux
```
packman -S python
```

## Running the project
All the files of the project is combined and all the modules are set to one file, so to run the 
project you just need to run.py file
```
python3 main.py
```

## Built With

* [Python](https://www.python.org/) - Programming language

## Authors

* **Ahmadreza Samadi** - *Programmer* - [Ahmadreza samadi](https://github.com/ahmadreza-smdi)

*Thanks for your attention.*
