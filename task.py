#
# This file is based on pyperplan
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>
#

"""
Classes for representing a STRIPS planning task
"""


class Operator:

    def __init__(self, name, preconditions, add_effects, del_effects):
        """
        The constructor of the class Operator. 

        In a STRIPS planning task, an Operator is an action that can be applied
        to change the state during the execution of a plan.

        In this class all sets are implemented as Python frozensets.
        See more here: https://www.programiz.com/python-programming/methods/built-in/frozenset
        
        @param name The name of the operator (e.g. "action1 operand1 operand2" 
               is the str name of an operator for the action action1 and the
               grounded operands operand1 and operand2)
        @param preconditions The preconditions (the predicates) that need to hold 
               at a given state for the operator to be applicable in state
        @param add_effects the predicates that become true in state after applying 
               the operator
        @param del_effects the predicates that become false in state after applying
               the operator
        """
        self.name = name
        self.preconditions = frozenset(preconditions)
        self.add_effects = frozenset(add_effects)
        self.del_effects = frozenset(del_effects)

    # ---- Step 1 ----
    # Implement the method
    def applicable(self, state):
        """
        Operators are applicable when their set of preconditions is a subset
        of the predicates that are true in "state".

        @return True if the operator's preconditions is a subset of the state,
                False otherwise
        """
        
        if self.preconditions.issubset(state):
            return True
        else:
            return False

        # return None # remove after implementing the method

    # ---- Step 2 ----
    # Implement the method
    def apply(self, state):
        """
        Applying an operator means removing the predicates that are made false
        by the operator from the set of true predicates in state and adding
        the predicates made true.

        Note that therefore it is possible to have operands that make a
        predicate both false and true. This results in the predicate being true
        at the end.

        @param state The state that the operator should be applied to
        @return A new state (set of predicates) after the application of the
                operator
        """

        if self.applicable(state):
            new_state = state - self.del_effects
            new_state = new_state | self.add_effects
            return new_state

        
        # return None # remove after implementing the method

    def __eq__(self, other):
        return (
            self.name == other.name
            and self.preconditions == other.preconditions
            and self.add_effects == other.add_effects
            and self.del_effects == other.del_effects
        )

    def __hash__(self):
        return hash((self.name, self.preconditions, self.add_effects, self.del_effects))

    def __str__(self):
        s = "%s\n" % self.name
        for group, facts in [
            ("PRE", self.preconditions),
            ("ADD", self.add_effects),
            ("DEL", self.del_effects),
        ]:
            for fact in facts:
                s += f"  {group}: {fact}\n"
        return s

    def __repr__(self):
        return "<Op %s>" % self.name


class Task:
    """
    A STRIPS planning task
    """

    def __init__(self, name, facts, initial_state, goals, operators):
        """
        @param name The task's name (i.e. the name of the defined problem)
        @param facts A set of all the predicate names that are valid in the domain
        @param initial_state A set of predicate names that are true at the beginning
        @param goals A set of predicate names that must be true to solve the problem
        @param operators A set of operator instances for the domain
        """
        self.name = name
        self.facts = facts
        self.initial_state = initial_state
        self.goals = goals
        self.operators = operators

    # ---- Step 3 ----
    # Implement the method
    def goal_reached(self, state):
        """
        The goal has been reached if all predicates that are true in "goals"
        are true in "state".

        @param state A state
        @return True if all the goals are reached, False otherwise
        """
        if self.goals.issubset(state):
            return True
        else:
            return False
        
        # return None # remove after implementing the method

    # ---- Step 4 ----
    # Implement the method
    def get_successor_states(self, state):
        """
        Return all the possible next states that can be reached after "state", and
        the operators that need to be applied for reaching the next states.

        For every operator of the Task instance, if an operator is applicable at the
        current "state", store in a list the pair of the operator, and the new (next) state
        that holds when applying the operator in "state".
        
        @param state A state 
        @return A list with (op, new_state) pairs where "op" is the applicable
        operator and "new_state" the state that results when "op" is applied
        in state "state".
        """
        successor_states = []
        for operator in self.operators:
            if operator.applicable(state):
                successor_states.append((operator, operator.apply(state)))

        return successor_states

    def __str__(self):
        s = "Task {0}\n  Vars:  {1}\n  Init:  {2}\n  Goals: {3}\n  Ops:   {4}"
        return s.format(
            self.name,
            ", ".join(self.facts),
            self.initial_state,
            self.goals,
            "\n".join(map(repr, self.operators)),
        )

    def __repr__(self):
        string = "<Task {0}, vars: {1}, operators: {2}>"
        return string.format(self.name, len(self.facts), len(self.operators))
