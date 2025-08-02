/**
 * @file cart.cpp
 * @brief this file implements the cart class 
 * @author Logan Griffin
 * @date 7/5/2025
 */

#include "item.h"
#include "cart.h"
#include <vector>
#include <iostream>
#include <iomanip>
using namespace std;

// constructor
Cart::Cart() : subtotal(0.0)
{}

// function to add an item to the cart and increment subtotal
void Cart::addItem(Item i)
{
    items.push_back(move(i));
    subtotal += i.getUnitPrice();
}

// displays the items currently in the cart
void Cart::displayCart() const
{
    // print headers
    cout 
    << left << setw(20) << "Item Number"
    << left << setw(20) << "Product ID"
    << left << setw(40) << "Description"
    << right << setw(10) << "Unit Price"
    << "\n";

    // print items
    for (int i = 0; i < items.size(); i++)
    {
        cout 
        << left << setw(20) << i+1
        << left << setw(20) << items[i].getProductID()
        << left << setw(40) << items[i].getDescription()
        << right << setw(10) << fixed << setprecision(2) << items[i].getUnitPrice() 
        << "\n";
    }
    
    // print subtotal
    cout << "\nSubtotal before tax is: $" << subtotal;
}

// returns subtotal
double Cart::getSubtotal() const
{
    return subtotal;
}