import pygame
class A_star:
    """A star class takes as arguments a start and a goal node and the graph that
    contains the nodes.
    It returns a list with the path from the end node to the start node.
    """
    def __init__(self,start,goal,Glist):
        #open and closed set are empty at the start
        self.closed_set=[]
        self.open_set=[]
        self.start=start
        self.goal=goal

        self.GLIST=Glist
        self.path=[]
        self.path1={}

        self.g_score={}
        self.f_score={}
        self.h_score={}
        #at first in the open set is only the start node
        self.open_set.append(self.start)
        #calculating the costs for the start node
        self.g_score[self.start]=0
        self.h_score[self.start]=self.cost(self.start,self.goal)
        self.f_score[self.start]=self.g_score[self.start]+self.h_score[self.start]

        
    def solve(self):
        while self.open_set:
            # the node with the minimum cost is the current node
            self.curent=self.min_f(self.open_set)
            self.path.append(self.curent)
            
            if self.curent==self.goal:
                # if the current is the goal return the path
                route = []
                pos = self.goal
                while pos != self.start:
                    route.append(pos)
                    pos = self.path1[pos]

                route.append( self.start )
                return (route)
            #remove the curent from the open set
            self.open_set.remove(self.curent)
            #add the node in the close set
            self.closed_set.append(self.curent)
            #get the neighbours for the current node
            self.neighbours=self.get_neighbours(self.curent,self.GLIST)

            #get every node from neighbours list
            for n in self.neighbours:
                #if it is in the closet set skip it
                if n in self.closed_set:
                    continue
                newM=self.g_score[self.curent]+self.cost(self.curent,n)
                #if the node has a lower cost then the neighbours or is not in the open set
                if newM<self.g_score[n] or n not in self.open_set:
                    #set the new cost
                    self.g_score[n]=newM
                    self.h_score[n]=self.cost(n,self.goal)
                    self.f_score[n]=self.g_score[n]+self.h_score[n]
                    #set the path to retrace it
                    self.path1[n] = self.curent
                    
                    if n not in self.open_set:
                        #add the node in the open set
                        self.open_set.append(n)

        
    def cost(self,start,goal):
        """Calculates the heuristic cost given 2 coordonates"""
        dx=abs(start[0]-goal[0])
        dy=abs(goal[1]-start[1])
        D=abs(dx-dy)

        E=min(dx,dy)

        return (((E*14)+(D*10)))

                
    def min_f(self,open_list):
        """Gets the minimum from a list"""
        for i in range(len(open_list)-2):
            for j in range(len(open_list)-1):
                if self.f_score[open_list[i]]<self.f_score[open_list[j]]:
                    aux=open_list[i]
                    open_list[i]=open_list[j]
                    open_list[j]=aux

        self.curent=open_list[0]
        return (self.curent)
    def get_neighbours(self,current,Glist):
        """Gets the neighbours of a node"""
        nei=[]

        x, y = current

        for i in range(-30,50,30):
            for j in range(-30,50,30):
                newX = x + i
                newY = y + j

                if newX==x and newY==y:
                    continue
                else:
                    if (newX,newY) in Glist and Glist[ (newX,newY)] == True:

                        self.g_score[(newX,newY)]=self.cost(self.start,(newX,newY))
                        self.h_score[(newX,newY)]=self.cost((newX,newY),self.goal)
                        self.f_score[(newX,newY)]=self.g_score[(newX,newY)]+self.h_score[(newX,newY)]
                        nei.append( (newX,newY) )
        return nei                
