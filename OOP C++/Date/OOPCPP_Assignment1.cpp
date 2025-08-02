/*
This assignment involves writing a program that models a simple date. Design a 
Date class that models a date as having a month attribute (1-12), a day attribute (1-31), a year attribute (yyyy), and a month name (January-December). Provide appropriate class constructors, getter methods, setter methods, and any other methods you think are necessary to model a simple date. Write a program that creates at least two dates, invokes their behaviors, and displays their attributes. Leap years should be accounted for. 

Submit your source code and a screen capture of program output. 
Submit your work in a zip file using your first initial, last name, and problem set number as follows: initial_lastname_assignment_1.zip. For example, if your first name is Jane and your last name is Smith, the name of your submit file would be j_smith_assignment_1.zip. 
*/



#include <iostream>
#include "date.h"
using namespace std;

/**
 * @file OOPCP_Assignment1.cpp
 * @brief this file creates a few dates and shows features of the Date class 
 * @author Logan Griffin
 * @date 6/9/2025
 */

int main() {

    // creating a new date
    Date d2(10, "October", 2000);
    d2.printDate();

    // changing the day
    d2.setDay(15);

    // changing the month
    d2.setMonth("January");

    // changing the year
    d2.setYear(1954);

    // printing changed values
    d2.printDate();

    // showing get month method
    cout<< "Month is: " << d2.getMonth() << "\n";
    
    // creating another date to show leap years included
    Date d3(29, "February", 2028);
    d3.printDate();

    // changing the year to an invalid leap year
    // program will throw an error and terminate here
    d3.setYear(2025);

    return 0;
}