#
# Program Name: C2F.s
# Author: 	Logan Griffin
# Date: 	7/8/2024
# Purpose: 	Convert celsius to fahrenheit
#

.text
.global main

main: 
	# push the tack
	SUB sp, sp, #4
	STR lr, [sp]

	# prompt for input
	LDR r0, =prompt1
	BL printf

	# scan
	LDR r0, =format1
	LDR r1, =num1
	BL scanf

	LDR r0, = num1
	LDR r0, [r0]
	BL C2F
	MOV r1, r0

	# print
	LDR r0, =output
	BL printf

	# pop the stack
	LDR lr, [sp]
	ADD sp, sp, #4
	MOV pc, lr

.data
	
	prompt1: .asciz "\nEnter the temperature in C you want in F: \n"
	output: .asciz "\nThe temperature in F is: %d\n"
	format1: .asciz "%d"
	num1: .word 0
