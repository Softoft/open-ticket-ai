# MVP

## Features

Queue and Priority Classifiation

Either use you own huggingface model or use the default ATC models

the default queue model diffeentiates between 42 different classes
the priority model beween 5 priorities.

You can match those queues and priorities to you own queues and priorities.

Also you set the queue of the incominngh tickets and the unclassified queue as well as the confidence threshold for the queue model.

## Architecture Implementation

Prety simple QueueClassifier and Priority Classifier just load the huggingface models and runs them.
Then these are mappoed to your local queues, this is just a dictionary you sert in thhe config. Use wildcard * to match
every queue. In almost all cases you will like to have a Misc or Junk Queue where wildcards are moved into.



The same for the priority, but there are only 5 Prios, so wildcard works the same, but wont be needed in most cases.

The TicketClassifier calls both Classifiers at the same time and returns the results.

The TicketClassifier is called by the TicketProcessr, the TicketProcessor then calls its injected TicketSystemAdapter, where it will
call the updateTicket method with the results of the TicketClassifier. The TicketProcessor runs in a loop,
It always fetches the next ticket from the TicketSystemAdapter, then calls the TicketClassifier and updates the ticket with the results.
In Config you can set the polling interval, default is 10 seconds.

Appplication runs as a docker compose service in the same network as otobo web runs.
Specifcally for OTOBO You need to setup the OTOBO Webservices and you need to create a special ATCUser with the needed permissions.
It needs read onto the incoming tickets queue and move into for all queues it should be allowed into. ALso write and or prioritry for the incoming ticket queue.
First prio is updated than queue is updated.

OTOBO As a REST Provider needs to be setup.

Then in trhe config of ATC the URLS are set and the ticket system that is used is setup in yaml config file.



