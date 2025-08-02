#
# Program Name: Inches2Feet.s
# Author: 	Logan Griffin
# Date: 	7/8/2024
# Purpose: 	Convert inches to whole feet
# 

.text
.global main

main:
	
	# push the stack
	SUB sp, sp, #4
	STR lr, [sp, #0]
	
	# prompt for input
	LDR r0, =prompt1
	BL printf

	# scan for input
	LDR r0, =format
	LDR r1, =num1
	BL scanf

	LDR r0, =num1
	LDR r0, [r0]
	BL Inches2Ft
	MOV r1, r0

	# print feet
	LDR r0, =output
	BL printf

	# pop the stack
	LDR lr, [sp, #0]
	ADD sp, sp, #4
	MOV pc, lr

.data

	prompt1: .asciz "\nEnter the length in inches you want in feet: \n"
	output: .asciz "\nThe length in feet is: %d\n"
	format: .asciz "%d"
	num1: .word 0
