# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 16:08:01 2019

@author: zhum
"""

import matplotlib
#To build up GUIs, the default package to use is TKInter.
import tkinter
#change the backend  to render as associated with TKInter
matplotlib.use('TkAgg')
      
import random
import operator
import matplotlib.pyplot
import agentframework
import csv
import matplotlib.animation

#First we need to get the webpage by issuing a HTTP request.
import requests
import bs4

r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
print(td_ys)
print(td_xs)


# Lines here happen before any data is processed
#for row in dataset
    # Lines here happen before each row is processed
    #for values in row
        # do something with values.
    # Lines here happen before after row is processed
# Lines here happen after all the data is processed

environment = []
f= open('in.txt', newline = '')
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in reader:
    rowlist = []                       #A list of rows
    for value in row:                    #A list of value
        #print(value)
        #parsed_line = str.split(row, ",")
        rowlist.append(value)
    environment.append(rowlist)                 #Floats
f.close()  #Don't close until you are done with the reader:
           # the data is read on request.

'''for row in range(0,len(environment)):
    for col in range (0, len(environment[row])):
        print(environment[row][col])'''

#matplotlib.pyplot.imshow(environment)
#matplotlib.pyplot.show


def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a.x - agents_row_b.x)**2) +
    ((agents_row_a.y - agents_row_b.y)**2))**0.5


num_of_agents = 10
num_of_iterations = 100
neighbourhood = 20
agents = []


fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

#ax.set_autoscale_on(False)

# Make the agents.
for i in range(num_of_agents):
   #for i in range(num_of_agents):
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    agents.append(agentframework.Agent(environment, agents, y, x))
    #agents.append(agentframework.Agent(environment, agents))

carry_on = True	

def update(frame_number):
    
    fig.clear()   
    global carry_on
    # Move the agents.
    
    random.shuffle(agents)
    for i in range(num_of_agents):
        
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
        
        #set up condition that carry_on = false
        if (agents[i].store >= 200):
            carry_on = False
            print ("stopping condition")
            
    matplotlib.pyplot.xlim(0, 99)
    matplotlib.pyplot.ylim(0, 99)
    matplotlib.pyplot.imshow(environment)
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
        print("coordinate x, coordinate y :",agents[i].x,agents[i].y)

def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < 100) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1

#animation = matplotlib.animation.FuncAnimation(fig, update, interval=1,repeat=False)#frames=1)

#animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
   #canvas.show()
    canvas.draw()
   
   
root = tkinter.Tk()
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

#create a menu bar
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run) 

tkinter.mainloop()


#matplotlib.pyplot.show()


 