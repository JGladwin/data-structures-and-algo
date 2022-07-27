C++:

Install g++ compiler before proceeding.

For local compilation, #include <bits/stdc++.h> can be used for compilation for the g++ compiler. This header file allows us to include the entire standard library. Thus, it is not needed to add libraries like iostream, vector and algorithm. This header file is not found in the clang or MSVC compilers.


C++11 Code can be compiled using:

g++ -std=c++11 -O2 -Wall test.cpp -o test

Program 1:
int a, b;
string x;
cin>>a>>b>>c; 

Terminal:

123 456 monkey

  (or)
    
123     456
monkey

Explanation: the different arguments given in the terminal for cin is differentiated by either a new line or space

-> scanf and printf can be used as alternatives to cin and cout

-> Sometimes, input and output are bottlenecks in a program. The following lines at the beginnning of the code makes I/O more efficient:

ios::sync_with_stdio(0);
cin.tie(0);

-> \n works faster than endl for line breaks because endl always causes flush operation

what is flush operation? writing from primary to secondary storage is called flush operation

Applications generally do not write directly to storage (hdd, ssd, etc). They write to buffers in memory. flush writes the information stored in these buffers to storage.

This is done for efficient operation of your computer. Many times in UNIX/Linux temp files are created for application purposes. These temp files are deleted as the application closes. So in many cases these temp files live briefly in a buffer and never actually get written to storage.

But sometimes, like with databases, you want to make sure the data gets to storage. In these cases you can flush the buffers so a power failure is less likely to leave the data in a questionable state.

-> For getting the whole line as input, use getline

eg.
string s;
getline(cin,s);
