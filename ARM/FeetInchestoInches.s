#
# Program Name: FeetInchestoInches.s
# Author: 	Logan Griffin
# Date: 	6/24/2024
# Purpose: 	Convert a number of feet and inches to only inches
#

.text
.global main
main:

	# push the stack
	SUB sp, sp, #4
	STR lr, [sp]

	# prompt user for number of feet
	LDR r0, =prompt1
	BL printf

	# scan the value
	LDR r0, =format
	LDR r1, =totalFeet
	BL scanf

	# prompt user for number of inches
	LDR r0, =prompt2
	BL printf	

	# scan the value
	LDR r0, =format
	LDR r1, =totalInches
	BL scanf

	# math
	LDR r0, =totalFeet
	LDR r0, [r0]
	MOV r1, #12
	MUL r0, r0, r1 // inches from the feet
	LDR r1, =totalInches
	LDR r1, [r1]
	ADD r0, r0, r1
	
	# output the vlaue
	MOV r1, r0
	LDR r0, =output
	BL printf

	# pop the stack
	LDR lr, [sp]
	ADD sp, sp, #4
	MOV pc, lr

.data
	prompt1: .asciz "\nEnter the number of feet: "
	prompt2: .asciz "\nEnter the number of inches: "
	output: .asciz "\nThe total number of inches is: %d\n"
	totalFeet: .word 0
	totalInches: .word 0
	format: .asciz "%d"

