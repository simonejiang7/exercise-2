(define (domain t1-domain)
    (:requirements :strips :typing)
    (:types time inh room)
    (:predicates (canArrive ?t - time ?i - inh ?r - room)
            (before ?t1 -time ?t2 - time)
            (lock ?r - room)
            (staffAtReception)
            )
    (:action unlock
        :parameters (?t1 - time ?t2 - time ?i - inh ?r - room)
        :precondition (
            and (lock ?r) (before ?t1 ?t2) (canArrive ?t1 ?i ?r) (staffAtReception)
        )
        :effect (
            and (not (lock ?r)) (arrive ?t1 ?i ?r) (not (staffAtReception))
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
        :parameters (?t1 - time ?t2 - time ?i - inh ?r - room)
        :precondition (
            (join ?t1 ?i ?r)
        )
        :effect(
            and(setup ?i ?r) (before ?t1 ?t2) (staffAtReception)
        )
    )
)