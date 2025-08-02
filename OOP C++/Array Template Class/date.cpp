#include <iostream>
#include "date.h"
#include <map>
using namespace std;

/**
 * @file date.cpp
 * @brief this file implements the Date class 
 * @author Logan Griffin
 * @date 7/21/2025
 */


// constructor
Date::Date(int m, int d, int y)
{
    day = d;
    month = m;
    year = y;
}

// method to set day
// takes an integer
void Date::setDay(int d) 
{ 
    day = d;
} 

// method to set month
// takes a string
void Date::setMonth(int m) 
{
    month = m;
}

// method to set year
// takes an integer
void Date::setYear(int y) 
{
    year = y;
} 

// method to return day
int Date::getDay() const { return day; } 

// method to return month string
int Date::getMonth() const{ return month; } 

// method to return year
int Date::getYear() const { return year; }

// method to print date
void Date::printDate() const
{
    cout<< "Date is: " << month << " / " << day << " / " << year << "\n";
}
