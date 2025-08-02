/*
In an earlier class lecture, we demonstrated implementing an object-oriented solution for a simple counter. 
Assume we have a need to implement a slightly different counter, one that also has a memory capability, as indicated below:

Use the containment technique that was discussed in class (to build composite classes) to implement a memory counter.
*/

/**
 * @file OOPCPP_Assignment2_2.cpp
 * @brief this file shows the functionality of a counter controlled by user interface
 * @author Logan Griffin
 * @date 6/16/2025
 */

#include <iostream>
using namespace std;
#include "userInterface.h"
#include "counter.h"

int main()
{
    // create counter object
    Counter c;

    // create interface object
    UserInterface anInterface (&c);

    // start execution
    anInterface.executeSelection();
};