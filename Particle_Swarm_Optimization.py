#This is simple example program for solve problem by Particle Swarm Optimization(PSO) 
#Author: Mr.Chanon Sattrupinat
#Date  : 2021/9/12
import random as rd
import numpy as np

#SET GLOBAL VARIABLES
n=300;
iteration=150;
w=0.3;
n1=0.3;
n2=0.3;
Upper_x1=5;
Upper_x2=5;
Lower_x1=-5;
Lower_x2=-5;
delta_x1=Upper_x1-Lower_x1;
delta_x2=Upper_x2-Lower_x2;

#SET CONSTANT
positions=np.array([[]]);
velocity=np.array([[]]);
P_best=np.array([[]]); 
G_best=np.array([[]]); 
New_positions=np.array([[]]);
index_G_best=0;

# SET OBJECTIVE FUNCTION
def Objective_function(x1,x2):
  obj_point=((((x1)**2)+x2-11)**2)+((x1+(x2**2)-7)**2) #Himmelblau's function
  return obj_point


# GENERATION INITIAL SOLUTIONS 
def Gen_init_solution(delta_v1=1 ,delta_v2=1):
  global n,positions,velocity,P_best,delta_x1,delta_x2,Lower_x1,Lower_x2
  positions=np.array([[((rd.uniform(0,1))*delta_x1)+Lower_x1,((rd.uniform(0,1))*delta_x2)+Lower_x2]])
  velocity=np.array([[((rd.uniform(0,1))*delta_v1),((rd.uniform(0,1))*delta_v2)]])
  for i in range(n-1):
    p_append=np.array([[((rd.uniform(0,1))*delta_x1)+Lower_x1,((rd.uniform(0,1))*delta_x2)+Lower_x2]])
    positions=np.concatenate((positions,p_append),axis=0)
    v_append=np.array([[((rd.uniform(0,1))*delta_v1),((rd.uniform(0,1))*delta_v2)]])
    velocity=np.concatenate((velocity,v_append),axis=0)
  P_best=positions


# FIND P_BEST
def Find_P_best():
  global n,positions,velocity,P_best
  P_best_point=[]
  point_new=[]
  for i in range(n):
    P_best_point_add=Objective_function(P_best[i][0],P_best[i][1])
    P_best_point.append(P_best_point_add)
    point_new_add=Objective_function(positions[i][0],positions[i][1])
    point_new.append(point_new_add)
  for j in range(n):
    if (P_best_point[j] > point_new[j]):
      P_best[j][0]=positions[j][0]
      P_best[j][1]=positions[j][1]


# FIND G_BEST
def Find_G_best():
  global n,positions,velocity,G_best,index_G_best
  point=[]
  for i in range(n):
    point_add=Objective_function(positions[i][0],positions[i][1])
    point.append(point_add)
  index_G_best=0
  for j in range(n):
    if point[j] == min(point):
      index_G_best=j
  G_best=np.array([[positions[index_G_best][0],positions[index_G_best][1]]])

# CALCULATE VELOCITY PARTICLES
def Velocity_particles():
  global w,positions,velocity,n1,n2,P_best,G_best
  r1=rd.uniform(0,1)
  r2=rd.uniform(0,1)
  velocity=(w*velocity)+(n1*r1*(P_best-positions))+(n2*r2*(G_best-positions))

#CALCULATE NEW POSITION OF SOLUTIONS
def Update_position():
  global positions,velocity
  positions=np.sum([positions,velocity], axis=0)
  
if __name__=='__main__':
    Gen_init_solution(50,50)
    for i in range(iteration):
        Find_P_best()
        Find_G_best()
        Velocity_particles()
        Update_position()
        print(G_best)
