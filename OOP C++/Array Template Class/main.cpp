/**
 * @file main.cpp
 * @brief this file demonstrates the use of a template array class
 * @author Logan Griffin
 * @date 7/21/2025
 */

#include "arrayTemplate.h"
#include "date.h"
#include <string>
using namespace std; 


int main()
{
    // create arrays
    ArrayTemplate <int> integers(3);
    ArrayTemplate <float> floatNums(3);
    ArrayTemplate <string> words(3);
    ArrayTemplate <Date> dates(3);

    integers[0] = 50;
    integers[1] = 100;

    floatNums[0] = 3.14;
    floatNums[1] = 5.5;

    words[0] = "object";
    words[1] = "oriented";
    words[2] = "programming";

    Date d1(7, 21, 2025);
    Date d2(7, 4, 1776);
    dates[0] = d1;
    dates[1] = d2;

    cout << "\n\nInteger Array:" << "\n";
    for (int j = 0; j < integers.getSize(); j++)
    {
        cout << integers[j] << endl;
    }

    cout << "\n\nFloat Array:" << "\n";
    for (int j = 0; j < floatNums.getSize(); j++)
    {
        cout << floatNums[j] << endl;
    }

    cout << "\n\nWords Array:" << "\n";
    for (int j = 0; j < words.getSize(); j++)
    {
        cout << words[j] << endl;
    }

    cout << "\n\nDate Array:" << "\n";
    for (int j = 0; j < dates.getSize(); j++)
    {
        dates[j].printDate();

        cout << "\n";
    }
    
}