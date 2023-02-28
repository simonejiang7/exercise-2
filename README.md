# Exercise 2: Automated Planning

A partial implementation of a STRIPS-like planner in Python. The planner solves a problem based on a domain, where both the *problem* and the *domain* are defined in [PDDL 1.2](https://planning.wiki/ref/pddl). The implemenation is based on [pyperplan](https://github.com/aibasel/pyperplan).

## Table of Contents
-   [Requirements](#requirements)
-   [Project structure](#project-structure)
-   [How to run the project](#how-to-run-the-project)
-   [Task 2](#task-2)
-   [Task 3](#task-3)
 
## Requirements
The project requires [Python](https://www.python.org/) >= 3.6.

## Project structure
```bash
├── benchmarks # benchmark examples with domain and problem use cases, which you can use to see the planner behavior
├── examples # simple example of a "block" domain and problem, which you can use to see the planner behavior
│   ├── blocks-world-domain.pddl 
│   └── blocks-world-problem.pddl
├── search # includes implementations of different search algorithms (i.e. astar,wastar,gbf,bfs,ehs,ids,sat)
│   ├── a_star.py # (altered in Task 2) template of A* search algorithm 
│   ├── breadth_first_search.py
│   ├── ...
│   └── searchspace.py # (used in Task 2) includes a class for creating instance nodes that are visited during search 
├── task.py # (altered in for Task 2)  includes classes for creating Operators and STRIPS-like instances  ⟨Propositional arguments, Operators , Initial state , Goals⟩  
├── plan.py # (used in Task 2) the main script for solving a planning problem 
├── pddl # a PDDL parser 
├── heuristics # includes implementations of different heuristic methods (i.e. blind,landmark,lmcut,hadd,hff,hmax,hsa)
├── grounding.py # grounding a schematic PDDL task to a STRIPS planning task
└── planner.py # a STRIPS-like planner
```

## How to run the project 
You can run the script `plan.py` with Python 3 for solving a problem defined in PDDL.
You can specify the following arguments:
- positional arguments:
  - `domain`: the file path of the domain defined in PDDL
  - `problem`: the file path of the problem defined in PDDL

- optional arguments:
  - `-s {astar,wastar,gbf,bfs,ehs,ids,sat}`: the search algorithm from A*, weighted A*, greedy best first, breadth first, enforced hillclimbing, iterative deepening, sat solve (default: bfs)

```
python3 plan.py [-s {astar,wastar,gbf,bfs,ehs,ids,sat}] [domain] problem
```
For example, to run the planner with the breadth-first algorithm:
```
python3 plan.py -s bfs examples/blocks-world-domain.pddl examples/blocks-world-problem.pddl
```
Or to run the planner with the A* algorithm that you implemented in Task 2:
```
python3 plan.py -s astar t1-your-domain.pddl t1-your-problem.pddl
```

## Task 2
- Complete the implementation of [`task.py`](task.py), which includes classes for creating Operators and STRIPS-like instances  ⟨Propositional arguments, Operators , Initial state , Goals⟩:  
     - Implement the methods `applicable()` and `apply()` of the `Operator` class
     - Implement the methods `goal_reached()` and `get_successor_states()` of the `Task` class
     - TIPS:
       - Study the class `Operator` in [`task.py`](task.py) to see how the planner should handle the removal and addition of predicates 
       - Use [Python Frozenset](https://www.programiz.com/python-programming/methods/built-in/frozenset) .
- Complete the implementation of [`a_star.py`](search/a_star.py), which includes methods for searching based on the A* search algorithm:
     - Implement the method `astar_search()`
     - TIPS: 
       - Study the class `Task` in [`task.py`](task.py) to see how the search algorithm should handle STRIPS-like planning tasks
       - Study the class `SearchNode` in [`searchspace.py`](search/searchspace.py) to see how the search algorithm should handle the nodes of the search space 
       - Use the [heapq module](https://pythontic.com/algorithms/heapq/introduction) for handling heaps in Python.

## Task 3
- Examine the `task-3/t3-domain.py` and the `task-3/t3-problem.py`, and the behavior of the planner when solving the problem in the domain, so that you answer the questions provided to you in the exescise sheet: 
  - [`t3-domain.pddl`](task-3/t3-domain.pddl): the domain
  - [`t3-problem.pddl`](task-3/t3-problem.pddl): the problem
  - [`t3-solution.soln`](task-3/t3-solution.soln): a solution to the problem in the domain generated with a classical STRIPS planner
