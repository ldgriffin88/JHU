#
# Program Name: Mul10.s
# Author: 	Logan Griffin
# Date: 	6/24/2024
# Purpose:     	Multiply an integer by 10 using left shift + add
#

.text
.global main
main:

	# push the stack
	SUB sp, sp, #4
	STR lr, [sp]

	# prompt for integer
	LDR r0, =prompt
	BL printf

	# scan for integer
	LDR r0, =format
	LDR r1, =int
	BL scanf

	# math
	LDR r0, =int
	LDR r0, [r0]
	LSL r1, r0, #3 // shift value by 3
	LSL r2, r0, #1 // shift value by 1

	ADD r0, r1, r2 // add the two shifted values

	# output
	MOV r1, r0
	LDR r0, =output
	BL printf

	# pop the stack
	LDR lr, [sp]
	ADD sp, sp, #4
	MOV pc, lr

.data
	prompt: .asciz "\nEnter an integer: "
	output: .asciz "\nYour integer multiplied by 10 is: %d\n"
	format: .asciz "%d"
	int: .word 0
