#
# Program Name: Multiply.s
# Author: 	Logan Griffin
# Date: 	7/29/2024
# Purpose: 	Calculate multiplication through recursive addition
#

.text
.global main
main:
	# push the stack
	SUB sp, sp, #4
	STR lr, [sp]

	# prompt and scan for first input
	LDR r0, =prompt1
	BL printf
	LDR r0, =format
	LDR r1, =num1
	BL scanf

	# prompt and scan for second input
	LDR r0, =prompt2
	BL printf
	LDR r0, =format
	LDR r1, =num2
	BL scanf

	# load values to call function
	LDR r0, =num1
	LDR r0, [r0]
	LDR r1, =num2
	LDR r1, [r1]
	BL Mult
	
	# print output
	MOV r1, r0
	LDR r0, =output
	BL printf
	
	# pop the stack
	LDR lr, [sp]
	ADD sp, sp, #4
	MOV pc, lr

.data
	prompt1: .asciz "\nEnter the first number to be multiplied: "
	prompt2: .asciz "\nEnter the second number to be multiplied: "
	output:  .asciz "\nThe product is: %d\n"
	format:	 .asciz "%d"
	num1:    .word 0
	num2: 	 .word 0

# END main

.text
Mult: 
	# push the stack
	SUB sp, sp, #12
	STR lr, [sp, #0]
	STR r4, [sp, #4]
	STR r5, [sp, #8]

	MOV r4, r0 // m
	MOV r5, r1 // n
	
	# if n == 1, return n
	# else return m + Mult(m, n-1)
	CMP r5, #1
	BNE Else
		MOV r0, r4
		B Return
	Else:
		SUB r1, r5, #1
		MOV r0, r4
		BL Mult
		ADD r0, r4, r0
		B Return
	Endif:	

	# pop the stack
	Return:
	LDR lr, [sp, #0]
	LDR r4, [sp, #4]
	LDR r5, [sp, #8]
	ADD sp, sp, #12
	MOV pc, lr
.data

# End Mult
