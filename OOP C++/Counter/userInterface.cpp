#include <iostream>
using namespace std;
#include <string>
#include "counter.h"
#include "userInterface.h"

/**
 * @file userInterface.cpp
 * @brief this file implmenets the userInterface class 
 * @author Logan Griffin
 * @date 6/16/2025
 */

// constructor
UserInterface::UserInterface( Counter *c)
{
    aCounter = c;
    menuChoice = 0;
}

void UserInterface::displayChoices()
{
    string choices[] = {"1: increment counter",
                        "2: decrement counter",
                        "3: reset counter",
                        "4: add memory value",
                        "5: reset memory value",
                        "6: quit"};
    for (int i = 0; i < 6; i++)
        cout << choices[i] << endl;
}

void UserInterface::getUserInput()
{
    cin >> menuChoice;
}

void UserInterface::displayOutput()
{
    cout << "Current Count: " << aCounter -> returnCount() << endl;
    cout << "Current Memory: " << aCounter -> returnMem() << endl;
}

void UserInterface::executeSelection()
{   
    while (menuChoice != 6)
    {
        displayChoices();
        getUserInput();
        switch (menuChoice)
        {
            case 1: aCounter -> incrementCount(); displayOutput(); break;
            case 2: aCounter -> decrementCount(); displayOutput(); break;
            case 3: aCounter -> resetCount(); displayOutput(); break;
            case 4: aCounter -> addMemory(); displayOutput(); break;
            case 5: aCounter -> resetMemory(); displayOutput(); break;
            case 6: cout << "Program Ending" << endl; break;

        }
    }
}
        
