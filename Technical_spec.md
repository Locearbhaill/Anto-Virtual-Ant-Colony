Technical Specification
Project Anto
Alexander Cahill __________________________________ 15321711
-alexander.cahill23@mail.dcu.ie
Liam Ó Cearbhaill __________________________________ 15384941
-liam.ocearbhaill2@mail.dcu.ie
0. Table of contents
Introduction.....................................................................................................
System Architecture..........................................................................................
High Level Design............................................................................................
Problems and Resolutions..................................................................................
Installation Guide..............................................................................................

1. Introduction
1.1 Overview
We have implemented a digital simulation of an ant colony using Python and pyGame. Our
colony simulation includes ants who use an Ant Colony Optimisation(ACO) algorithm with
pheromones in order to accurately model the behaviour of ants within a real-life colony.
These ants will search for the shortest paths towards gathering food and upon gathering a
certain amount of food they will also increase the size of the colony by spawning new ants.
We have also included enemy ants with the goal of destroying the colony and soldier ants
tasked with the aim of defending the colony from enemies.

Although our original goal was to implement a Genetic Algorithm to allow the ants to improve
upon themselves, time constraints and experience meant that a simpler ACO algorithm
approach would suffice in order to achieve our goal of simulating an ant colony. As ACO is
inspired by real life ants, the basic concept is that the ants will wander effectively at random
until they come across a food source at which point they will return to their colony while
laying a pheromone trail. The shortest paths will have the most pheromones over time and
thus be the most likely to be traversed by other ants. The probability of choosing the next
move within the ants is decided by a “transition rule”

<img src = "images/math1.png"/>

(page 5,
https://www.researchgate.net/publication/245310587_A_new_transition_rule_for_ant_colony_optimization_algorithms_application_to_pipe_network_optimization_problems​)

Where 𝜏𝑖𝑗 represents the pheromone trail 𝜂𝑖𝑗  represents the “inverse distance” , while
𝛼 represents the weight for the “importance” of pheromone trails and 𝛽  represents the
weight for the “importance” of inverse distance.
2. System Architecture
This program requires no external programs or prerequisites save the two we libraries we
have imported to cut down on development time.
We have used PyGame in order to allow us to render our colony simulation in a 2D “field”,
this is a pip installable library providing gui and other useful functions.
We have also made use of random within this program. Random comes as standard within
Python and PyGame is easily installed with the use of pip.
Our original system architecture diagram can be seen as follows:

<img src = "images/lds1.png"/>

This was highly simple and a revised high level version can now been seen as follows:

<img src = "images/ldsnew.jpg"/>

The relationships of functions within these modules can be seen in the diagram with blue
arrow-headed lines.
The visualisation of the colony can be expressed as the environment in which the ants
operate within and thus the UI file encompasses both the drawing aspects of the simulation
as well as much of the variables which can be changed in order to allow the colony to
produce many different behaviours.
The user may also directly interact with the visualisation to alter the environment by clicking
anywhere to place food or clicking buttons to pause(red)/slow(yellow)/resume(green) the
simulation.

<img src = "images/pasted_image_0.png"/>

(A screenshot of our UI including the three interactive colored buttons.)

3. High-Level Design
Our original Class diagram is as follows:

<img src = "images/classold.png"/>

A revised version can be seen as follows:

<img src = "images/classnew.jpg"/>

The largest difference that can be seen between the two is that we have scrapped the
Genetic Algorithm approach. We have still implemented a version of an Ant Colony
Optimisation to allow realistic ants movement which still fulfills the majority of our
requirements. With more time we may have been able to implement a Genetic Algorithm.

As the UI is not a class we have not included it within the class diagram except to show it’s
interactions with the other classes within the program.

Our Logical Data Structure diagram can be seen as follows:

<img src = "images/ldsss.jpg"/>

Our Data Flow Diagram is as follows:

<img src = "images/last.jpg"/>

4. Problems and Resolution
Our first major hurdle to overcome was the learning curve associated with genetic
algorithms. Neither of us had a good grasp on how to implement genetic algorithms. After
getting most of the framework of the program in place we realised that we may be unable to
create a genetic algorithm and apply it to the simulation. With the Ant Colony Optimisation
Algorithm and pheromones working correctly we felt that this was an acceptable tradeoff as
we achieved part of our initial goal without having to forfeit the system’s overall functionality
if we were to start designing and implementing a Genetic Algorithm.

Our second major hurdle lay within the transition rule used for calculating the probability of
movement within the ants. All ants were moving exactly the same way at exactly the same
time despite multiple attempts. The problem turned out to be a simple oversight when
implementing the transition rule. The bottom half of the equation which divides the top half
was being calculated within the same loop as the top half causing the divisor, and thus the
equation, to change with every iteration and it was introducing odd movement into the ants.
It took us longer than we would have liked to spot this but separating the two calculations
into their own loops solved this problem.

Initially when we started writing the program the code for the user interface and Ant class
were contained in the same file. Later in the development we decided each class and it’s
related code should be contained within its own file as the previous method inhibited
workflow and caused unexpected errors to occur. We found it somewhat difficult to isolate

the Ant class as it and the ui file were so intertwined. Through lots of debugging we were
able to move the Ant class and most of the related code to it’s own file.

We also had a problem where when you exited the program via clicking the X in the top right
corner, a second instance of the simulation would open as opposed to closing the initial
instance of the simulation. How we overcame this was by altering the control flow and if
statement logic within the main. An extra quit() was also added and a culmination of all these
changes solved this problem.

5. Installation Guide
Prerequisites: User must have PyGame installed. If you do not have PyGame installed it is
easily installed through the Python terminal by using “pip install pygame”. This will install
PyGame on your interpreter and you will have met the prerequisite.

The (simulation) software can be easily installed through downloading the “code” folder from
the project GitLab repository.

The user can choose to download the files in .zip or .tar format which then need to be
unpacked. These files can then be unpacked to a desired location using a variety of open
source or proprietary software.

The execution of the software is done through the command line.

The program is written in Python and requires Python version 3.7.0 to run correctly as well
as the use of the PyGame library.

The simulation is started when the user executes the “ui.py” file and ends when the user
clicks the X in the corner of the ui window or terminates the simulation via terminal.

Please refer to the user manual for information on the operation of the Ant Colony Simulation