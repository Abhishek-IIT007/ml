import math
from random import randint





###now  steps in k means cluster
###cluster assignment
### move centroid step

                                
def Distance(x,y):                  #finding the distance b/w points
    EUD=0
    #print(x, y)
    for i in range (len(x)):
	    EUD+=math.pow(float(x[i])-float(y[i]),2)

    return math.sqrt(EUD)

def Class_kmeans(means,points):         #assigning or classifying data according to clusters
	pos=-1
	minm=-1
	for i in range(len(means)):
		dist=Distance(points,means[i])
		if (dist<minm):
			minm=dist
			pos=i           # refing to the index
	return pos

###in this update means fuction i have used the formula mean of n numbers =  (mean of n-1 numbers * n-1)+ new number added / totral number(N) 
                                
def Update_means(n,mean,point):      ###function to update means by the new average
    for i in range(len(mean)):
        m = mean[i]
        m = (m*(n-1)+point[i])/(n)
        
     
    return mean


# function which calculates/finds means and calculates clusters
def Calc_means(k,points,maxIteration=1000):                ### 1000 iteration max.. suggested by andrew ng
    # Initializing means to points from dataset
    
    f=len(points[0])
    
    means = [[0 for i in range(f)] for j in range(k)]
    #print("means= ", means)
    for i in range(len(means)):  ###initializing means as suggested by andrew ng. Local optima problem can still occur
        op=randint(1,len(points))
        means[i]=points[op]

    # we will need lists which store the cluster size of each mean; and the cluster to which a data point belongs
    
    data_centroid=[0 for i in range(len(points))]
    Clst_size=[0 for i in range(k)]
    
    for itr in range(maxIteration):
        for i in range(len(points)):
            constant= True          ###checking if the clusters are changing or not                    
            point=points[i]         # accesing each point
            pos=Class_kmeans(means,point)
            Clst_size[pos]+=1
            size=Clst_size[pos]
            means[pos]=Update_means(size,means[pos],point)
            if(pos!=data_centroid[i]):
                constant=False
            data_centroid[i]=pos
        if(constant):
            break

    clusters=[[] for i in range(k)]      ### clusters is the list which stores all the current points belonging to a particular cluster
    for dat in points:
            pos=Class_kmeans(means,dat)
            clusters[pos].append(dat)           # points being fed to the clusters 
    return means,clusters

# function that reads data from txt file

def preprocess(fileName):
    #Read the file, splitting by lines
    file = open(fileName,'r')
    lines = file.read().split('\n')
    
    file.close()

    points = []

    for i in range(len(lines)):
        line = lines[i].split(' ')    #splitting by space
        
        each_points = []

        for j in range(len(line)):          #to convert string into float
            value = float(line[j])
            
            each_points.append(value) #Add feature value to dict
    	   
        points.append(each_points)


        
    return points


def writing(k,means):
    file1=open('clusters.txt','w')
    for i in range(k):
        for j in range(len(means[0])) :
            file1.write(str(means[i][j]))
	    file1.write(" ")
	file1.write("\n")

	
def main():                                
    filename=input("Please enter the name of file with extension  ")
    k=int(input("Please enter the number of clusters you want  "))
    points=preprocess(filename)
    
    means,clusters=Calc_means(k,points)
    #print("the result is  ",means)
    #print(" The means may not be exact due to the problem of local optima:")                       
    writing(k,means)
    
if __name__ == "__main__": ###for running script in bash
    main()

