/** 
Earlier in the semester we demonstrated the development of an integer array class. Develop a template class for an array in which various types of arrays could be handled. Write a program that creates and displays arrays of integers, floats, strings, and Date objects (where Date objects model a date using integer month, day, year attributes). Submit source code and a screen capture of your executing program. 
 */

 /**
 * @file arrayTGemplate.h
 * @brief this file declares the arrayTemplate class 
 * @author Logan Griffin
 * @date 7/21/2025
 */

#include <iostream>
#include "date.h"
using namespace std;


template <class T> class ArrayTemplate
{
private: T* arrayElements;      //array of type T
            int size;     // size of array

public: ArrayTemplate <T> (int asize);     // constructor
        ~ArrayTemplate <T>();       // destructor
        int getSize();      // getter for size of array
        T& operator[] (int index) const;       // overload operator
};

// constructor
template <class T> ArrayTemplate<T>::ArrayTemplate(int asize)
{
    // assign size
    size = asize;

    // create array
    arrayElements = new T [asize]{};
}

// function to delete array
template <class T> ArrayTemplate<T>::~ArrayTemplate()
{
    delete [] arrayElements;
}

// function to return size
template <class T> int ArrayTemplate<T>::getSize()
{
    return size;
}

// operator overload to return value at index
template <class T> T& ArrayTemplate<T>::operator[](int index) const
{
    if (index < 0 || index >= size)
    {
        cout << "Index out of range." << endl;
    } 
    
    return arrayElements[index];
}

 