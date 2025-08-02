#include <iostream>
using namespace std;

/**
 * @file date.h
 * @brief this file declares the Date class 
 * @author Logan Griffin
 * @date 6/9/2025
 */

class Date
{
    // private attributes
    private:
        int day;
        string month;
        int year;
    
    // public methods
    public:
        // date() = default;    
        Date(int, string, int);

        // setters
        void setDay(int); // method to set day
        void setMonth(string); // method to set month
        void setYear(int); // method to set year
        
        // getters 
        int getDay() const; // method to return day
        string getMonth() const; // method to return month
        int getYear() const; // method to return year

        void printDate(); // method to print date
        bool checkDate(); // method to validate the date
};