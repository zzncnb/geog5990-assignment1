# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 13:27:00 2019

@author: zhumi
"""

import random

#The name of the class starts with capitals and is in CamelCase.
class Agent():
    # "self" represents object. If we store data inside an object, we store it inside self.
    def __init__(self, environment, agents, x, y):   #Form of constructor and variable.
        self.environment = environment
        self.store = 0 # We'll come to this in a second.
        
        
        #Adjust the function to give default of two variabes as None.
        #This will work if they are missing.
        if (x == None):
            self.x = random.randint(0,100)
        else:
            self.x = x
        if (y == None):
            self.y = random.randint(0,100)
        else:
            self.y = y
            
        self.agents = agents

    def set_x(self,value):
        self.x = value


    def get_x(self):
        return self.x
    
    def set_y(self,value):
        self.y = value
    
    def get_y(self):
        return self.y
    
    def __str__(self):
        return "x=" + str(self.x) + ",y=" + str(self.y)
    
    def move(self):  #Make it move
        if random.random () < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100
        
        if random.random () < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100
            
    def eat(self): # Make it eat what is left
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
                    
            
    #Loop through the agents in self.agents .
    # Calculate the distance between self and the current other agent:
    #distance = self.distance_between(agent)
    # If distance is less than or equal to the neighbourhood
    # Sum self.store and agent.store .
    # Divide sum by two to calculate average.
    # self.store = average
    # agent.store = average
            
            
    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
            dist = self.distance_between(agent)
            if dist <= neighbourhood:
                sum = self.store + agent.store
                ave = sum /2
                self.store = ave
                agent.store = ave
                
    # Fuction takes in two arbitary agents and will return the distance between them.
    def distance_between(self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5
   
     
        