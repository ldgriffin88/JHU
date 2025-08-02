/**
 * @file item.cpp
 * @brief this file implements the Item class 
 * @author Logan Griffin
 * @date 7/5/2025
 */

# include "item.h"

// constructor
Item::Item(const string& productID, const string& description, double unitPrice): productID(productID), description(description), unitPrice(unitPrice) 
{}

string Item::getProductID() const 
{
    return productID; 
}

string Item::getDescription() const 
{
    return description;
}

double Item::getUnitPrice() const 
{
    return unitPrice; 
}