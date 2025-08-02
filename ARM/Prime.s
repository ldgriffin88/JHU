#
# Program Name: Prime.s
# Author: 	Logan Griffin
# Date: 	7/23/2024
# Purpose:  	Take an integer input and output if the number is prime.
#

.text
.global main
main: 

# Dictionary
# r4 = input value
# r5 = input value divided by 2
# r6 = subtraction test number
# r7 = remainder from subtraction test

	# push the stack
	SUB sp, sp, #16
	STR lr, [sp, #0]
	STR r4, [sp, #4]
	STR r5, [sp, #8]
	STR r6, [sp, #12]
	STR r7, [sp, #16]
	STR r8, [sp, #17]

	# prompt user for number, say enter -1 to end the problem
	LDR r0, =prompt
	BL printf
	LDR r0, =format
	LDR r1, =num
	BL scanf

	# start sentinel loop
	startLoop:
		LDR r1, =num
		LDR r1, [r1]
	
		# compare to -1
		# if not -1 go onto other cmp	
		CMP r1, #-1
		BEQ endLoop

		# statement or block to execute
		# compare to 3 again and if less than print out error
		CMP r1, #3
		BLT error
			B endError // jump over error if all comparisons failed

		error:
			LDR r0, =error1
			BL printf
			
			# get a new value
			LDR r0, =prompt
			BL printf
			LDR r0, =format
			LDR r1, =num
			BL scanf
			B startLoop
				
		endError:	
		
		# have valid input here
		# establish number to count to
		MOV r4, r1 // move input value
		MOV r7, r1 // move input value for subtraction
		MOV r0, r1 // move input value for division
		MOV r1, #2 
		BL __aeabi_idiv
		MOV r5, r0 // move input value/2 into r5

	
		# first test number
		MOV r6, #2
		
		# start loop to test if number is divisible by test num
		startLoop2:

			CMP r5, r6
			# if r5 is less than r6, all numbers have been checked and number is prime
			BLT prime // number is prime. go here first to print then end loop
				startLoop3:	
					CMP r7, r6 // comparing remaining value
					BLT endLoop3
						# if more subtraction is needed
						SUB r7, r7, r6
						B startLoop3
				endLoop3:

			# now have remainder from loop 3 in r7
			CMP r7, #0
			BEQ notPrime
				# if remainder is not 0
				ADD r6, r6, #1 // increment the subtraction value
				MOV r7, r4 // reset the input value
				B startLoop2

			notPrime:
				LDR r0, =numNotPrime
				LDR r1, =num
				LDR r1, [r1]
				BL printf
				B endLoop2

			prime: 
				LDR r0, =numPrime
				LDR r1, =num
				LDR r1, [r1]
				BL printf
						
		endLoop2:


		# get next value
		LDR r0, =prompt
		BL printf
		LDR r0, =format
		LDR r1, =num
		BL scanf
		B startLoop

	endLoop:


	# pop the stack
	LDR lr, [sp, #0]
	LDR r4, [sp, #4]
	LDR r5, [sp, #8]
	LDR r6, [sp, #12]
	LDR r7, [sp, #16]
	ADD sp, sp, #16
	MOV pc, lr

.data
	prompt: .asciz "\nEnter a positive number higher than 2. Enter -1 to quit: \n"
	format: .asciz "%d"
	num: 	.word 0
	error1: .asciz "\nNumber entered cannot be 0, 1, 2, or less than -1.\n"
	numNotPrime: .asciz "\nNumber %d is not prime.\n"
	numPrime: .asciz "\nNumber %d is prime.\n"

