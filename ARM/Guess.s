#
# Program Name: Guess.s
# Author: 	Logan Griffin
# Date: 	7/23/2024
# Purpose: 	This program chooses a random number between 1 and a max value
#		entered by the user. The user then enters guesses until they
#		identify the random number.
# Note: 	Code for random number generation courtesy of Rand.s function
#		written by Chuck Kann. 

.text
.global main
main:

# Dictionary
# r4 = stores the random value 
# r5 = count for number of guesses

	# push the stack
	SUB sp, sp, #8
	STR lr, [sp, #0]
	STR r4, [sp, #4]
	STR r5, [sp, #8]

	# prompt for input and scan
	LDR r0, =prompt
	BL printf
	LDR r0, =format
	LDR r1, =max
	BL scanf

	MOV r1, #30

	# start loop to test input
	# loop ends with valid input and random number generated
	startLoop:
		LDR r1, =max
		LDR r1, [r1]

		CMP r1, #2
		BLT error
			# generate random number
			# Code from Chuck Kann
			BL rand
			MOV r4, r0 // save the number
			LDR r1, =max
			LDR r1, [r1]
			# modulus operation
			BL __aeabi_idiv
			MUL r0, r0, r1
			SUB r0, r4, r0
			MOV r4, r0	
			B endLoop

		error: 
			LDR r0, =invalid
			BL printf

		# get new value
		LDR r0, =prompt
		BL printf
		LDR r0, =format
		LDR r1, =max
		BL scanf
		B startLoop
	endLoop:

	# have valid input here
	# prompt for guess
	LDR r0, =promptGuess
	BL printf
	LDR r0, =format
	LDR r1, =guess
	BL scanf

	# initialize number of guesses
	MOV r5, #1

	# loop for guessing
	startLoop2:
		LDR r1, =guess
		LDR r1, [r1]
	
		CMP r1, r4 // compare to random number
		BEQ endLoop2
			BLT tooLow
			BGT tooHigh
			B endLoop2

		tooLow:
			LDR r0, =low
			BL printf
			LDR r0, =guesses
			MOV r1, r5 // print number of guesses
			BL printf
			ADD r5, r5, #1
			B newGuess

		tooHigh:
			LDR r0, =high
			BL printf
			LDR r0, =guesses
			MOV r1, r5 // print number of guesses
			BL printf
			ADD r5, r5, #1
			B newGuess

		# get new guess and restart loop
		newGuess:
			LDR r0, =promptGuess
			BL printf
			LDR r0, =format
			LDR r1, =guess
			BL scanf 
			B startLoop2

	endLoop2:

	# guess is correct
	LDR r0, =correct
	BL printf
	LDR r0, =guessesFinal
	MOV r1, r5
	BL printf
		

	# pop the stack
	LDR lr, [sp, #0]
	LDR r4, [sp, #4]
	LDR r5, [sp, #8]
	ADD sp, sp, #8
	MOV pc, lr


.data
	prompt: .asciz "\nEnter a number greater than 1 to serve as the maximum value: "
	promptGuess: .asciz "Enter a guess for the random number: \n"
	format: .asciz "%d"
	max: .word 0
	guess: .word 0
	high: .asciz "\nThat guess is too high. "
	low: .asciz "\nThat guess is too low. "
	correct: .asciz "\nThat is correct. "
	invalid: .asciz "\nThat is not a valid maximum value. "
	guesses: .asciz "That is guess number %d.\n"
	guessesFinal: .asciz "That took %d guesses.\n"
