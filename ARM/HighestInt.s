#
# Program Name: HighestInt.s
# Author: 	Logan Griffin
# Date: 	7/16/2024
# Purpose:	Take in 3 integers and return the highest value
#

.text
.global main
main: 
	# push the stack
	SUB sp, sp, #4
	STR lr, [sp]

	# prompt for first integer
	LDR r0, =prompt1
	BL printf

	# scan for first integer
	LDR r0, =format
	LDR r1, =int1
	BL scanf
	
	# prompt for second integer
	LDR r0, =prompt2
	BL printf
	
	# scan for second integer
	LDR r0, =format
	LDR r1, =int2
	BL scanf
	
	# prompt for third integer
	LDR r0, =prompt3
	BL printf

	# scan for third integer
	LDR r0, =format
	LDR r1, =int3
	BL scanf

	# call function
	LDR r0, =int1
	LDR r0, [r0]
	LDR r1, =int2
	LDR r1, [r1]
	LDR r2, =int3
	LDR r2, [r2]
	BL findMaxOf3

	# print the value
	MOV r1, r0
	LDR r0, =output
	BL printf
	
	# pop the stack
	LDR lr, [sp]
	ADD sp, sp, #4
	MOV pc, lr

.data
	prompt1: .asciz "\nEnter the first of 3 integers: "
	prompt2: .asciz "\nEnter the second of 3 integers: "
	prompt3: .asciz "\nEnter the third of 3 integers: "
	output:  .asciz "\nThe highest integer of the 3 is: %d\n"
	format:  .asciz "%d"
	int1:	 .word 0
	int2:	 .word 0
	int3:	 .word 0

# END Main

.text
findMaxOf3:
	
	# push the stack
	SUB sp, sp, #4
	STR lr, [sp]

	# move first integer to r3
	MOV r3, r0
	
	# move second integer for r4
	MOV r4, r1
	
	# move third integer to r5
	MOV r5, r2

	# compare first value to second value
	CMP r3, r4
	BLT secondGTfirst

	firstGTsecond:
		CMP r3, r5
		BLT firstLTthird
			B firstGTthird

	secondGTfirst:
		CMP r4, r5
		BLT secondLTthird
			B secondGTthird
		
	firstGTthird:
		MOV r0, r3
		B EndIf
	
	firstLTthird:
		MOV r0, r5
		B EndIf
		
	secondGTthird:
		MOV r0, r4
		B EndIf

	secondLTthird:
		MOV r0, r5
		B EndIf

	EndIf:
	

	# pop the stack
	LDR lr, [sp]
	ADD sp, sp, #4
	MOV pc, lr

.data
	
