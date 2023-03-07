(define (problem t1-problem)
    (:domain t1-domain)
    (:objects 
        inh1,inh2 - inh
        time1,endTime1,time1,endTime2 - time
        room1,room2 - room
        )
    (:init(staffAtReception)(canArrive time1 inh1 room1) (before endTime1 (time 24))(lock room1)(canArrive time2 inh2 room2) (before endTime2 (time 24))(lock room2))
    (:goal (AND (setup inh1) (setup inh2)))
)