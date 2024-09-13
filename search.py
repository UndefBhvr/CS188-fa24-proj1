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
from game import Directions
from typing import List


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


def tinyMazeSearch(problem: SearchProblem) -> List[Directions]:
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def DFSHelper(
    state, stack: util.Stack, problem: SearchProblem, visited: set
) -> List[Directions]:
    if problem.isGoalState(state):
        return stack.list
    if state in visited:
        return []
    visited.add(state)
    for next_state, act, _ in problem.getSuccessors(state):
        stack.push(act)
        res = DFSHelper(next_state, stack, problem, visited)
        if res != []:
            return res
        stack.pop()
    return []


def depthFirstSearch(problem: SearchProblem) -> List[Directions]:
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
    stack = util.Stack()
    start = problem.getStartState()
    visited = set()
    return DFSHelper(start, stack, problem, visited)
    # util.raiseNotDefined()


def breadthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    queue = util.Queue()
    start = problem.getStartState()
    visited = set()
    queue.push((start, []))
    while not queue.isEmpty():
        state, acts = queue.pop()
        if state in visited:
            continue
        visited.add(state)
        if problem.isGoalState(state):
            return acts
        for next_state, act, _ in problem.getSuccessors(state):
            if next_state in visited:
                continue
            queue.push((next_state, acts + [act]))
    return []
    # util.raiseNotDefined()


def uniformCostSearch(problem: SearchProblem) -> List[Directions]:
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    # Using Dijkstra Algorithm in infinite maps
    pq = util.PriorityQueue()
    start = problem.getStartState()
    pq.push((start, []), 0)
    visited = {}
    while not pq.isEmpty():
        state, acts = pq.pop()
        cost = problem.getCostOfActions(acts)
        if state in visited and visited[state] <= cost:
            continue
        visited[state] = cost
        if problem.isGoalState(state):
            return acts
        for next_state, act, cost in problem.getSuccessors(state):
            new_acts = acts + [act]
            pq.push((next_state, new_acts), problem.getCostOfActions(new_acts))
    return []
    # util.raiseNotDefined()


def nullHeuristic(state, problem=None) -> float:
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic) -> List[Directions]:
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    pq = util.PriorityQueue()
    start = problem.getStartState()
    pq.push((start, []), 0)
    visited = {}
    while not pq.isEmpty():
        state, acts = pq.pop()
        cost = problem.getCostOfActions(acts)
        if state in visited and visited[state] <= cost:
            continue
        visited[state] = cost
        if problem.isGoalState(state):
            return acts
        for next_state, act, cost in problem.getSuccessors(state):
            new_acts = acts + [act]
            cost1 = problem.getCostOfActions(new_acts)
            cost2 = heuristic(next_state, problem)
            pq.push((next_state, new_acts), cost1 + cost2)
    return []
    # util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
