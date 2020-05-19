Indices:

1 Introduction……………………………………2

1.1 Overview……………………………………………………….2

1.2 Glossary………………………………………………………..2

2 General Description…………………………..

2.1 System Functions……………………………………………..2

2.2 User Characteristics and Objectives………………………..3

2.3 Operational Scenarios………………………………………..4

2.4 Constraints…………………………………………………….5

3 Functional Requirements…………………….6

3.1 Ant Class………………………………………………………..6

*3.2* Drawing the visualisation with PyGame……………………..6

3.3 Food……………………………………………………………..7

3.4 Pheromone trails……………………………………………….8

4 System Architecture…………………………..9

5 High Level Design…………………………….10

5.1 Class Diagram…………………………………………………10

5.2 Logical Data System………………………………………….11

6 Preliminary Schedule………………………...12

7 Appendices…………………………………....15

1\. Introduction:

1.1 -Overview: The project consists of a virtual representation of an
ant colony. We will be using Genetic algorithms in order to model the
colony. Each iteration of the ant colony will improve upon the last,
becoming more efficient and developing more and more complex but ordered
structures.

The behaviour of the ants is inspired by real ants, they lay pheromone
trails stating their intended actions and other ants choose their
actions respective to the probability based on the number of pheromone
trails already laid to other actions.

In order to improve with each iteration the simulation will generate a
score, or a fitness, which provides a scale to improve on.

The fitness function will generate a score based on the amount of food
gathered and ants created, this function will be used to define which
ants the algorithm will pick with each generation in order to improve
efficiency and continuously maximise the score. With each change of
environment the ant colony will need to be “trained” again in order to
find the most efficient directives to follow.

1.2 -Glossary:

**Python:** Python is an interpreted high-level programming language for
general-purpose programming.

**PyGame:** PyGame (the library) is a free and Open Source Python
programming language library for making multimedia applications like
games built on top of the rich SDL library.

2\. General Description:

**2.1 -System Functions:**

The primary function of the system is to model a random world with
obstacles and resources that our colony can learn to survive and thrive
in. Initially we expect colonies to be inefficient, be unable to grow or
get trapped in loops similar to the real life scenario “circle of death”
that ants sometimes encounter.

The end goal is to have a system that will be able to produce colonies
that can efficiently grow and adapt to changes for example a decrease in
resources or an increase in threats.

Another end goal is to be able to have the user interact with the
environment and define the start conditions of the colony ie. The
prevalence of resources, starting population, prevalence of threats.

*User Functionality System:*

Firstly the user will have to download the ant colony program from
github or have a copy from one of the developers. The program may be run
without the use of the internet and on any system supporting Python and
PyGame. Upon running the program the user will simply have to wait or
watch as the virtual ants begin to find food as well as create pheromone
trails and traverse them. The longer the user leaves the simulation
running the more complex the structures created by the ants will be and
over more time those structures will become more structured as the ants
better themselves and find more efficient paths.

The ants will go through generations with the aid of genetic algorithms
with each generation in order to technically become better at collecting
food and pathfinding with each iteration.

*GUI for displaying the simulation:*

Currently we plan on using PyGame to visualise the simulation using
different colored dots to represent different elements of the simulation
such as the ants themselves, the colony location, food and obstacles.
There is no need to over-complicate the visualisation and therefore a
top-down 2D-view will be sufficient in order to somewhat accurately
represent the colony in a simple clutter free format.

**2.2 -User Characteristics and Objectives:**

We predict that the users of this application will be limited to our
project supervisor, co-ordinator and both developers. Because of this it
is assumed that all users possess the required level of technical
expertise to use the program effectively.

*Our main objectives with regard to requirements for the system from the
user’s perspective are:*

-To display the ants in a minimalistic clutter free format.

-To have the ability to modify the environment.

-To have the ability to modify the colony and its characteristics.

**2.3 Operational Scenarios: **

**-2.3.1: User begins simulation.**

The user will open the program and begin the simulation. In the
beginning the ants will behave near randomly searching for the optimal
path towards maintaining and expanding their colony choosing between
finding food, raising new ants or defending the colony. After leaving
the simulation running for some amount of time the ants should begin to
create more intricate but structured paths towards the success of the
colony.

**-2.3.2: User adds resources.**

The user will have a simulation open and running. The user simply left
clicks to add food to the field. The coordinates of the button will be
evaluated and a food resource will be added to the x and y coordinate

