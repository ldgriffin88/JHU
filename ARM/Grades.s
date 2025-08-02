#
# Program Name: Grades.s
# Author: 	Logan Griffin
# Date: 	7/12/2024
# Purpose: 	This program takes a name and average and outputs the grade.
#

.text
.global main
main:
	# push the stack
	SUB sp, sp, #4
	STR lr, [sp]

	# prompt for first name
	LDR r0, =prompt1
	BL printf

	# scan for first name
	LDR r0, =format1
	LDR r1, =firstName
	BL scanf

	# prompt for last name
	LDR r0, =prompt2
	BL printf

	# scan for last name
	LDR r0, =format1
	LDR r1, =lastName
	BL scanf

	# prompt for average grade
	LDR r0, =prompt3
	BL printf

	# scan for grade
	LDR r0, =format2
	LDR r1, =grade
	BL scanf

	# print the name
	LDR r0, =output
	LDR r1, =firstName
	LDR r2, =lastName
	BL printf	
	
	# print grade (grade in r0)
	LDR r0, =grade
	LDR r0, [r0]
	BL printGrades
	
	# pop the stack
	LDR lr, [sp]
	ADD sp, sp, #4
	MOV pc, lr

.data
	prompt1: .asciz "\nEnter a first name: "
	prompt2: .asciz "\nEnter a last name: "
	prompt3: .asciz "\nEnter an average grade: "
	output: .asciz "\n%s %s\'s"
	format1: .asciz "%s"
	format2: .asciz "%d"
	firstName: .space 30
	lastName: .space 30
	grade:   .word  0

# END Main

.text
printGrades:
	SUB sp, sp, #8
	STR lr, [sp]
	STR r4, [sp, #4]
	
	# store r0 in r4 for safety
	MOV r4, r0
	
	# code for function
	MOV r0, #0
	CMP r4, #0
	ADDGE r0, r0, #1 // make true if grade is greater than or equal to zero
	MOV r1, #0
	CMP r4, #100
	ADDLE r1, r1, #1 // make true if grade is less than or equal to 100
	AND r0, r0, r1 // r0 now has value if between 0 and 100.

	CMP r0, #1
	BNE ErrorMsg // branch to error message if grade NOT valid
	# block for if grade IS valid	
	gradeA:
		CMP r4, #90
		BLT gradeB // branch to check for B if less than 90
			# block for if grade is 90-100
			LDR r0, =grade_A
			BL printf
			B EndIf
	gradeB:
		CMP r4, #80
		BLT gradeC
			# block for if grade is 80-90
			LDR r0, =grade_B
			BL printf
			B EndIf
	gradeC: 
		CMP r4, #70
		BLT gradeF
			# block for if grade is 70-80
			LDR r0, =grade_C
			BL printf
			B EndIf
	gradeF:
		# block for if grade is less than 70
		LDR r0, = grade_F
		BL printf
		B EndIf

	
		B gradeA
		B EndIf
	ErrorMsg:
		# print if grade is invalid
		LDR r0, =error
		BL printf
	EndIf:
	
	# pop the stack
	LDR lr, [sp]
	LDR r4, [sp, #4]
	ADD sp, sp, #8
	MOV pc, lr
	

.data		
	error: .asciz " grade must be 0-100.\n"
	grade_A: .asciz " grade is an A.\n"
	grade_B: .asciz " grade is a B.\n"
	grade_C: .asciz " grade is a C.\n"
	grade_F: .asciz " grade is a F.\n"
