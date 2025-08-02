/**
 * @file date.h
 * @brief this file declares the Date class 
 * @author Logan Griffin
 * @date 7/21/2025
 */

#pragma once
#include <iostream>
using namespace std;


class Date
{
    // private attributes
    private:
        int day;
        int month;
        int year;
    
    // public methods
    public:
        Date() = default;   
        Date(int, int, int);

        // setters
        void setDay(int); // method to set day
        void setMonth(int); // method to set month
        void setYear(int); // method to set year
        
        // getters 
        int getDay() const; // method to return day
        int getMonth() const; // method to return month
        int getYear() const; // method to return year

        void printDate() const; // method to print date
};