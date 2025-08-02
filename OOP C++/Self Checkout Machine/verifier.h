/**
 * @file verifier.h
 * @brief this file declares the verifier class 
 * @author Logan Griffin
 * @date 7/5/2025
 */
 #pragma once


 class Verifier
 {
    private:
        int approvalCode;
        void generateCode();
    public:
        Verifier();
        int getApprovalCode();     
 };