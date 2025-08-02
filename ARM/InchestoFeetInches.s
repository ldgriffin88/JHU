#
# Program Name: InchestoFeetInches.s
# Author: 	Logan Griffin
# Date: 	6/24/2024
# Purpose: 	Convert number of inches to feet and inches
#

.text
.global main
main:

	# push the stack
	SUB sp, sp, #4
	STR lr, [sp]
	
	# prompt user for total num of inches
	LDR r0, =prompt
	BL printf

	# scan the value
	LDR r0, =format
	LDR r1, =totalInches
	BL scanf

	# math
	LDR r0, =totalInches
	LDR r0, [r0]
	MOV r1, #12
	BL __aeabi_idiv
	MOV r3, r0 // move feet to r3

	# get inches from feet
	MOV r1, #12
	MOV r0, r3
	MUL r0, r1, r3 // total inches covered by feet

	# get inches
	LDR r1, =totalInches
	LDR r1, [r1]
	SUB r1, r1, r0 // subtract and leave value in r1

	# output
	MOV r2, r1
	MOV r1, r3
	LDR r0, =output
	BL printf

	# pop the stack
	LDR lr, [sp]
	ADD sp, sp, #4
	MOV pc, lr

.data
	prompt: .asciz "\nEnter the total number of inches: "
	format: .asciz "%d"
	totalInches: .word 0
	output: .asciz "\nThat equals %d feet and %d inches."
