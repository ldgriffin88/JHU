/**
 * @file repository.h
 * @brief this file declares the repository class 
 * @author Logan Griffin
 * @date 7/5/2025
 */

#pragma once
#include <ctime>
using namespace std;

class Repository
{
    private:
        double cashPurchase;
        double change;
        bool isOpen;
        int refill;
        
    public:
        Repository();
        void refillCheck();
        bool maintenance();
        double getChange() const;
        void disperseChange(double c);
        bool checkBalance();
        bool checkIfOpen();
        void addCashPurchase(double n);
};