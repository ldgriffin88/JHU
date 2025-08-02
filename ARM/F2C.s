.text

.global main
main:

	# save return on os stack
	SUB sp, sp, #4
	STR lr, [sp, #0]

	# prompt for input
	LDR r0, =prompt1
	BL printf
	
	# scan for input
	LDR r0, =input1
	SUB sp, sp, #4
	MOV r1, sp
	BL scanf
	LDR r0, [sp, #0]
	ADD sp, sp, #4

	# convert
	BL F2C
	MOV r1, r0
	
	# print celsius
	LDR r0, =format1
	BL printf
	
	# return to os 
	LDR lr, [sp, #0]
	ADD sp, sp, #4
	MOV pc, lr		

.data

	prompt1: .asciz "Enter the temp in F: \n"
	format1: .asciz "\nThe temp in C is: %d\n"
	input1: .asciz "%d"
	num1: .word 0
