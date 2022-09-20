Auto93 is a dataset which draws automobile data based on the standards following the
 year 1993.

This gives us some insights about the various properties of four-wheeler automobiles 
in general with a certain domain of values. Let's go over all the attributes one by one.

LINE 1 ->
The first line, to be precise the first row (or tuple) consists of names of type string of 
all the attributes in an abbreviated form and below is the list of actual names followed
 by the abbreviated attribute names mentoned in the csv.
I. Cylinders -- Clndrs
Specifies the number of cylinders a model possesses
II. Volume -- Volume
Specifies the volume based on the basic dimensions
III. Horse Power -- Hp
Horse power is is a unit of measurement of power, or the rate at which work is done, 
usually in reference to the output of engines or motors.
IV. Weight in Pounds -- Lbs
As the name suggests, it specifies the weight in pounds which is abbreviated as LBs or
 Lbs
V. Acceleration -- Acc+
Acceleration is rate of change of velocity which is the rate of change of speed, to be
 precise how the vehicle speeds up or speeds down determined by its acceleration
VI. Model -- Model
VII. Origin -- origin
VIII. Miles Per Gallon -- Mpg+
MPG, or miles per gallon, is the distance, measured in miles, that a car can travel per
 gallon of fuel. MPG is also the primary measurement of a car's fuel efficiency: The 
higher a car's MPG, the more fuel efficient it is

REMAINING LINES ->
Henceforth, all the lines, rows to be precise consist of actual numeric values of 
corresponding attributes mentioned in the previous line i.e. line 1.

NOTE: Values are aligned and delimited by blanks. There are two data lines for each
 case.

Cars were selected at random from among 1993 passenger car models that were listed
 in both the _Consumer Reports_ issue and the _PACE Buying Guide_.  Pickup trucks
 and Sport/Utility vehicles were eliminated due to incomplete information in the 
_Consumer Reports_ source.  Duplicate models (e.g., Dodge Shadow and Plymouth 
Sundance) were listed at most once.

PEDAGOGICAL NOTES:
This is a multi-purpose dataset that can be used at many points in an introductory course.
It includes many good numeric variables and several options for dividing the cars up into 
groups. Students tend to be familiar with most of the variables (and specific car models).  
They can anticipate and pose explanations for many of the relationships to be found in the
data, although some surprises may be encountered.  One can easily find examples of pairs
of variables that demonstrate strong or weak, positive or negative associations.  PRICE 
and MPG variables tend to be popular choices as "dependent" variables.  Basic graphs will
often reveal unusual data values (like the price for a Mercedes-Benz).