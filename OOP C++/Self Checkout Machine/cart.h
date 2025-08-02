/**
 * @file cart.h
 * @brief this file declares the cart class 
 * @author Logan Griffin
 * @date 7/5/2025
 */

#pragma once
#include "item.h"
#include <vector>
using namespace std;

class Cart
{
    private:
        vector<Item> items;
        double subtotal;
    public:
        Cart();
        void addItem(Item i);
        void displayCart() const;
        double getSubtotal() const;
};
