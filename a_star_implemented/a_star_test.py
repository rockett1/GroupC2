
import pygame
class A_star:
    def __init__(self,start,goal,Glist):
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
    
        self.open_set.append(self.start)
        self.g_score[self.start]=0

        self.h_score[self.start]=self.cost(self.start,self.goal)
        self.f_score[self.start]=self.g_score[self.start]+self.h_score[self.start]
        
 
        
    def solve(self):
        while self.open_set:
            self.curent=self.min_f(self.open_set)


            self.path.append(self.curent)

            if self.curent==self.goal:
                print('gotcha')

                route = []
                pos = self.goal
                while pos != self.start:
                    route.append(pos)
                    pos = self.path1[pos]

                route.append( self.start )

                return (route)

  
            self.open_set.remove(self.curent)
            self.closed_set.append(self.curent)
            self.neighbours=self.get_neighbours(self.curent,self.GLIST)


            for n in self.neighbours:

                if n in self.closed_set:
                    continue
                newM=self.g_score[self.curent]+self.cost(self.curent,n)
                if newM<self.g_score[n] or n not in self.open_set:
                    self.g_score[n]=newM
                    self.h_score[n]=self.cost(n,self.goal)
                    self.f_score[n]=self.g_score[n]+self.h_score[n]
                    
                    self.path1[n] = self.curent
                    
                    if n not in self.open_set:
                        self.open_set.append(n)

        
    def cost(self,start,goal):
        
        dx=abs(start[0]-goal[0])
        dy=abs(goal[1]-start[1])
        D=abs(dx-dy)

        E=min(dx,dy)

        return (((E*14)+(D*10)))

                
    def min_f(self,open_list):
        for i in range(len(open_list)-2):
            for j in range(len(open_list)-1):
                if self.f_score[open_list[i]]<self.f_score[open_list[j]]:
                    aux=open_list[i]
                    open_list[i]=open_list[j]
                    open_list[j]=aux

        self.curent=open_list[0]
        return (self.curent)
    def get_neighbours(self,current,Glist):
        nei=[]

        x, y = current

        for i in range(-1,2,1):
            for j in range(-1,2,1):
                newX = x + i
                newY = y + j

                if Glist.get( (newX,newY), True ) == False :
                    self.g_score[(newX,newY)]=self.cost(self.start,(newX,newY))
                    self.h_score[(newX,newY)]=self.cost((newX,newY),self.goal)
                    self.f_score[(newX,newY)]=self.g_score[(newX,newY)]+self.h_score[(newX,newY)]
                    nei.append( (newX,newY) )

        return nei                

pygame.init()
white=(255,255,255)
black=(0,0,0)
screen = pygame.display.set_mode((600,600))
screen.fill(white)

l={}
for i in range(10):
    for j in range(10):
        l[(i,j)]=False

for i in range(1,6):
    l[(5,i)] = True

a = A_star((0,0),(9,9),l)
path = a.solve()

print('>',path)

        
for i in l:
    x=i[0]
    y=i[1]
    if l[i]:
        pygame.draw.rect(screen,black,(x*20,y*20,10,10))
    else:
        pygame.draw.rect(screen,(220,220,220),(x*20,y*20,10,10))

for x, y in path:
    c = (0,255,0)
    if l[(x,y)]:
        c = (255,0,0)
    pygame.draw.rect(screen,c,(x*20,y*20,10,10))
        
pygame.display.update()

