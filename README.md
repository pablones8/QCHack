Team:
Berta Casas (bertacasas17@gmail.com) 
Clara Colet (claracd98@gmail.com)
Berta Martínez (bertamp98@gmail.com)
Adrià Riera (adriariera9.9@gmail.com)
Pablo Rodríguez (pablorogra@gmail.com)


This project is a labyrinth game where you can move by applying gates to a quantum circuit and measuring the final state.

To move in the labyrinth you need to create your circuit, applying gates to the two qubits. Depending on the final state you mesaure, in a single shot, the ball is going to move in one direction or another; so if you measure the |00> state the ball is going to move up, |01> down, |10> to the right and |11> to the left. The objective is to find the circuit that gives you a 100% chance to move in the direction you choose. On the other hand, if the circuit you create can collapse to diferent states the ball can go to diferent directions, depending on the probability to get each state. 


You are allowed to use thre different gates: Hadamard (H), NOT (X) and Rx (R) with pi/2. If you insert another gate you need to restart the game.


To make the game more entretaining, and add other quantum concepts, you can go through walls following the rules of the tunneling efect. This means that if the ball is headed in a direction where there's a wall there is a certain possibility that the ball will go through said wall. 


In order for the user to see and understand how exactly the circuit is changing the initial state for each step, there is an histogram that shows the probability to get each state in the measure, in other words, it represents the final state. It is always possible to get to the final state that you wish to go with a 100% probability, so nullifying completlly all the other states. 


There are three labyrinth versions with increasing dificulty. The objective of the first labyrinth is simply to ilustrate the behaviour of a quantum gate and become familiarized with the program. The second labyrinth aims to get across the concept of interference in a clear way (to do so the initial state has some hadamard gates implemented so that implementing another hadamard interference appears). And the third, the most complicated one, is just to have some fun playing!


We tried to make a game that helped the user to understand how interference worked in the context of quantum computing, and also how quantum gates modify the state of the system, in particular we use the H, X and Rx(pi/2) that allow a certain range of play whithout becoming intimidating to people whithout a quantum computing background.


We tried to make a game that helped the user to understand how interference worked in the context of quantum computing, and also how quantum gates modify the state of the system, in particular we use the NOT, H and Rx(pi/2) gates, that allows a certain range of play without becoming intimidating to people whithout a quantum computing background. We expand on the concept of interference when discussing the second labyrinth, however the objective of the game is to apply gates with a constuctive interference to the state you want to go to, and a destructive interference to the ones you don't want to go. 


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
  

