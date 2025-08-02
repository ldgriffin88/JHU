# Ft2Inches.s
# An Assembly program to calculate Feet to Inches
.text
.global main

main:
	# save retrun to os on stack
	SUB sp, sp, #4
	STR lr, [sp, #0]
	
	# prompt for input in feet
	LDR r0, = prompt1
	BL printf
	
	# scan for input
	LDR r0, =input1
	SUB sp, sp, #4
	MOV r1, sp
	BL scanf
	LDR r0, [sp, #0]
	ADD sp, sp, #4
	
	#  convert
	BL Ft2Inches
	MOV r1, r0
	
	# print inches
	LDR r0, =format1
	BL printf
	
	# return to os
	LDR lr, [sp, #0]
	ADD sp, sp, #4
	MOV pc, lr

.data
	prompt1: .asciz "Enter the length in feet yo want in inches: \n"
	format1: .asciz "\nThe length in inches in %d\n"
	input1: .asciz "%d"
	num1: .word 0
	
