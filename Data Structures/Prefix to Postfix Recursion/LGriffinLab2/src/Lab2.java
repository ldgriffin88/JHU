package LGriffinLab2.src;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

/*
 * This class reads an input file and converts each line
 * from a prefix expression to an infix and postfix expression, with error checking.
 * 
 * @author - Logan Griffin
 */
public class Lab2 {

   static BufferedReader input = null;
   static BufferedWriter output = null;
   static int next;
   static boolean invalidStatement = false;
   static int nodeCount = 0;
   static int leafCount = 0;

   public static void main(String[] args) {
      // TODO Auto-generated method stub

      // crate initial node
      Node m = new Node(null);

      // check for correct number of command line arguments
      if (args.length != 2) {
         System.out.println("Usage: java Lab2 [input file pathname] "
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

      // test for line
      try {
         next = input.read();
      } catch (IOException e) {
         // TODO Auto-generated catch block
         System.err.println("Cannot read the first character of the file.");
         System.exit(0);
      }

      // keep finding characters until the end of the file is reached
      while (next != -1) {
         // call method to build the expression tree
         m = buildTree((char) next);
         // here all the nodes should be made

         // create/reset counters for nodes and leaves
         // used later to determine if a statement is valid
         nodeCount = 0;
         leafCount = 0;

         // check the statement for an invalid character
         CheckStatement(m);

         // if there is a space, letter, or operator after the
         // expression tree is made, they need to be passed over
         // if there is a letter or operator after, the entire line
         // contains an invalid statement
         try {
            next = input.read();

            while (characterType((char) next) == -1
                  || characterType((char) next) == 0
                  || characterType((char) next) == 1) {

               // setting invalidStatement to true if a letter or operator is found
               if (characterType((char) next) == 0
                     || characterType((char) next) == 1) {
                  invalidStatement = true;
               }

               // getting the next character in the line/file
               next = input.read();
            }

            // loop to skip over the carriage returns and new line characters
            while (characterType((char) next) == -2
                  || characterType((char) next) == -3) {
               next = input.read();
            }

         } catch (IOException e) {
            // TODO Auto-generated catch block
            System.err.println("File could not be read any further.");
            System.exit(0);
         }

         // a statement is invalid if there is not one more leaf than regular node
         if (leafCount - nodeCount != 1) {
            invalidStatement = true;
         }

         // to cover the case where a single operator is on the line
         if (m != null && characterType(m.data.charAt(0)) == 0
               && nodeCount == 0) {
            invalidStatement = true;
         }

         // writing invalid statement to file
         if (invalidStatement && m != null) {

            try {
               output.write("The statement on this line was invalid.");
               output.newLine();
               output.newLine();
            } catch (IOException e) {
               // TODO Auto-generated catch block
               System.err.println("Could not write to output file.");
               System.exit(0);
            }
         }

         // if the statement is valid, write the prefix version of the expression
         // (input),
         // infix version, and the postfix version
         if (!invalidStatement) {

            try {
               output.write("The prefix expression is: ");
               printPre(m);
               output.newLine();
               output.write("The infix expression is: ");
               printIn(m);
               output.newLine();
               output.write("The postfix expression is: ");
               printPost(m);
               output.newLine();
               output.newLine();
            } catch (IOException e) {
               // TODO Auto-generated catch block
               System.err.println("Could not write to output file.");
               System.exit(0);
            }
         } // end if statement

         // reset variable before next expression is evaluated
         invalidStatement = false;
      } // end main while loop

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
      
   } // end main mathod

   /**
    * This method iterates recursively through the expression tree, checking each
    * node for the value to be equal to "Invalid". If found, the method changes the
    * class variable "invalidStatement" to true.
    * 
    * @param n is of type Node
    * 
    * @author - Logan Griffin
    */
   public static void CheckStatement(Node n) {

      // invalid statement if root node is null
      if (n == null) {
         invalidStatement = true;
      } else {

         if (n.data.equals("Invalid")) {
            invalidStatement = true;
         }

         // increment leafCount and nodeCount class variables based on the node having a
         // left and right child
         if (n.left == null && n.right == null) {
            leafCount++;
         } else {
            nodeCount++;
         }

         // if there is a left child, recursively call and evaluate the left child
         if (n.left != null) {
            CheckStatement(n.left);
         }

         // if there is a right child, recursively call and evaluate the right child
         if (n.right != null) {
            CheckStatement(n.right);
         }
      } // end if statement

   } // end CheckStatement method

   /**
    * This method prints the postfix version of the statement by recursively
    * iterating through the expression tree.
    * 
    * @param n is of type Node
    * 
    * @author - Logan Griffin
    */
   public static void printPost(Node n) {

      if (n.left != null) {
         printPost(n.left);
      }

      if (n.right != null) {
         printPost(n.right);
      }

      // block to print the data of the node
      try {
         output.write(n.data);
      } catch (IOException e) {
         // TODO Auto-generated catch block
         System.err.println("Could not print the postfix expression.");
         System.exit(0);
      }
      
   } // end printPost method

   /**
    * This method prints the infix version of the statement by recursively
    * iterating through the expression tree.
    * 
    * @param n is of type Node
    * 
    * @author - Logan Griffin
    */
   public static void printIn(Node n) {

      if (n.left != null) {
         printIn(n.left);
      }

      // block to print the data of the node
      try {
         output.write(n.data);
      } catch (IOException e) {
         // TODO Auto-generated catch block
         e.printStackTrace();
      }

      if (n.right != null) {
         printIn(n.right);
      }
      
   } // end printIn method

   /**
    * This method prints the prefix version of the statement by recursively
    * iterating through the expression tree.
    * 
    * @param n is of type Node
    * 
    * @author - Logan Griffin
    */
   public static void printPre(Node n) {

      // block to print the data of the node
      try {
         output.write(n.data);
      } catch (IOException e) {
         // TODO Auto-generated catch block
         e.printStackTrace();
      }

      if (n.left != null) {
         printPre(n.left);
      }

      if (n.right != null) {
         printPre(n.right);
      }
      
   } // end printPre method

   /**
    * This method builds an tree of nodes to represent the prefix expression from a
    * file. The method checks for invalid characters.
    * 
    * @param c is of type char and represents the next character in the file.
    * 
    * @return a node representing the root of the tree.
    */
   public static Node buildTree(char c) {

      // loop to skip over spaces and tabs
      while (characterType(c) == -1) {

         // read next character if a space or tab
         try {
            c = (char) input.read();
         } catch (IOException e) {
            // TODO Auto-generated catch block
            System.err
                  .println("Could not read character after space or tab.");
            System.exit(0);
         }
      } // end while loop

      // create a new null Node
      Node currentNode = new Node(null);

      // if the character is invalid
      // this is a base case
      if (characterType(c) < -3) {
         currentNode.data = "Invalid";
         return currentNode;
         // if the character is a letter
         // this is a base case
      } else if (characterType(c) == 1) {
         currentNode.data = String.valueOf(c);
         return currentNode;
         // if the character is an operator or a new line
      } else if (characterType(c) == 0 || characterType(c) == -2) {

         // set the node's data
         currentNode.data = String.valueOf(c);

         // recursive calls
         try {

            // get new character
            char next = (char) input.read();

            // if not a new line character, call method again
            // this is going left in the tree
            if (characterType(next) != -2) {
               currentNode.left = buildTree(next);
            }

            // get another character
            if (characterType(next) != -3) {
               next = (char) input.read();
            }

            // if not a new line character, call method again
            // this is going right in the tree
            if (characterType(next) != -2) {
               currentNode.right = buildTree(next);
            } else {
               // if new line character, move to next character
               input.read();
            }

         } catch (IOException e) {
            System.err.println("Could not execute buildTree method.");
            System.exit(0);
         }
      } // end try catch block

      // this will be null if there is a null character at the beginning of the line
      if (currentNode.data == null) {
         return null;
      }

      return currentNode;
      
   } // end buildTree method

   /**
    * This method takes in a character and determines if it is a number, valid
    * operator, carriage return, new line or a space/tab.
    * 
    * @param next is a char
    * @return an integer value corresponding to the type of char
    * 
    * @author Logan Griffin
    */
   public static int characterType(char next) {

      int character = -4;
      int ascii = next;

      // assign character to 0 if an operator
      // assign character to 1 if letter
      // assign character to -1 if space or tab
      // assign character to -2 if new line
      // assign character to -3 if carriage return
      if (ascii == 36 || ascii == 42 || ascii == 43 || ascii == 45
            || ascii == 47) {
         character = 0;
      } else if (64 < ascii && ascii < 91) {
         character = 1;
      } else if (96 < ascii && ascii < 123) {
         character = 1;
      } else if (ascii == 32 || ascii == 9) {
         character = -1;
      } else if (ascii == 10) { // new line character
         character = -2;
      } else if (ascii == 13) {
         character = -3;
      } // end if statement

      return character;
      
   } // end characterType method

} // end Lab2 class
