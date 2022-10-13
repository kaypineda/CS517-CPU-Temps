# CS517-CPU-Temps
CS 517 Semester Project, Fall 2022

# Requirements
* Python 3.10

# Usage
```
python3 cpu-temps.py input-file
```
or
```
python cpu-temps.py input-file
```

# Sample Execution and Output
The program should produce an output text file that looks similar to:
```
     0 <= x <      30; y_0      =      61.0000 +   0.6333x; interpolation
    30 <= x <      60; y_1      =      98.0000 +  -0.6000x; interpolation
    60 <= x <      90; y_2      =      20.0000 +   0.7000x; interpolation
    90 <= x <     120; y_3      =     128.0000 +  -0.5000x; interpolation
   120 <= x <     150; y_4      =      12.0000 +   0.4667x; interpolation
   150 <= x <     180; y_5      =     112.0000 +  -0.2000x; interpolation
   180 <= x <     210; y_6      =      34.0000 +   0.2333x; interpolation
   210 <= x <     240; y_7      =     146.0000 +  -0.3000x; interpolation
   240 <= x <     270; y_8      =       2.0000 +   0.3000x; interpolation
   270 <= x <     300; y_9      =     137.0000 +  -0.2000x; interpolation
   300 <= x <     330; y_10     =     197.0000 +  -0.4000x; interpolation
   330 <= x <     360; y_11     =     -78.0000 +   0.4333x; interpolation
   360 <= x <     390; y_12     =     222.0000 +  -0.4000x; interpolation
   390 <= x <     420; y_13     =      79.0000 +  -0.0333x; interpolation
   420 <= x <     450; y_14     =    -215.0000 +   0.6667x; interpolation
   450 <= x <     480; y_15     =      85.0000 +   0.0000x; interpolation
   480 <= x <     510; y_16     =     389.0000 +  -0.6333x; interpolation
   510 <= x <     540; y_17     =     151.0000 +  -0.1667x; interpolation
   540 <= x <     570; y_18     =    -353.0000 +   0.7667x; interpolation
   570 <= x <     600; y_19     =     445.0000 +  -0.6333x; interpolation
   600 <= x <     630; y_20     =      45.0000 +   0.0333x; interpolation
   ...
```