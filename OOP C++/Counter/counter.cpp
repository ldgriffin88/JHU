#include <iostream>
using namespace std;
# include "counter.h"

/**
 * @file counter.cpp
 * @brief this file implmenets the Counter class 
 * @author Logan Griffin
 * @date 6/16/2025
 */

// constructor
Counter::Counter()
{
    count = 0;
}

void Counter::incrementCount()
{
    count++;
}

void Counter::decrementCount()
{
    count--;
} 

void Counter::resetCount()
{
    count = 0;
}

void Counter::resetMemory()
{
    mem = 0;
}

void Counter::addMemory()
{
    mem = mem + count;
}

int Counter::returnCount()
{
    return count;
}

int Counter::returnMem()
{
    return mem;
}

