import numpy as np
import time as time
import matplotlib.pyplot as plt
import matplotlib as mpl

def Function(x,y):
    z = (x-10)**2 + (y-20)**2
    return(z)


def PSO(iterations,swarm_size,particle_best_XY,global_best_XY,\
        particle_XY,particle_velocity,global_best_value):
    best_value = []                  
    locBest = []                     
    iteration_value_best = []        
    locList_best = []               
    iteration_value = []            
    locList = []                     
    for i in range(iterations): 
        for j in range(swarm_size):
            for k in range(2): n 
                u = np.random.rand(2) 
                error_particle_best = particle_best_XY[j,k] - particle_XY[j,k]
                error_global_best = global_best_XY[k] - particle_XY[j,k]
                v_new = inertia*particle_velocity[j,k] + \
                    local_weight*u[0]*error_particle_best + \
                    global_weight*u[1]*error_global_best
                if v_new < -max_velocity:
                    v_new = -max_velocity
                elif v_new > max_velocity:
                    v_new = max_velocity
                particle_XY[j,k] = particle_XY[j,k] + v_new*step_size
                particle_velocity[j,k] = v_new
            v = Function(particle_XY[j,0],particle_XY[j,1])
            if v < particle_best_value[j]: 
                particle_best_value[j]=v
                particle_best_XY[j,:] = particle_XY[j,:].copy()
            if v < global_best_value:
                global_best_value=v
                global_best_XY = particle_XY[j,:].copy()
        print('x='+'%.2f' % global_best_XY[0]+', y='+'%.2f' % global_best_XY[1])
        best_value.append(global_best_value.copy())
        locBest.append(global_best_XY.copy())
        iteration_value.append(v)
        locList.append(particle_XY.copy())
        v = Function(particle_XY[:,0].copy(),particle_XY[:,1].copy())
        iteration_value_best.append(np.min(v))
        locList_best.append(particle_XY[np.argmin(v),:])
    return locList,locBest

def plot_PSO_result(locList,locBest):
    plt.figure(figsize=(5,5))
    plt.grid('on')
    plt.rc('axes', axisbelow=True)
    plt.scatter(10,20,100,marker='*',facecolors='k', edgecolors='k')
    for i in range(len(locList)):
        plt.scatter(locList[i][:,0],locList[i][:,1],10,marker='x')
        plt.scatter(locBest[i][0],locBest[i][1],50,marker='o',\
                    facecolors='none',edgecolors='k',linewidths=0.4)
        plt.text(locBest[i][0]+0.1,locBest[i][1]+0.1,str(i),fontsize=8)
    plt.xlim(-1,15)
    plt.ylim(-1,23)
    plt.xlabel('$x$')
    plt.ylabel('$y$')
    plt.title('Particle Swarm Optimization')
    plt.savefig('results',dpi=300)
    plt.show()

if __name__ == "__main__":
    swarm_size = 5
    iterations = 26 
    inertia = 0.5 
    local_weight = 2 
    global_weight =  2 
    max_velocity = 1 
    step_size = 1 
    particle_XY = np.random.rand(swarm_size,2)-0.5 
    particle_velocity = np.random.rand(swarm_size,2)
    particle_best_value = Function(particle_XY[:,0],particle_XY[:,1])
    particle_best_XY = np.copy(particle_XY)
    global_best_value = np.min(particle_best_value)
    global_best_XY = particle_XY[np.argmin(particle_best_value)].copy()
    locList,locBest = PSO(iterations,swarm_size,particle_best_XY,\
                          global_best_XY,particle_XY,particle_velocity,global_best_value)
    plot_PSO_result(locList,locBest)