**-2.3.3: User modifies the starting scenario.**

The user will be able to open the code and view the various variables
that control the environment and the characteristics of the ants. A menu
will preferably be available to modify these variables but those users
who possess the required expertise will be able to modify the code
directly to change the number of starting ants, the colors of all the
elements within the program, the amount of food initially available, the
number of obstacles present and the size of the window presenting the
ants. After modification the user will simply begin the program and it
will run with the user’s new modifications.

**-2.3.4: User exits the program.**

After running the simulation for any duration of time the user will want
to exit the program. He/she will be able do so at any point by simply
exiting the program. The program will also finish calculations once all
of the food in the environment has been depleted. Should this be the
case the program will output various statistics about the simulation
such as the number of iterations of ants the simulation generated and
the amount of time the simulation ran for.

**2.4 Constraints: **

There are not many strict constraints on this program as there is no
private information stored on the program. Should we have required
anything other than Metadata (age, sex, etc.) we would need to include a
GDPR agreement and receive ethical approval but thankfully none of those
apply here.

*Time Constraints:*

The completion due date for this project is 5pm Friday 8/3/2019.

*User requirement:*

We understand the needs of the user requirements and will be able to
meet them in the given time frame.

*Financial constraints:*

There are thankfully no financial constraints which apply to this
project.

*Design constraints:*

We would like to structure our program using OO in order to model ants
as accurately as possible and have the program run smoothly on any
platform supporting pyGame and Python but as we will be building our
program initially in Python and we have a wide range of changing
elements we will not expect incredibly quick runtimes. A
re-implementation in C or even JavaScript would more than likely greatly
increase our efficiency.

As already mentioned we plan on initially designing and implementing our
ant colony program in Python using pyGame for visualisation. We decided
on Python because we have both been involved in projects where the
implementation was Python focused and we are both most comfortable using
it.

3\. Functional Requirements

3.1 **Ant Class**

*Description*

The Ant Class will be the class which all ants are modelled from. Every
iteration of ant will be modelled from this class and it is essential to
control the movements of ants as well as control the release of
pheromone trails. Without this the program would not be of the Object
Oriented paradigm.

*Criticality*

The Ant Class is essential to the system in order to run correctly and
be of the intended paradigm. This class will define a whole range of
abilities the ants will have. More than likely there will be a general
ant class and several ant subclasses detailing the different abilities
of different types of ants.

*Technical issues*

The main issue here is to ensure that all methods within the ant class
interact with each other correctly. The use of global variables will
more than likely become essential in order to ensure that the methods
interact with functions outside of the class also.

*Dependencies with other requirements.*

It is essential that the ant class interact with all other aspects of
the program. It may also be essential to incorporate these functions
with PyGame to ensure accurate visual representation.

*3.2* **Drawing the visualisation with PyGame**

*Description*

PyGame will be used to visually represent the simulation. This will
require all platforms which are running this program to have PyGame
installed.

*Criticality*

PyGame is essential to visualise the simulation. We considered Tkinter
which is a built in library pre installed with all copies of Python but
this proved to contain too few functions and PyGame simply has more
functionality and in our opinion looks a lot better.

*Technical Issues*

While there exists many powerful rendering engines providing tools to
incorporate Python code such as Unity, they add a level of complexity we
feel is simply unnecessary for this project. With simple development and
minimised run times as well as a simple representation in mind, PyGame
seems to be the optimal choice.

*Dependencies with other requirements.*

In order to achieve the above goal we must ensure to present all
elements of the program in a clutter free simple format while at the
same time ensuring that all information is displayed correctly. There
must be a key to ensure proper identification of the elements present on
the screen.

3.3 **Food**

*Description*

The ants will look for food on the field. This food is essential to the
colony and used to produce more ants which will in turn look for more
food to increase the size of the colony. This food will be a set amount
and will be placed randomly on the field for the ants to find. This set
amount is changeable by the user by either editing the initial starting
amount or by placing more.

*Criticality*

It is essential that this food is easy to spot on our visual
representation and is placeable on the field at any point of the program
running by the user. The user should not be allowed to place double
amounts of food in a single area. The amount of food will not change but
is subject to change based on the preferences of the user.

*Technical Issues*

The above should be achieved with a few lines of code or maybe even a
seperate class modelling the food as an object. Either way it will be
visually represented by a different color than those of the
representations of other elements.

*Dependencies with other requirements.*

