/**
 * @file item.h
 * @brief this file declares the item class 
 * @author Logan Griffin
 * @date 7/5/2025
 */

#pragma once
#include <string>
using namespace std;

class Item
{
    private:
        string productID;
        string description;
        double unitPrice;
    public: 
        // constructors
        Item() = default;
        Item(const std::string& productID,
        const std::string& description,
        double unitPrice);

        // getters
        string getProductID() const;
        string getDescription() const;
        double getUnitPrice() const;

};