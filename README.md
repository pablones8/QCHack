#Aquí és on posarem la descripció del projecte

Our project is a quantum labyrinth were the movment inside the labyrinth comes defined by the mesure of a quantum system.

To move in the labyrinth you need to create your circuit, applying gates to the two qubits. Depending on the final state you mesaure, in a single shot, the ball is going to move in one direction or another; so if you measure the |00> state the ball is going to move up, |01> down, |10> to the right and |11> to the left. The objective is to find the circuit that gives you a 100% chance to move in the direction you choose. On the other hand, if the circuit you create can collapse to diferent states the ball can go to diferent directions, depending on the probability to get each state. 

You are allowed to use thre different gates: Hadamard (H), NOT (X) and Rx (R) with pi/2. If you insert another gate you need to restart the game.

To make the game more entretaining, and add other quantum concepts, you can go through walls following the rules of the tunneling efect. This means that if the ball is headed in a direction where there's a wall there is a certain possibility that the ball will go through said wall, if the wall is thicker the probability to go through the wall decreases.

In order for the user to see and understand how exactly the circuit is changing the initial state for each step, there is and histogram that shows the probability to get each state in the measure, in other words, it represents the final state. It is always possible to get to the final state that you wish to go with a 100% probability, so nullifying completlly all the other states. 

There are three labyrinth versions with increasing dificulty. The objective of the first labyrinth is simply to ilustrate the behaviour of a quantum gate and become familiarized with the program. The second labyrinth aims to get across the concept of interference in a clear way (to do so the initial state has some hadamard gates implemented). And the third, the most complicated one, is just to have some fun playing!

We tried to make a game that helped the user to understand how interference worked in the context of quantum computing, and also how quantum gates modify the state of the system, that's why you can only use three gates that allow a certain range of play whithout becoming intimidating to people whithout a quantum computing background.

There are three labyrinth versions with increasing difficulty. The objective of the first labyrinth is simply to ilustrate the behaviour of a quantum gate and become familiarized with the program. The second labyrinth aims to get across the concept of interference in a clear way. And the third, the most complicated one, is just to have some fun playing!

In case you get stuck, here are the SOLUTIONS to move the ball in each case:
-Level 1: Initial state=00
  Movement commands
  - |00>: DOWN --> apply no gates
  - |01>: UP --> apply X to q0
  - |10>: RIGHT --> apply X to q1
  - |11>: LEFT --> apply X to q0 and q1
  
-Level 2: Initial state=superposition of all states (00, 01, 10, 11)
  Movement commands
  - |00>: DOWN --> apply H to q0, and H to q1
  - |01>: UP --> apply H and X to q0, and H to q1 
  - |10>: RIGHT --> apply H to q0, and H and X to q1
  - |11>: LEFT --> apply H and X to q0, and H and X to q1
  
-Level 3: Initial state=superposition of states 00 and 01
  Movement commands
  - |00>: DOWN --> apply R and X to q0, and X and X to q1
  - |01>: UP --> apply R and to q0
  - |10>: RIGHT --> apply R and X to q0, and X to q1
  - |11>: LEFT --> apply R to q0, and X to q1
  
=======

We had some problems during the development of this project. At first we tried a diferent project that allowed you to find a quantum circuit given a certain probability histogram. But the technical difficulty of the problem forced us to switch directions. We chose this project because is a classical game that we thought easy to understand and where the user can play with diferent quantum circuits with a clear goal in mind and relatively easy execution. In the development of this especific project we encountered difficulties in the use of a graphic interface because our lack of knowledge in the subject.

It has been a really fun and challenging experience were we have learned a lot about both about quantum and classical computing. 