We must ensure that we have a method of displaying the fact that a food
source is being depleted. This will be done visually, more than likely a
color change or a notification.

3.4 **Pheromone trails**

*Description*

This will be the trail left by ants who have successfully found food or
are partaking in other tasks. This trail will be used by other ants and
affect the probability at which they will choose tasks.

*Criticality*

It is important that the trail is only left by successful ants, or at
least the most potent trails are left by successful ants. It is possible
that we will structure our program so that only a select type of ant
will release pheromone trails and regular ants following the trail may
only enforce it’s potency. This way there will be less cases of ants
choosing random trails that lead nowhere that are left by unsuccessful
ants.

*Technical Issues*

It is of the utmost importance that a system is figured that allows the
pheromone trails to “evaporate” as they do in real life. This is both
being more realistic with our simulation and also solving the problem of
ants following “dead” trails. We predict that altering the transparency
of a color will suffice to model the pheromone trail with this in mind.

It is also possible that the ants will get stuck in a “circle of death”
as they do in real life with multiple ants following other ants trails
who are simply following the ones left by those following them. It is
genuinely a problem which occurs in the wild and we can imagine this
happening in our simulation. A system for eliminating the ants who have
traversed a certain distance with no success will have to be implemented
to solve this as well as the problem of ants traversing randomly without
success.

*Dependencies with other requirements.*

It is imperative that the pheromone trail system operates correctly and
in union with the ant class as it is the ants themselves which release
varying amounts of pheromones as they move.

4\. System Architecture

System Architecture Diagram:

![](media/image2.jpg "System Architecture Diagram"){width="4.489583333333333in"
height="2.6145833333333335in"}

The user will interact with the program when modifying variables such as
food, obstacles and initial amount of ants. PyGame will interact with
the back-end of the simulation to correctly represent what the
simulation is achieving and the user will also directly interact with
the visualisation in order to place food or obstacles. There are no
third-party functions or complexities which will affect the program, it
should be able to run standalone, that is without the need for any
supporting material.

5\. High level Design

Here we provide a system model using SSADM tools to illustrate the
system and it’s intended functions.

*Class diagram*

This diagram is used to display the different classes, what they will
contain and how they will interact with each other.

*Logical Data System*

In this diagram we show an overview of how the user will interact with
the system through cardinalities. Ants simulation variables also covers
modifiers for the genetic algorithm.

***Class Diagram***
![](https://gitlab.computing.dcu.ie/cahila23/2019-ca326-acahill-virtualantcolony/tree/master/functional_spec/images/ClassDiagram.jpg "Class Diagram"){width="6.270833333333333in"
height="4.430555555555555in"}

***Logical Data System***

![](https://gitlab.computing.dcu.ie/cahila23/2019-ca326-acahill-virtualantcolony/tree/master/functional_spec/images/LDS.jpg "Logical Data System"){width="4.020833333333333in"
height="3.8645833333333335in"}

5.2 *Generalisation of high level design.*

We aim to design the program in an Object Oriented style, that is that
we plan on modelling all elements of the program as objects with their
own methods and parameters. We will be using Genetic algorithms in order
to allow the ants to improve upon themselves and we then plan on
implementing the visualisation with PyGame.

6\. Preliminary Schedule

This section will provide a preliminary view of our planned project
timeline through the use of a simple Gantt Chart.

![](https://gitlab.computing.dcu.ie/cahila23/2019-ca326-acahill-virtualantcolony/tree/master/functional_spec/images/Prelim1.png "Preliminary Schdule 1"){width="7.494791119860017in"
height="5.239583333333333in"}

![](https://gitlab.computing.dcu.ie/cahila23/2019-ca326-acahill-virtualantcolony/tree/master/functional_spec/images/Prelim2.png "Preliminary Schdule 2"){width="9.114583333333334in"
height="5.442707786526684in"}

![](https://gitlab.computing.dcu.ie/cahila23/2019-ca326-acahill-virtualantcolony/tree/master/functional_spec/images/Prelim3.png "Preliminary Schdule 3"){width="9.875620078740157in"
height="5.557291119860017in"}

7\. Appendices

Python Documentation Available:
[*https://www.python.org/*](https://www.python.org/)

PyGame Documentation Available:
[*https://www.pygame.org/*](https://www.pygame.org/)

Alastair Sutherland:
[*https://www.computing.dcu.ie/\~alistair/projects.html*](https://www.computing.dcu.ie/~alistair/projects.html)
