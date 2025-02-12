# ROP Emporium
This repository contains my solutions to the ROP Emporium CTF Series, specifically the x86-64 challenges. ROP Emporium is a Capture the Flag (CTF) style challenge that focuses on exploiting buffer overflows with Return-Oriented Programming (ROP) and other low-level techniques. These challenges allow you to sharpen your binary exploitation, debugging, and reverse engineering skills. 

There are plenty of guides that already exist for these challenges, I am instead going to focus on the things that gave me difficulty and my general process for solving this CTF series. 

# Challenges

1 - ret2win

2 - split

3 - callme

4 - write4

5 - badchars

6 - fluff

7 - pivot

8 - ret2csu

# General Approach
I started each challenge with static analysis utiizing readelf, objdump, and eventually ropper to begin.
* First I would run the binary normally
* Second I would run the binary and test the overflow
* After the initial introduction to the binary, I would use readelf, objdump, and ropper each in their own tab of my CLI to perform static analysis. Sometimes the challenges contain a "useful" function with specific rop gadgets. For the challenges that had this avenue available, I analyzed the gadgets and tried to figure out the "intended" solution. Almost all of the "useful" function rop gadgets available lead to a very obvious intended solution route.

After intial analysis, I would start to craft my exploit in parallel with dynamic analysis using gdb-gef. For example I might craft a simple return or call to test parameters and behavior. I would also use gdb to find more information about the binary if needed. Commonly I had to go and examine or dump the Procedure Linkage Table (PLT) and Global Offset Table (GOT) in order to find crucial information needed for my rop-chain to function correctly. 

After this, I would finish the rop chain and test the completion of the challenge for the flag return. Sometimes I would have to go and debug or change small pieces of my solution in order to consistently solve the challenge. A few times I would get about 80-90% of the challenge done and get stuck and have to reseach more about how the stack functions, how certain assembly instructions work, or specific issues I was encountering. 

# Challenge - Specific Commentary
This is a reflection on my undertaking of the rop empoirum CTF website. I've completed all CTFs in x86-64. Because plenty of guides already exist I will just be highlighting my lessons learned / struggles faced and not on the solutions themselves. 
Challenge 1: ret2win 
	This challenge introduces stack overwriting, overwrite the stack base pointer with the address of ret2win() and enjoy. I spent most of my time here introducing myself to pwntools python library and automating some testing. The only difficulty faced was understanding stack alignment and the movaps issue.
Challenge 2: split
	This challenge actually required a real rop chain and not just a return. This was straightforward, but required some work with ropper instead of just objdump
Challenge 3: callme
	while writing this writeup and rerunning my solutions I found a curious fact; callme shares a filename with ret2csu (the 8th challenge) called "encrypted_flag.dat" these files are different and you can only have 1 "active" at a time. My script that attempts to solve all 8 files will not return the flag of the "other" challenge. To get around this I could import zipfile and unzip the archives before I run each to ensure smooth operation, but given the scope of this project I've opted to just attach visual proof of callme running and call it a day. 
Challenge 4: write4 - 
	Oh so this is one of the ways you can arbitraily write to memory, neat. I had a lot of fun with this one. Some trial in error on deciding where to write to.
Challenge 5: badchars - 
	lots of trial and error and a lot of research to refresh myself on binary operations. I knew the route to take for the solution but actually sitting down and getting there was tedious.
Challenge 6: fluff - 
	This challenge gave me the most trouble. I had a good idea of how the 3 assembly instructions worked to create the write function, but actually understanding them so I could utilize them in my rop chain took my over a day of research and trial and error.
Challenge 7: pivot - 
	The answer was not just throwing the new stack location on the stack (why did I even think that would work?) It was setting the stack pointer to the new location. Also had some fun trying to read that location from the terminal in various ways to be able to grab it and add it to the ropchain. 
Challenge 8: ret2csu -
	I watched the blackhat talk 2-3 times while learning how this works. This challenge is actually only the first half of ret2csu. Instead of an actual ret2csu this is only like 80% of it. Instead of calling puts, or write you're calling ret2win() from the got. Shares a file with callme that breaks easily. 
