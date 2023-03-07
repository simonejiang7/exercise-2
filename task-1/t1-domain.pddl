(define (domain t1-domain)
    (:requirements :strips :typing)
    (:types time inh room)
    (:predicates (canArrive ?t - time ?i - inh ?r - room)
            (before ?t1 -time ?t2 - time)
            (lock ?r - room)
            (staffAtReception)
            )
    (:action unlock
        :parameters (?t - time ?i - inh ?r - room)
        :precondition (
            and (lock ?r) (before ?t (time 24)) (canArrive ?t ?i ?r) (staffAtReception)
        )
        :effect (
            and (not (lock ?r)) (not (canArrive ?t ?i ?r)) (arrive ?t ?i ?r) (not (staffAtReception))
        )
    )
    (:action join
        :parameters (?t - time ?i - inh ?r - room)
        :precondition (
            and (arrive ?t ?i ?r) 
        )
        :effect(
            (join ?t ?i ?r)
        )
    )
    (:action showRoom
        :parameters (?t - time ?i - inh ?r - room)
        :precondition (
            (join ?t ?i ?r)
        )
        :effect(
            and(setup ?i ?r) (before ?t (time 24)) (staffAtReception)
        )
    )
)