/**
 * @file sco.cpp
 * @brief this file implements the SCO class 
 * @author Logan Griffin
 * @date 7/5/2025
 * 
 * This class simulates a self checkout machine. The execute function will first check to see if the machine needs to be refilled with change and if the cash purchase repository needs to be emptied. After that, it will display the items available in the store for the user to checkout. The user repeatedly selects which items they want to buy, and the sco displays their cart and subtotal. When the user is done scanning items, they are prompted for payment method.The payment methods are either credit, debit, or cash. If credit or debit, the sco uses a verifier to get an approval code. If cash, the sco asks how much cash and then provides thhe correct change, updating its repository's change and cash purchase repository. Enter 'y' at the end of a checkout to start a new checkout.
 */

#include "sco.h"
#include "cart.h"
#include "repository.h"
#include <iomanip>
#include <iostream>
using namespace std;

// main execution function
void SCO::execute()
{   
    // char to run while loop
    char run = 'y';

    // check if new day in order to replenish change or empty cash
    repository.refillCheck();

    // while customers are checking out
    while (run == 'y')
    {
        // check to see that it is not in the maintenance period or if there is not enough change left
        if (!repository.checkIfOpen())
        {
            cout << "Maintenance in progress. Try again tomorrow.";
            run = 'n';
        } else 
        {
            // if sco is available
            // display available items
            displayItems();
            cout << "\nEnter the item number of your first item:  ";

            // while there are still items to "scan"
            while (menuChoice != 0)
            {
                // gather user choice
                getUserInput();

                // add correct item to cart
                switch (menuChoice)
                {
                    case 1: cart.addItem(allProducts[0]); break;
                    case 2: cart.addItem(allProducts[1]); break;
                    case 3: cart.addItem(allProducts[2]); break;
                    case 4: cart.addItem(allProducts[3]); break;
                    case 5: cart.addItem(allProducts[4]); break;
                    case 6: cart.addItem(allProducts[5]); break;
                    case 7: cart.addItem(allProducts[6]); break;
                    case 8: cart.addItem(allProducts[7]); break;
                    case 9: cart.addItem(allProducts[8]); break;
                    case 10: cart.addItem(allProducts[9]); break;
                    case 11: cart.addItem(allProducts[10]); break;
                    case 12: cart.addItem(allProducts[11]); break;
                    case 0: cout << "\nChecking out:\n"; break;
                }

                // display the cart
                cout << "\nYour Cart is: \n";
                cart.displayCart();

                // prompt for next item
                cout << "\n\nEnter the number of the next item you are buying, or enter 0 to check out:  ";
            }

            // display final cart
            cout << "\n\nHere is your final cart: \n";
            cart.displayCart();

            // calculate subtotal and total
            double tax = cart.getSubtotal() * .05;
            cout << "\nTax is: $" << tax;
            double total  = cart.getSubtotal() + tax;
            cout << "\nYour total with tax is: $" << total << "\n";

            // reset menu choice to get payment method
            menuChoice = 0;

            // prompt for payment method
            while (menuChoice < 1 || menuChoice > 3)
            {
                cout << "\nPlease specify payment method: \n 1) Credit Card \n 2) Debit Card \n 3) Cash\n";
                getUserInput();
            }

            // if paying with credit card, need to verify and return verification number
            if (menuChoice == 1 || menuChoice == 2)
            {
                // verify payment
                cout << "Transaction approved. Approval code: " << verifier.getApprovalCode();
            } else if (menuChoice == 3)
            {   
                // prompt for how much cash customer wants to pay with
                cout << "Please enter the amount of cash you will be paying with in the format of dollars and cents: \n";
                getCashAmount();

                // calcualte change due
                double changeDue = cashAmt - total;
                
                // display amonts
                cout << "\nCash amount is: " << cashAmt << "\n";
                cout << "\nTotal is: " << total << "\n";

                // keep asking for new change amount as long as 
                while (changeDue > repository.getChange() || changeDue < 0)
                {
                    if (changeDue > repository.getChange())
                    {
                        cout << "\nInvalid cash amount. Cannot provide enough change.\n";
                    } else if (changeDue < 0)
                    {
                        cout << "\nCash amount is less than total.\n";
                    }
                    
                    cout << "\nPlease enter the amount of cash you will be paying with in the format of dollars and cents: \n";
                    getCashAmount();
                    changeDue = cashAmt - total;
                }
                
                // give change and subtract from change repo
                repository.disperseChange(changeDue);
                repository.addCashPurchase(cashAmt);

                if (!repository.checkIfOpen())
                {
                    // below 50 dollars
                    // shut down until cash is replenished
                    cout << "Change below $50.00. Message sent to SCO control center. The SCO will be available when change is replenished.";
                }
            }

            // print final receipt and prompt for new checkout
            cout << "\n\nThank you for shopping with us.";
            cout << "\nAnother customer? Enter 'y'/'n':  ";
            cin >> run;
            
        }
    }

    // end program
    cout << "\n\nProgram Ending" << endl;
}

void SCO::getUserInput()
{
    cin >> menuChoice;
}

void SCO::getCashAmount()
{
    cin >> cashAmt;
}

void SCO::displayItems()
{   
    cout << "\n\n" 
    << left << setw(20) << "Item Number"
    << left << setw(20) << "Product ID"
    << left << setw(40) << "Description"
    << right << setw(10) << "Unit Price"
    << "\n";

    for (int i = 0; i < 12; i++)
    {
        cout 
        << left << setw(20) << i+1
        << left << setw(20) << allProducts[i].getProductID()
        << left << setw(40) << allProducts[i].getDescription()
        << right << setw(10) << fixed << setprecision(2) << allProducts[i].getUnitPrice() 
        << "\n";
    }
}