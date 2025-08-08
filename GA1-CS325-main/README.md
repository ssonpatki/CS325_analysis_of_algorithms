# 325---GA1
CS325: Analysis of Algorithms, Fall 2024 Group Assignment 1 Due: Tue, 10/15/24

Homework Policy:
Students should work on group assignments in groups of preferably three people. Each group submits to CANVAS a zip ﬁle that includes their source code and their typeset report. The report must include the name of all group members. Speciﬁcally, for this assignment your zipped folder should contain two ﬁles named assignment1.pdf, and assignment1.py. One submission from each group is suﬃcient.
The goal of the homework assignments is for you to learn solving algorithmic problems. So, I recommend spending suﬃcient time thinking about problems individually before discussing them with your friends.
You are allowed to discuss the problems with other groups, and you are allowed to use other resources, but you must cite them. Also, you must write everything in your own words, copying verbatim is plagiarism.
I don’t know policy: you may write ”I don’t know” and nothing else to answer a question and receive 25 percent of the total points for that problem whereas a completely wrong answer will receive zero.
Algorithms should be explained in plain english. You can use pseudocodes if it helps your explanation, but the grader will not try to understand a complicated pseudocode.
More items might be added to this list. ©
A library is organizing a book release event that spans D days.

Several book clubs have

registered to participate, and each club wishes to attend the event together on the same day. In total, there are n book clubs, with each club having a diﬀerent number of members: c1, c2, . . . , cn. The book clubs registered sequentially, meaning that club i signed up before club j if i < j, which gives them priority in scheduling. The library needs to determine the minimum number of attendees they must accommodate each day to ensure:

All clubs get to attend the event within the D days.
Every club attends together, without any members being split across diﬀerent days.
The order of registration is respected: any club that registered earlier must attend before or
n the same day as any later club.
To help the library plan the event eﬀectively, we need to solve the following:

Design an algorithm with O(n logC) time complexity to ﬁnd the minimum number of atten- dees to accommodate per day, where n is the number of book clubs and C is the total number
f attendees: C = ∑n i=1 ci.
Design a polynomial time algorithm for this problem with a runtime depending only on n, without considering C.
Report (60%). In your report, include the description of your algorithms, running time analysis, and proof of correctness. Algorithms should be explained in plain english. You can use pseudocodes if it helps your explanation, but the grader will not try to understand a complicated pseudocode. Part (A) is worth 40 percent and part (B) 20 percent. Any polynomial time algorithm for part (B) receives full credit. A surprisingly fast algorithm can receive extra credit.

Code (40%). Submit a python program that computes the minimum number of attendees to accommodate per day to ﬁnish the event in D days. Your program will be tested against several test cases, for correctness and eﬃciency. For each test case, the program will be automatically stopped after 20 seconds if it is not done in that time. In this case, the group will miss the points of that test case.

Note: it is important that your output is formatted as described below, since your codes will be tested automatically. Speciﬁcally, you must implement the function “min num attendees” in the following code. The code you submit will be an implementation of this procedure in a ﬁle named “assignment1.py”.


Input/Output. The input ﬁle is composed two lines. The ﬁrst line is a one integer 1 ≤ D ≤ 106. The second line contains n integers g1, g2, . . . , gn that are separated by commas; you can assume that 1 ≤ n ≤ 106 and that for all 1 ≤ i ≤ n, we have 1 ≤ gi ≤ 106.

The output ﬁle must composed of one line that contains a single integer that is the min number of attendees per day per day that guarantees that all clubs can attend the event in D days in order.



