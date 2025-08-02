package LGriffinLab3.src;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

/*
 * This class takes in 3 files:
 * 1) frequency table
 * 2) clear text to encode
 * 3) encoded text to decode
 * 
 * and writes to an output file. The output file will show the printed 
 * Huffman Tree built from the heap class based on the frequency table,
 * the Huffman code for each letter in the frequency table, the encoded 
 * version of the clear text, and the decoded version of the encoded text.
 * 
 * @author - Logan Griffin
 */
public class Lab3 {

   static BufferedReader input = null;
   static BufferedReader inputClear = null;
   static BufferedReader inputEncode = null;
   static BufferedWriter output = null;
   static String next = null;
   static String nextClear = null;
   static String nextEncode = null;

   public static void main(String[] args) {
      // TODO Auto-generated method stub

      // check for correct number of command line arguments
      if (args.length != 4) {
         System.out.println("Usage: java Lab3 [Frequency table pathname] "
               + "[File to encode pathname] " + "[File to decode pathname] "
		+ "[File to output pathname]");
         System.exit(0);
      }

      // open files for input and output
      // first input file should be frequency table
      // second input file should be clear text to encode
      // third input file should be coded text to decode
      try {
         input = new BufferedReader(new FileReader(args[0]));
         inputClear = new BufferedReader(new FileReader(args[1]));
         inputEncode = new BufferedReader(new FileReader(args[2]));
         output = new BufferedWriter(new FileWriter(args[3]));
      } catch (Exception ioe) {
         System.err.println("One of the files cannot be found.");
         System.exit(0);
      }

      try {
         next = input.readLine();
      } catch (IOException e) {
         // TODO Auto-generated catch block
         System.err
               .println("Cannot read the first line of freqeuncy table.");
         System.exit(0);
      }

      // create new heap
      Heap heapy = new Heap();

      // to track length of frequency table
      int numLetters = 0;

      // loop through frequency table
      while (next != null) {

         String letter = String.valueOf(next.charAt(0));
         String freq = "";

         // assign the letter and frequency
         for (int k = 4; k < next.length(); k++) {

            freq = freq + String.valueOf(next.charAt(k));
         }

         // create new node
         Node newLetter = new Node(letter, Integer.valueOf(freq));

         // insert node into heap array
         heapy.insert(newLetter);

         numLetters = numLetters + 1;

         try {
            next = input.readLine();
         } catch (IOException e) {
            // TODO Auto-generated catch block
            System.err
                  .println("Could not read next line of frequency table.");
            System.exit(0);
         }
      } // end while loop

      // to make the Huffman tree
      for (int merges = 0; merges < numLetters - 1; merges++) {

         heapy.merge();
      }

      Node root = Heap.arr[1];
      String startCode = "";

      // to print the tree in preorder form
      try {
         output.write(
               "--------------------------------------------------\n");
         output.write("PRINTING HUFFMAN TREE \n");
         output.write(
               "--------------------------------------------------\n\n");
         output.write("The Huffman Tree is: \n");

         heapy.printTree(root, root, output);

         output.newLine();
         output.newLine();
      } catch (IOException e) {
         // TODO Auto-generated catch block
         System.err.println("Could not print the Huffman Tree.");
         System.exit(0);
      }

      // to print out the codes for each letter
      try {
         output.write(
               "--------------------------------------------------\n");
         output.write("PRINTING LETTER CODES \n");
         output.write(
               "--------------------------------------------------\n\n");
         output.write("The codes for each letter are: ");
         output.newLine();

         heapy.printCodes(root, startCode, output);

         output.newLine();
      } catch (IOException e) {
         // TODO Auto-generated catch block
         System.err.println("Could not print the codes for each letter.");
         System.exit(0);
      }

      // to encode the clear text file
      try {
         nextClear = inputClear.readLine();
         output.write(
               "--------------------------------------------------\n");
         output.write("ENCODING SECTION \n");
         output.write(
               "--------------------------------------------------\n\n");
      } catch (IOException e) {
         // TODO Auto-generated catch block
         System.err.println(
               "Could not write to file or read the clear text file.");
         System.exit(0);
      }

      // to read all the lines in the clear text file
      while (nextClear != null) {

         try {
            output.write("The text to encode is: \n");
            output.write(nextClear + "\n\n");
            output.write("The encoded text is: \n");
         } catch (IOException e) {
            // TODO Auto-generated catch block
            System.err.println("Could not write encoded text to file.");
            System.exit(0);
         }

         // loop through the line in the input file and get letter code
         for (int len = 0; len < nextClear.length(); len++) {

            heapy.getLetterCode(root, startCode,
                  String.valueOf(nextClear.charAt(len)), output);
         }

         try {
            output.newLine();
            output.newLine();
            output.newLine();
            nextClear = inputClear.readLine();
         } catch (IOException e) {
            // TODO Auto-generated catch block
            System.err.println("Could not write read clear text file.");
            System.exit(0);
         }
      } // end while loop

      // to decode the encoded text form the input file
      try {
         nextEncode = inputEncode.readLine();
         output.write(
               "--------------------------------------------------\n");
         output.write("ENCODING SECTION \n");
         output.write(
               "--------------------------------------------------\n\n");
      } catch (IOException e) {
         // TODO Auto-generated catch block
         System.err.println("Could not read from encoded file.");
         System.exit(0);
      }

      // loop through lines from encoded file
      while (nextEncode != null) {

         String toDecode = "";

         try {
            output.write("The text to decode is: \n");
            output.write(nextEncode + "\n\n");
            output.write("The decoded text is: \n");

            // add first number to code
            toDecode = toDecode + nextEncode.charAt(0);

            // loop through the entire code
            // reset string to be evaluated by getLetter method when
            // method returns true
            for (int v = 1; v <= nextEncode.length(); v++) {

               boolean check = heapy.getletter(root, toDecode, output);

               if (check) {

                  // reset string
                  toDecode = "";
                  if (v == nextEncode.length()) {
                     break;
                  }
                  toDecode = toDecode + nextEncode.charAt(v);
               } else {

                  // add next character to string
                  if (v == nextEncode.length()) {
                     break;
                  }

                  toDecode = toDecode + nextEncode.charAt(v);
               }
            } // end for loop

         } catch (IOException e) {
            // TODO Auto-generated catch block
            System.err.println("Could not decode text.");
            System.exit(0);
         }

         try {
            output.newLine();
            output.newLine();
            output.newLine();
            nextEncode = inputEncode.readLine();

         } catch (IOException e) {
            // TODO Auto-generated catch block
            System.err.println("Could not write decoded text to file.");
            System.exit(0);
         }
      } // end while loop

      try {
         output.close();
         input.close();
      } catch (IOException e) {
         // TODO Auto-generated catch block
         System.err.println("Could not close reader or writer.");
         System.exit(0);
      }

   } // end main method
} // end Lab3 class
