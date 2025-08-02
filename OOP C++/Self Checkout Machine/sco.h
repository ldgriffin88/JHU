/**
 * @file sco.h
 * @brief this file declares the sco class 
 * @author Logan Griffin
 * @date 7/5/2025
 */

#pragma once
#include "item.h"
#include "cart.h"
#include "verifier.h"
#include "repository.h"

class SCO
{
    private:
        Item allProducts[12];
        int menuChoice;
        double cashAmt;
        Cart cart;
        Verifier verifier;
        Repository repository;
    public:
        SCO(): allProducts{
            {"Meat01", "T-Bone Steak", 7.99},
            {"Meat02", "Tyson Fresh Chicken Wings", 10.00},
            {"Icecream01", "Chocolate Ice Cream", 2.50},
            {"Icecream02", "Vanilla Ice Cream", 2.50},
            {"Corn01", "Fresh Sweet Corn", 2.00},
            {"Casewater01", "24 Bottles 16-Oz of Deer Park Water", 4.99},
            {"Potatochips01", "Plain Potato Chips", 2.00},
            {"Potatochips02", "Green Onion Potato Chips", 2.00},
            {"Donuts01", "Glazed Donuts One-Dozen", 4.99},
            {"Sausage01", "8-Sausage Pack", 4.99},
            {"Eggs01", "Dozen Eggs", 3.00},
            {"Milk01", "Gallon Milk", 4.00}
        }
        {}

        void displayItems();
        void execute();

        // getters
        void getUserInput();
        void getCashAmount();
};  