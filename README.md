The team is formed by Adrià Riera (adriariera9.9@gmail.com), Berta Casas (bertacasas17@gmail.com), Berta Martínez (bertamp98@gmail.com), Clara Colet (claracd98@gmail.com), Pablo Rodríguez (pablorogra@gmail.com). 

Our project is a quantum labyrinth were the movement inside comes defined by the mesure of a quantum system.

To move in the labyrinth you need to create your circuit, applying gates to two qubits. Depending on the final state you measure in a single shot, the ball is going to move in one direction or another. So if you measure the |00> state the ball is going to move up,|01> down, |10> to the right and |11> to the left. The goal is to find a circuit which gives you a 100% chance to move in the direction you choose. On the other hand, if the circuit you create can collapse to different states, the ball can go to different directions, depending on the probability to get each state. 

You are allowed to use three gates: Hadamard (H), NOT (X) and Rx (R) with pi/2. If you enter another gate, the game won't recognize and will add no gate to the circuit. Make sure to write correctly the gates (H, X, R).

To make the game more entertaining, and add other quantum concepts, you can go through the walls following the rules of the tunneling effect. This means that if the ball is headed in a direction where there is a wall, exists certain probability that the ball will go through. If the wall is thicker, then the probability to go through the wall decreases.

In order for the user to see and understand how exactly the circuit is changing the initial state for each step, there is and histogram that shows the probability to get each state in the measure. The IBM's quantum simulator have been used for this part. It is always possible to get to the final state that you wish to go with a 100% probability, so nullifying completely all the other states. 

There are three labyrinth versions with increasing difficulty. The objective of the first labyrinth is simply to illustrate the behavior of a quantum gate and become familiarized with the program. The second labyrinth aims to get across the concept of interference in a clear way. To do so the initial state has some hadamard gates implemented). For the last level, the most complicated one, the goal is only to have some fun playing!

We have tried to make a game that helped the user to understand how interference worked in the context of quantum computing, and also how quantum gates modify the state of the system. That is why you can only use three gates that allow a certain range of play without becoming intimidating to people with no quantum computing background.



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

The initial project we wanted to present was a little different from this one. Our first idea was, given a probability distribution of the final state, build a circuit which applied to the state |00...0> reproduced the same histogram of probability. 

At first, we solved the problem for 1 qubit. Implementing an arbitrary rotation U we could reproduce every probability distribution. But for 2 qubits, the universal gate you can implement also implies entanglement and it is more complicated. The technical difficulty of the problem forced us to switch directions. 

We chose this new project because is a classical game that we thought easy to understand and where the user can play with different quantum circuits with a clear goal in mind and relatively easy execution. In the development of this especiffic project we encountered difficulties in the use of a graphic interface because our lack of knowledge in the subject.

It has been a really fun and challenging experience were we have learned a lot about both quantum and classical computing. 
