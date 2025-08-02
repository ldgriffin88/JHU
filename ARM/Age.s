.text
.global main
main:

	# push the stack
	SUB sp, sp, #4
	STR lr, [sp, #0]

	# print a prompt
	LDR r0, =prompt1
	BL printf

	# read in the age
	LDR r0, =format1
	LDR r1, =age1
	BL scanf

	# print the output string
	LDR r0, =output1
	LDR r1, =age1
	LDR r1, [r1, #0]
	BL printf

	# print formatted string	
	LDR r0, =output2
	BL printf

	# pop the stack
	LDR lr, [sp, #0]
	ADD sp, sp, #4
	MOV pc, lr

.data
	prompt1: .asciz "What is your age? "
	output1: .asciz "Your age is: \t%d\t\n"
	output2: .asciz "Quotes in \"formatted\" string.\n"
	format1: .asciz "%d"
	age1:    .word  0
