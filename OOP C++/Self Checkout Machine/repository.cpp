/**
 * @file repository.cpp
 * @brief this file implements the repository class 
 * @author Logan Griffin
 * @date 7/5/2025
 * 
 * The class contains a cash purchase repository and a change repository. The cash purchase repository gets emptied every day. The change repository gets $200 added to it every day. The functions here implement those features by testing when a checkout is occurring. If occurring on a new day, then the change will be added and cash purchase emptied. The cash purchase also has a window where it is being emptied such that it will make the self checkout machine unavailable. That period is set to be 11:30-midnight every day. If the change repository goes below $50.00, the sco will be out of service until it is replenished.
 */

#include "repository.h"
#include <ctime>
#include <iostream>
using namespace std;

// constructor
Repository::Repository() : change(0.00), cashPurchase(0.00), refill(-1)
{}

// checks if current checkout is occurring on new day
void Repository::refillCheck()
{
    // get time values
    time_t now = time(NULL);
    // make into structure
    tm current = *localtime(&now);

    // get day of year
    int day = current.tm_yday;

    int diff;

    // if first refill
    if (refill == -1)
    {
        diff = 1;
    } else if (day >= refill) // if day is later than refill
    {
        diff = day - refill;
    } else // if new year, calculate days since
    {
        diff = day + (365 - refill);
    }

    // add the correct amount of change
    double depositAmt = diff * 200.00;
    change += depositAmt;

    // update day
    refill = day;

    // empty cash Purchase since it also zeroes out every day
    cashPurchase = 0.00;
}

// function to see if the cash purchase is being emptied. If being emptied, then the sco will be unavailable.
bool Repository::maintenance()
{
    // get time values
    time_t now = time(NULL);
    // make into structure
    tm current = *localtime(&now);

    // if between 11:30 and midnight
    if (current.tm_hour == 23 && current.tm_min > 30)
    {
        // empty cash purchase
        cashPurchase = 0.00;

        // sco unavailable
        return true;
    } else 
    {
        // sco available
        return false;
    }
}

double Repository::getChange() const
{
    return change;
}

// update change repository based on customer's payment
void Repository::disperseChange(double c)
{
    cout << "\nReturning change in the amount of: $" << c;
    change -= c;
    cout << "\nChange left in repository is: $" << change;
}

// determine if change balance is below $50.00
bool Repository::checkBalance()
{
    if (change < 50.00)
    {
        // sco unavailable until replenished
        return true;
    } else 
    {
        // sco available
        return false;
    }
}

// function to check if balance is below $50.00 or maintenance occurring
bool Repository::checkIfOpen()
{
    if (checkBalance() || maintenance())
    {
        isOpen = false;
    } else
    {
        isOpen = true;   
    }

    return isOpen;
}

// function to increment cash purchase repository when customer pays with cash
void Repository::addCashPurchase(double n)
{
    cashPurchase += n;
    cout << "\nCash purchase repository is now: $" << cashPurchase << "\n";
}