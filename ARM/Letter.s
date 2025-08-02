#
# Program Name: Letter.s
# Author: 	Logan Griffin
# Date: 	7/16/2024
# Purpose:	Take input and determine if it is a letter or not
#

.text
.global main
main:
	# push the stack
	SUB sp, sp, #4
	STR lr, [sp]

	# prompt for character
	LDR r0, =prompt
	BL printf

	# scan for character
	LDR r0, =format
	LDR r1, =char
	BL scanf

	# load character
	LDR r1, =char
	LDR r1, [r1]

	MOV r2, #0 // all bits are zero
	CMP r1, #0x41
	ADDGE r2, #1 // if true, bit 0 is changed to 1
	
	MOV r3, #0
	CMP r1, #0x5A
	ADDLE r3, #1
	AND r2, r2, r3 // results from first AND, if true r1 is uppercase

	MOV r0, #0
	MOV r3, #0
	CMP r1, #0x61
	ADDGE r3, #1

	MOV r4, #0
	CMP r1, #0x7A
	ADDLE r4, #1
	AND r3, r3, r4 // results form second and, if true r1 is lowercase
	ORR r2, r2, r3 // results from OR, if true r1 is a letter

	CMP r2, #1
		BNE notChar
			LDR r0, =output2
			BL printf
			B EndIf

	notChar:
		LDR r0, =output1
		BL printf
		B EndIf

	EndIf:
	

	# pop the stack
	LDR lr, [sp]
	ADD sp, sp, #4
	MOV pc, lr

.data
	prompt:  .asciz "\nEnter input to be tested if character: "
	output1: .asciz "\nNo, that is not a character.\n"
	output2: .asciz "\nYes, that is a character.\n"
	format:  .asciz "%c"
	char:    .space 1
	

