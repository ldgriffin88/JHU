#
# Program Name: Negative.s
# Author:	Logan Griffin
# Date: 	6/24/2024
# Purpose: 	Negate an integer using 2's complement
#

.text
.global main
main:

	# push the stack
	SUB sp, sp, #4
	STR lr, [sp]

	# prompt user for integer
	LDR r0, =prompt
	BL printf
	
	# scan the value
	LDR r0, =format
	LDR r1, =int
	BL scanf
	
	LDR r0, =int
	LDR r0, [r0]
	MVN r1, r0 // one's complement 
	ADD r1, r1, #1 // add 1

	# output the value
	LDR r0, =output
	BL printf
	
	# pop the stack
	LDR lr, [sp]
	ADD sp, sp, #4
	MOV pc, lr

.data
	prompt: .asciz "\nEnter an integer: "
	output: .asciz "\nThe negated value is: %d\n"
	format: .asciz "%d"
	int: .word 0
	
