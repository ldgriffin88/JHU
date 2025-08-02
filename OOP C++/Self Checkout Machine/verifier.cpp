/**
 * @file verifier.cpp
 * @brief this file implements the verifier class 
 * @author Logan Griffin
 * @date 7/5/2025
 */

 #include "verifier.h"

 // constructor
 Verifier::Verifier() : approvalCode(0)
 {}

 // provide approval code
 int Verifier::getApprovalCode()
 {
    generateCode();
    return approvalCode;
 }

 // increment the code
 void Verifier::generateCode()
 {
    ++approvalCode;
 }