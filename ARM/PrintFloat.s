#
# Program Name: PrintFloat.s
# Author:       Logan Griffin
# Date:		6/16/2024
# Purpose:	Takes an input value as a float and outputs it
#

.text
.global main

main:
	# push the stack
	SUB sp, sp, #4
	STR lr, [sp, #0]

	# prompt user for float value
	LDR r0, =prompt1
	BL printf
	
	# store input value
	LDR r0, =format1
	LDR r1, =float1
	BL scanf

	# print the value
	LDR r0, =output1	
	LDR r1, =float1
	VLDR s0, [r1]
	VCVT.F64.F32 d0, s0 
	VMOV r1, r2, d0
	BL printf

	# pop the stack
	LDR lr, [sp, #0]
	ADD sp, sp, #4
	MOV pc, lr
	
	
.data
	float1:  .float 0.0
	prompt1: .asciz "Enter a number as a float: "
	format1: .asciz "%f"
	output1: .asciz "The value entered was: %f\n"
	
