#
# Progam Name: Fibonacci.s
# Author:      Logan Griffin
# Date:        7/29/2024
# Purpose:     Recursive calculate Fibonacci number
#
	
.text
.global main
main:

	# push the stack
	SUB sp, sp, #4
	STR lr, [sp]

	# prompt and scan for input
	LDR r0, =prompt
	BL printf
	LDR r0, =format
	LDR r1, =num
	BL scanf
	
	# call function
	LDR r0, =num
	LDR r0, [r0]
	BL Fib

	# print output
	MOV r1, r0
	LDR r0, =output
	BL printf	

	# pop the stack
	LDR lr, [sp]
	ADD sp, sp, #4
	MOV pc, lr

.data
	prompt: .asciz "\nEnter a number: "
	output: .asciz "\nThe Fibonacci value is: %d\n"
	format: .asciz "%d"
	num:    .word  0

# END main

.text
Fib:

	# push the stack
	SUB sp, sp, #12
	STR lr, [sp, #0]
	STR r4, [sp, #4]
	STR r5, [sp, #8]

	MOV r4, r0 // to keep value safe

	CMP r4, #0 
	BNE Equalto1
		MOV r0, #0
		B Return
	Equalto1: 
		CMP r4, #1
		BNE Else
			MOV r0, #1
			B Return
	Else:
		SUB r0, r4, #1
		BL Fib
		MOV r5, r0 // to keep sum
		SUB r0, r4, #2		
		BL Fib
		ADD r0, r0, r5
		B Return
	Endif:	// for good measure

	# pop the stack
	Return:	
	LDR lr, [sp, #0]
	LDR r4, [sp, #4]
	LDR r5, [sp, #8]
	ADD sp, sp, #12
	MOV pc, lr

.data

# END Fib
