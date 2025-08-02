package LGriffinLab1.src;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

/*
 * This class reads an input file and converts each line
 * from a prefix expression to a postfix expression, with error checking.
 * 
 * @author Logan Griffin
 */
public class Lab1 {

   /**
    * This method takes in a character and determines if it is a number, valid
    * operator, or a space.
    * 
    * @param next is a char
    * @return an integer value corresponding to the type of char
    * 
    * @author Logan Griffin
    */
   public static int CharacterType(char next) {

      int character = -2;
      int ascii = next;

      // assign character to 0 if an operator, 1 if letter
      if (ascii == 36 || ascii == 42 || ascii == 43 || ascii == 45
            || ascii == 47) {
         character = 0;
      } else if (64 < ascii && ascii < 91) {
         character = 1;
      } else if (96 < ascii && ascii < 123) {
         character = 1;
      } else if (ascii == 32) {
         character = -1;
      }
      return character;
   } // end characterType method

   /**
    * Start of the main method
    * 
    * @param args are taken from the command line and used as the input and output
    * files.
    * 
    * @author Logan Griffin
    */
   public static void main(String[] args) {
      // TODO Auto-generated method stub

      BufferedReader input = null;
      BufferedWriter output = null;

      // check for correct number of command line arguments
      if (args.length != 2) {
         System.out.println("Usage: java Lab1 [input file pathname] "
               + "[output file pathname]");
         System.exit(0);
      }

      // open files for input and output
      try {
         input = new BufferedReader(new FileReader(args[0]));
         output = new BufferedWriter(new FileWriter(args[1]));
      } catch (Exception ioe) {
         System.err
               .println("Either the input or output file cannot be found.");
         System.exit(0);
      }

      // create string to write to
      String prefixLine = null;

      // read each line
      try {

         // initialize the prefix line
         prefixLine = input.readLine();
         // loop while the next line is not blank
         while (prefixLine != null && prefixLine.isBlank() != true) {
            // call the stack class constructor and make it the
            // length of the line. The stack will never need to be
            // longer than that. This keeps from creating an unnecessarily
            // large stack array
            Stack prefix = new Stack(prefixLine.length());

            // boolean to track if the expression is valid
            boolean containsInvalid = false;

            // loop to put the characters from the string into the stack
            int i = 0;
            while (i < prefixLine.length()) {

               // check type of character to eliminate blank spaces
               int type = CharacterType(prefixLine.charAt(i));

               // if there is a letter or operator, push it to the stack
               if (type >= 0) {
                  prefix.push(String.valueOf(prefixLine.charAt(i)));
               } else if (type == -1) {
                  // ignore spaces
               } else {
                  // change boolean and exit the loop to save time
                  containsInvalid = true;
                  break;
               } // end if statement
               i++;
            } // end while loop

            // create a stack to track the expression
            Stack exp = new Stack(prefixLine.length());

            // keep counts to track operators and operands
            // if the difference is more than 1, the expression
            // is invalid
            int operatorCount = 0;
            int operandCount = 0;

            // loop while there are still characters to assess and the line
            // has not already been ruled out as invalid
            while (prefix.isEmpty() == false && containsInvalid == false) {

               // get the last term from the line
               String term = prefix.pop();

               if (CharacterType(term.charAt(0)) == 1) {
                  // if character is a letter
                  operandCount++;
                  // push the letter onto the expression stack
                  exp.push(term);
               } else if (CharacterType(term.charAt(0)) == 0) {
                  // if character is an operator
                  operatorCount++;
                  // pop the expression stack twice and then push the
                  // combined terms and the operator back to the exp stack
                  String first = exp.pop();
                  String second = exp.pop();
                  
                  if (first == null || second == null) {
                     containsInvalid = true;
                     break;
                  } 
                    
                  exp.push(first + second + term);
               } // end if statement
            } // end while loop
            
            // what happens if you hit an operator on the first or second time

            // if the expression is invalid, clear the stack and push a
            // message saying that line was invalid.
            if (operandCount - operatorCount != 1
                  || containsInvalid == true || operatorCount == 0 || operandCount == 0) {
               while (exp.isEmpty() == false) {
                  exp.pop();
               }
               exp.push("The expression on this line was invalid.");
            } // end if statement

            // writing to the output file
            try {
               output.write(exp.pop());
               output.newLine();
            } catch (IOException iox) {
               System.err.println("Expression stack is empty");
               System.exit(0);
            }

            // set the new line to the next line of the file
            prefixLine = input.readLine();
         } // end while loop

         // if next line cannot be read or another issue with the file
      } catch (IOException e) {
         // TODO Auto-generated catch block
         System.err.println("There was an error reading the line.");
      }

      // close the input/output readers/writers
      try {
         input.close();
      } catch (IOException e) {
         // TODO Auto-generated catch block
         System.err.println("Input could not be closed.");
      }
      try {
         output.close();
      } catch (IOException e) {
         // TODO Auto-generated catch block
         System.err.println("Output could not be closed.");
      } // end try/catch block to close
   } // end main method
} // end class
