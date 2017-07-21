# Parallel computing with message queues

## Introduction

Parallel computing refers to groups of processors working together cooperatively to solve a problem. The basic idea is to divide up a big problem into smaller chunks that can be solved independently at the same time, then recombine the individual pieces into a whole solution. A good real-world example is how a group of people can work cooperatively to solve a jigsaw puzzle faster than any individual could,  by first finding the corners and edges of the puzzle, then each participant working to find pieces that seem to fit a color or shape theme, and progressively fit these into larger and larger chunks of the puzzle.

In computing the answers to very hard problems it is often useful to break problems up into smaller pieces and distribute these to a number of independent processors to work on in parallel (hence "parallel computing"). In this exploration we will build a cluster of processors or "nodes" from our individual Raspberry Pis and set them to solving a problem cooperatively.

One of the fundamental things to parallel processing is that the nodes can talk to each other to exchange information and coordinate their individual activities, much as the group solving the jigsaw puzzle might do. People do this through a variety of ways such as talking, moving puzzle pieces around the table, and so on. Likewise, there are many ways to implement communications among collections of processors, but all share these common features:

- A physical medium through which to converse. In our case this will be either wired or wireless ethernet.
- A way for a program running on one node can send a message to another program on another node. For this we will use a "message queue" approach.
- A way to coordinate activities among programs. 



## What is a message queue?

A queue in everyday life is a group of people lined up for something, like paying for groceries or buying concert tickets. In computing a queue is a mechanism for receiving, lining up, and delivering messages in a specific order. Message queues are a kind of "inter-process communication" by which one program can send something interesting to another one. These programs, or "processes" can be running on the same computer or different ones.

As in real life, there are two primary functions: *enqueuing*, or adding something to the queue, and *dequeuing*, or taking something off the queue. Queues can either be *First in First out (FIFO)* as in the picture below, or *Last in First Out (LIFO)*. We typically think of FIFO queues as being more "fair" but there are occasions when LIFO queuing is needed. LIFO queues are also known in computer science as "stacks" and preserve the order of events when things are nested such as in subroutine calls and returns.

![Message queue](https://www.cloudamqp.com/img/blog/message-queue-small.png)

When processes are distributed across different computers a message queue can be used to both order messages in temporal sequence and deliver them to other computers. Examples might include email, Twitter or SMS messages.



​		![Image result for message queue](data:image/png;base64,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)



For our project we will use the Advanced Message Queuing Protocol, an open standard for message queuing. The specific implementation is RabbitMQ at the node level, and Pika, a Python programming interface for RabbitMQ, to be used within your programs.

A schematic for how RabbitMQ and Pika work together is shown below:

![https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_MRG/1.1/html/Messaging_User_Guide/images/producer-consumer.png](https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_MRG/1.1/html/Messaging_User_Guide/images/producer-consumer.png)	

The Producer process uses a programming interface or *binding* to send a message to a *broker*, which places the message in a specific queue. the Consumer process requests a message from a specific queue. When the message is delivered to the Consumer, it is removed from the queue and is no longer available to any other processes. 

We will explore parallel computing using message queues through the following phases:

1. Setting up: Installing RabbitMQ and Pika on your Pi
2. Starting out: Passing messages between processes on the same Pi; Looking at different ways to wait for messages.
3. Getting parallel: Passing messages between two different Pis (you will be working with a buddy)
4. Building a cluster: Passing messages among several Pis.

## 1. Setting up

The first step is to install the RabbitMQ server and the Pika Python programming library, and start the server by rebooting:

```sh
$ sudo apt-get install rabbitmq-server  # install the rabbitMQ server
$ sudo apt-get install python-pika      # install the python library for rabbitMQ
$ sudo reboot                         # restart everything. after reboot rabbitmq-server will run
...
$ sudo rabbitmqctl status                # make sure the message queue broker is running

$ sudo rabbitmqctl status
Status of node rabbit@raspberrypi ...
[{pid,705},
 {running_applications,[{rabbit,"RabbitMQ","3.3.5"},
                        {os_mon,"CPO  CXC 138 46","2.3"},
                        {xmerl,"XML parser","1.3.7"},
                        {mnesia,"MNESIA  CXC 138 12","4.12.3"},
                        {sasl,"SASL  CXC 138 11","2.4.1"},
                        {stdlib,"ERTS  CXC 138 10","2.2"},
                        {kernel,"ERTS  CXC 138 10","3.0.3"}]},
 {os,{unix,linux}},
 {erlang_version,"Erlang/OTP 17 [erts-6.2] [source] [async-threads:30] [kernel-poll:true]\n"},
 {memory,[{total,20828528},
          {connection_procs,1372},
          {queue_procs,2744},
          {plugins,0},
          {other_proc,8778412},
          {mnesia,29360},
          {mgmt_db,0},
          {msg_index,17080},
          {other_ets,378868},
          {binary,12880},
          {code,8903000},
          {atom,490973},
          {other_system,2213839}]},
 {alarms,[]},
 {listeners,[{clustering,25672,"::"},{amqp,5672,"0.0.0.0"}]},
 {vm_memory_high_watermark,0.4},
 {vm_memory_limit,103994163},
 {disk_free_limit,50000000},
 {disk_free,29715111936},
 {file_descriptors,[{total_limit,924},
                    {total_used,3},
                    {sockets_limit,829},
                    {sockets_used,1}]},
 {processes,[{limit,1048576},{used,124}]},
 {run_queue,0},
 {uptime,4891}]
...done.
pi@raspberrypi:~ $ 
```



At this point you have a working message queue installation on your Pi. Time to see what it can do!



## 2. Starting out

### a. Sending a message from one process to another on the same Pi

