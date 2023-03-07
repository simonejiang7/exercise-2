(define (problem t1-problem)
    (:domain t1-domain)
    (:objects 
        inh1 inh2 - inh
        time1 endTime1 time1 endTime2 - time
        room1 room2 - room
        )
    (:init(lock room1)(before time1 endTime1)(canArrive time1 inh1 room1)(staffAtReception)(lock room2)(before time2 endTieme2)(canArrive time2 inh2 room2))
    (:goal (AND (setup inh1) (before time1 endTime1 ) (setup inh2)(before time1 endTime1)(staffAtReception)))
)