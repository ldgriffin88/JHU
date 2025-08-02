#
# Program Name: kphCalc.s
# Author:	Logan Griffin
# Date: 	7/8/2024
# Purpose:	Convert a number of miles and hours into kilometers per hour
#

.text
.global main

main:

	# push the stack
	SUB sp, sp, #4
	STR lr, [sp, #0]

	# prompt for input miles
	LDR r0, =prompt1
	BL printf

	# scan
	LDR r0, =input1
	LDR r1, =num1
	BL scanf

	# prompt for input hours
	LDR r0, =prompt2
	BL printf

	# scan
	LDR r0, =input1
	LDR r1, =num2
	BL scanf

	# convert to kilometers/hour
	LDR r0, =num2
	LDR r0, [r0]
	LDR r1, =num1
	LDR r1, [r1]
	BL kph
	MOV r1, r0

	# print kilometers/hour
	LDR r0, = format1
	BL printf

	# pop the stack
	LDR lr, [sp, #0]
	ADD sp, sp, #4
	MOV pc, lr
	
.data

	prompt1: .asciz "\nEnter the number of miles: \n"
	format1: .asciz "The calculated kph is: %d\n"
	prompt2: .asciz "Enter the number of hours: \n"
	input1: .asciz "%d"
	num1: .word 0
	num2: .word 0
	
