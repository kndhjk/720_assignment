# 720_assignment
Computer Science 720 S1 – (2025)
Assignment 1 (part 1)
Requirements
For this part of Assignment 1 we want to see if you can extend the ideas for enumerating and ranking
efficiently a basic type of combinatorial objecs.
Consider binary strings B2n of length n where there are no contiguous subsequence of length longer
than two. Consider lexicographic ordering of B2n. For example:
B24 = {0010, 0011, 0100, 0101, 0110, 1001, 1010, 1011, 1100, 1101}
Write programs for the following problems, where the size constraints of x ∈ B2n are limited to
1 ≤ n ≤ 1000.
count: Given an integer n, output |B2n|.
successor: Given a string x of B2n print the successor of x, or ’None’ if x is the last one in the lexicographic
enumeration.
rank: Given a string x of B2n print the rank of x in the lex order. Remember the first element of
B2n, namely 00100100100..., has rank of 0.
There will be easy and hard test cases available to solve for each problem. Input, taken from
keyboard/stdin, will be several instances consisting of several lines of test strings x ∈ B2n. The first
line of each test file will be an integer 1 ≤ m ≤ 10000 denoting the number of tests in that file. This
is followed by m tests, each on its own line.
Submission and Marks
Due: Saturday, April 12 (11.59pm).
All solutions should be submitted to http://www.cs.auckland.ac.nz/automated-marker
Your single-source-file programs should use one of the valid programming language extension allowed.
Please read the automarker help/FAQ page. Develop and program your own solutions (e.g. don’t
search the Internet or share code with fellow classmates). You are allowed to submit up to 8 times
before a 20% penalty per task is applied.
This assignment is worth half 10% of your final grade. Note the second part of the assignment will
be worth 15% and also due the same day so try to complete this part as early as possible..
sample1 in:
3
2
4
8
sample1 output:
4
10
68
sample2 input:
3
1101001
00110011
10101010
sample2 output:
1101010
00110100
10101011
sample3 input:
3
100100
1101100
1001010101100
sample3 output:
13
40
412

