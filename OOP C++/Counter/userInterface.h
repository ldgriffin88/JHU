#pragma once
#include "counter.h"

/**
 * @file userInterface.h
 * @brief this file declares the userInterface class 
 * @author Logan Griffin
 * @date 6/16/2025
 */

class UserInterface
{
    private: 
        Counter *aCounter;
        int menuChoice;
    public:
        UserInterface( Counter *c );
        void displayChoices();
        void getUserInput();
        void executeSelection();
        void displayOutput();
};
