#pragma once

/**
 * @file counter.h
 * @brief this file declares the counter class 
 * @author Logan Griffin
 * @date 6/16/2025
 */

class Counter
{
    private:
        int count;
        int mem;
    public: 
        Counter();
        void incrementCount();
        void decrementCount();
        void resetCount();
        void resetMemory();
        void addMemory();
        int returnCount();
        int returnMem();
};