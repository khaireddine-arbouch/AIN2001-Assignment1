# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    
    # Initialize stack for DFS
    stack = util.Stack()
    
    # Initialize visited set to keep track of explored states
    visited = set()
    
    # Push the start state and an empty list of actions to the stack
    stack.push((problem.getStartState(), []))

    while not stack.isEmpty():
        # Pop the current state and its corresponding actions from the stack
        state, actions = stack.pop()

        # Check if the current state is the goal state
        if problem.isGoalState(state):
            return actions

        # Check if the state has been visited before
        if state not in visited:
            # Mark the state as visited
            visited.add(state)
            
            # Get the successors of the current state
            successors = problem.getSuccessors(state)

            # Push the successors onto the stack with updated actions
            for next_state, action, _ in successors:
                if next_state not in visited:
                    stack.push((next_state, actions + [action]))

    # If no solution is found, return an empty list
    return []


def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    
    # Initialize queue for BFS
    queue = util.Queue()
    
    # Initialize visited set to keep track of explored states
    visited = set()
    
    # Push the start state and an empty list of actions to the queue
    queue.push((problem.getStartState(), []))

    while not queue.isEmpty():
        # Dequeue the current state and its corresponding actions from the queue
        state, actions = queue.pop()

        # Check if the current state is the goal state
        if problem.isGoalState(state):
            return actions

        # Check if the state has been visited before
        if state not in visited:
            # Mark the state as visited
            visited.add(state)
            
            # Get the successors of the current state
            successors = problem.getSuccessors(state)

            # Enqueue the successors onto the queue with updated actions
            for next_state, action, _ in successors:
                if next_state not in visited:
                    queue.push((next_state, actions + [action]))

    # If no solution is found, return an empty list
    return []


def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    
    # Initialize priority queue for UCS
    priority_queue = util.PriorityQueue()
    
    # Initialize visited set to keep track of explored states
    visited = set()
    
    # Push the start state, an empty list of actions, and cost 0 to the priority queue
    priority_queue.push((problem.getStartState(), [], 0), 0)

    while not priority_queue.isEmpty():
        # Dequeue the current state, its corresponding actions, and the cost from the priority queue
        state, actions, cost = priority_queue.pop()

        # Check if the current state is the goal state
        if problem.isGoalState(state):
            return actions

        # Check if the state has been visited before
        if state not in visited:
            # Mark the state as visited
            visited.add(state)
            
            # Get the successors of the current state
            successors = problem.getSuccessors(state)

            # Enqueue the successors onto the priority queue with updated actions and cost
            for next_state, action, step_cost in successors:
                if next_state not in visited:
                    total_cost = cost + step_cost
                    priority_queue.push((next_state, actions + [action], total_cost), total_cost)

    # If no solution is found, return an empty list
    return []


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    
    # Initialize priority queue for A*
    priority_queue = util.PriorityQueue()
    
    # Initialize visited set to keep track of explored states
    visited = set()
    
    # Push the start state, an empty list of actions, cost 0, and heuristic value to the priority queue
    start_state = problem.getStartState()
    priority_queue.push((start_state, [], 0), heuristic(start_state, problem))

    while not priority_queue.isEmpty():
        # Dequeue the current state, its corresponding actions, cost, and heuristic value from the priority queue
        state, actions, cost = priority_queue.pop()

        # Check if the current state is the goal state
        if problem.isGoalState(state):
            return actions

        # Check if the state has been visited before
        if state not in visited:
            # Mark the state as visited
            visited.add(state)
            
            # Get the successors of the current state
            successors = problem.getSuccessors(state)

            # Enqueue the successors onto the priority queue with updated actions, cost, and heuristic value
            for next_state, action, step_cost in successors:
                if next_state not in visited:
                    total_cost = cost + step_cost
                    priority = total_cost + heuristic(next_state, problem)
                    priority_queue.push((next_state, actions + [action], total_cost), priority)

    # If no solution is found, return an empty list
    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
