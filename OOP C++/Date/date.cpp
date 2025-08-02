#include <iostream>
#include "date.h"
#include <map>
using namespace std;

/**
 * @file date.cpp
 * @brief this file implmenets the Date class 
 * @author Logan Griffin
 * @date 6/9/2025
 */

// constructor
Date::Date(int d, string m, int y)
{
    day = d;
    month = m;
    year = y;

    if (!checkDate())
    {
        cout<< "Date: " << month << " / " << day << " / " << year << " is invalid.\n";
        throw runtime_error("Invalid Date!");
    };
}

// method to set day
// takes an integer
void Date::setDay(int d) 
{ 
    day = d;

    if (!checkDate())
    {
        cout<< "Date: " << month << " / " << day << " / " << year << " is invalid.\n";
        throw runtime_error("Invalid Date!");
    };
} 

// method to set month
// takes a string
void Date::setMonth(string m) 
{
    month = m;
    
    if (!checkDate())
    {
        cout<< "Date: " << month << " / " << day << " / " << year << " is invalid.\n";
        throw runtime_error("Invalid Date!");
    };
} 

// method to set year
// takes an integer
void Date::setYear(int y) 
{
    year = y;

    if (!checkDate())
    {
        cout<< "Date: " << month << " / " << day << " / " << year << " is invalid.\n";
        throw runtime_error("Invalid Date!");
    };
} 

// method to return day
int Date::getDay() const { return day; } 

// method to return month string
string Date::getMonth() const{ return month; } 

// method to return year
int Date::getYear() const { return year; }

// method to print date
void Date::printDate()
{
    cout<< "Date is: " << month << " / " << day << " / " << year << "\n";
}

// method to check a date
// returns true if date is valid, false if not
bool Date::checkDate()
{
    // define months and days
    static const map<string, int> monthsAndDays = {
        {"January", 31},
        {"February", 28},
        {"March", 31},
        {"April", 30},
        {"May", 31},
        {"June", 30},
        {"July", 31},
        {"August", 31},
        {"September",30},
        {"October", 31},
        {"November", 30},
        {"December", 31}
    };

    
    // look for month in map
    auto it = monthsAndDays.find(month);
    if (it == monthsAndDays.end())
        return false;

    // months exists, now check days
    int daysInMonth = it->second;

    // check if leap year
    bool leapYear = false;
    if ((year % 4 == 0 and year % 100 != 0) || (year % 400 == 0))
        leapYear = true;

    // change days if month is February and leap year
    if (month == "February" && leapYear == true)
        daysInMonth = 29;

    // check for valid days and year
    if (day < 1 || day > daysInMonth || year < 0)
        return false;

    return true;
}
