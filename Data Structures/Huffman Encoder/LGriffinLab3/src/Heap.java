package LGriffinLab3.src;

import java.io.BufferedWriter;
import java.io.IOException;

/*
 * This class creates and populates a min heap using an array. 
 * There are methods to insert/remove nodes, a method to create
 * a Huffman Tree through merging, a method to get the Huffman 
 * code for a letter, a method to print the Huffman codes for 
 * all letters, and a method to get the letter from a specific 
 * Huffman code.
 * 
 * @author - Logan Griffin
 */
public class Heap {

   // to keep track of next index to insert in
   static int nextIndex;
   // array for priority queue
   static Node[] arr;

   /**
    * Method to construct a new heap. Sets index 0 to null
    * 
    * @author - Logan Griffin
    */
   Heap() {

      // create size of the array
      arr = new Node[50];
      arr[0] = null;
      nextIndex = 1;
   }

   /**
    * This method removes the root node of the array by swapping the data for the
    * largest populated index to the root and percolating that node down to its
    * appropriate position.
    * 
    * @return the node that is removed
    * 
    * @author - Logan Griffin
    */
   Node remove() {

      // store root node as temp
      Node temp = arr[1];

      // if the array has a root value
      if (temp != null) {

         // get the data of the largest node that is populated
         Node largestNode = arr[nextIndex - 1];
         // change the data in the index to null
         arr[nextIndex - 1] = null;
         // move largest node to the root so that it can be
         // percolated down to its new position
         arr[1] = largestNode;

         // variable to track current location within method
         int currentLoc = 1;

         // instantiate new nodes
         Node left;
         Node right;

         // testing if the right child is within the bounds of the array
         // sets left and right to null if not in the array
         if (currentLoc * 2 + 1 < arr.length) {

            left = arr[currentLoc * 2];
            right = arr[currentLoc * 2 + 1];
         } else {

            left = null;
            right = null;
         }

         // while at least one child is not null, do comparisons
         // a lower priority value equals a higher priority in the heap
         while (left != null || right != null) {

            // if there is no right child, compare to left child
            if (right == null) {

               // compare to left child
               // if higher priority (lower number) then swap down
               if (arr[currentLoc].priority > left.priority) {

                  // swap current location and left child
                  arr[currentLoc] = left;
                  arr[currentLoc * 2] = largestNode;
                  // set new location to where node was swapped
                  currentLoc = currentLoc * 2;
               } else {
                  // exits loop when no swap needed
                  break;
               }

               // if there is no left child, but there is a right child, compare to right child
            } else if (left == null) {

               // compare to right child.
               // if higher priority (lower number) then swap
               if (arr[currentLoc].priority > right.priority) {

                  arr[currentLoc] = right;
                  arr[currentLoc * 2 + 1] = largestNode;
                  currentLoc = currentLoc * 2 + 1;
               } else {
                  // exits loop when no swap needed
                  break;
               }

               // to handle when there is a left and right child
            } else {

               // if left child is higher priority, then compare current with left child
               if (left.priority < right.priority) {

                  if (arr[currentLoc].priority > left.priority) {

                     // swap current location and left child
                     arr[currentLoc] = left;
                     arr[currentLoc * 2] = largestNode;
                     currentLoc = currentLoc * 2;
                  } else {
                     // exits loop when no swap needed
                     break;
                  }
                  // if right child is higher priority, then compare current with right child
               } else if (right.priority < left.priority) {

                  if (arr[currentLoc].priority > right.priority) {

                     // swap current location and right child
                     arr[currentLoc] = right;
                     arr[currentLoc * 2 + 1] = largestNode;
                     currentLoc = currentLoc * 2 + 1;
                  } else {
                     // exits loop when no swap needed
                     break;
                  }
                  // if the priorities are the same and a swap is needed
                  // priority goes to single letters over complex
                  // and alphanumeric if both complex or both simple
               } else if (right.priority == left.priority
                     && right.priority < arr[currentLoc].priority) {

                  // if both right and left are simple
                  if (left.data.length() == 1 && right.data.length() == 1) {

                     // comparing right and left
                     if (left.data.compareTo(right.data) < 1) {

                        // swap with left child
                        arr[currentLoc] = left;
                        arr[currentLoc * 2] = largestNode;
                        currentLoc = currentLoc * 2;
                     } else {

                        // swap with right child
                        arr[currentLoc] = right;
                        arr[currentLoc * 2 + 1] = largestNode;
                        currentLoc = currentLoc * 2 + 1;
                     }
                     // if the left is simple and right is complex
                  } else if (left.data.length() == 1
                        && right.data.length() > 1) {

                     // swap with left child
                     arr[currentLoc] = left;
                     arr[currentLoc * 2] = largestNode;
                     currentLoc = currentLoc * 2;
                     // if the left is complex and the right is simple
                  } else if (left.data.length() > 1
                        && right.data.length() == 1) {

                     // swap with right child
                     arr[currentLoc] = right;
                     arr[currentLoc * 2 + 1] = largestNode;
                     currentLoc = currentLoc * 2 + 1;
                     // when both left and right are complex
                  } else {

                     // to track minimum alphanumeric values
                     char leftMin = left.data.charAt(0);
                     char rightMin = right.data.charAt(0);

                     // loop through left data
                     for (int i = 1; i < left.data.length(); i++) {

                        if (left.data.charAt(i) < leftMin) {
                           leftMin = left.data.charAt(i);
                        }
                     }

                     // loop through right data
                     for (int j = 1; j < right.data.length(); j++) {

                        if (right.data.charAt(j) < rightMin) {
                           rightMin = right.data.charAt(j);
                        }
                     }

                     // comparing minimum values
                     if (leftMin < rightMin) {

                        // swap with left child
                        arr[currentLoc] = left;
                        arr[currentLoc * 2] = largestNode;
                        currentLoc = currentLoc * 2;
                     } else {

                        // swap with right child
                        arr[currentLoc] = right;
                        arr[currentLoc * 2 + 1] = largestNode;
                        currentLoc = currentLoc * 2 + 1;
                     }
                  } // end of testing two complex data with same priority
               } // end of testing same priority
            } // end of testing when there are two children

            // test prior to setting new left and right
            if (currentLoc * 2 + 1 < arr.length) {

               left = arr[currentLoc * 2];
               right = arr[currentLoc * 2 + 1];
            } else {
               left = null;
               right = null;
            }
         } // end while loop
           // decrease counter for next available spot
         nextIndex = nextIndex - 1;
      } else {

         System.err.println("There was no node to remove.");
         System.exit(0);
      }

      return temp;
   } // end remove method

   /**
    * This method inserts a node into the next available index in the array. The
    * inserted node is compared with its parent node until the parent node is less
    * than the inserted node.
    * 
    * @param n is of type Node
    * 
    * @author - Logan Griffin
    */
   void insert(Node n) {

      // insert node at next available space
      arr[nextIndex] = n;

      int location = nextIndex;

      // get parent node if there is a parent
      if (nextIndex > 1) {

         Node parent = arr[nextIndex / 2];

         // while the inserted node's priority is higher (lower value) than its parent
         while (parent != null && n.priority <= parent.priority) {

            if (n.priority < parent.priority) {

               // swap with parent
               arr[location / 2] = n;
               arr[location] = parent;
               location = location / 2;
               parent = arr[location / 2];
               // if the priority is the same as parent, then need to compare data
            } else if (n.priority == parent.priority) {

               // if both are simple, compare alphanumeric
               if (n.data.length() == 1 && parent.data.length() == 1) {

                  if (n.data.compareTo(parent.data) < 0) {

                     // swap with parent
                     arr[location / 2] = n;
                     arr[location] = parent;
                     location = location / 2;
                     parent = arr[location / 2];
                  } else {
                     // exits loop when no swap needed
                     break;
                  }
                  // if inserted or parent is complex
               } else if (n.data.length() > 1 || parent.data.length() > 1) {

                  // if inserted is simple but parent is complex
                  if (n.data.length() == 1 && parent.data.length() > 1) {
                     // swap with parent
                     arr[location / 2] = n;
                     arr[location] = parent;
                     location = location / 2;
                     parent = arr[location / 2];
                     // if both are complex
                  } else if (n.data.length() > 1
                        && parent.data.length() > 1) {

                     // to track minimum alphanumeric values
                     char nMin = n.data.charAt(0);
                     char parentMin = parent.data.charAt(0);

                     // loop through inserted
                     for (int i = 1; i < n.data.length(); i++) {

                        if (n.data.charAt(i) < nMin) {
                           nMin = n.data.charAt(i);
                        }
                     }

                     // loop through parent
                     for (int j = 1; j < parent.data.length(); j++) {

                        if (parent.data.charAt(j) < parentMin) {
                           parentMin = parent.data.charAt(j);
                        }
                     }

                     // compare minimum values
                     if (nMin < parentMin) {

                        // swap with parent
                        arr[location / 2] = n;
                        arr[location] = parent;
                        location = location / 2;
                        parent = arr[location / 2];
                     }
                  } else {
                     // exits loop when no swap needed
                     break;
                  }
               }
            } // end testing if inserted and parent are same priority
         } // end testing if inserted s higher priority than parent
      } // end testing if parent exists

      // increment next index
      nextIndex++;
   } // end insert method

   /**
    * This method removes the root node from the tree twice, combines the two data
    * and priority of the two nodes, then inserts the new node back into the array.
    * 
    * @author - Logan Griffin
    */
   void merge() {

      Node one = remove();
      Node two = remove();

      // sum priorities
      int mergedPriority = one.priority + two.priority;
      // concatenate data
      String mergedData = one.data + two.data;

      StringBuilder alpha = new StringBuilder(mergedData);

      // insertion sort algorithm to put data in abc order
      for (int i = 1; i < alpha.length(); i++) {

         int j = i;

         while (j > 0 && alpha.charAt(j) < alpha.charAt(j - 1)) {
            // swap characters
            char temp = alpha.charAt(j);
            alpha.setCharAt(j, alpha.charAt(j - 1));
            alpha.setCharAt(j - 1, temp);
            --j;
         }
      } // end insertion sort

      // create new node
      Node mergedNode = new Node(alpha.toString(), mergedPriority);
      // set left and right of new node
      mergedNode.left = one;
      mergedNode.right = two;

//      System.out.println();
//      System.out.println("Merging " + one.data + " and " + two.data);
//      System.out.println("Left priority is: " + one.priority);
//      System.out.println("Right priority is: " + two.priority);
//      System.out.println("New data is: " + mergedData);
//      System.out.println("New priority is: " + mergedPriority);

      // insert node back into array
      insert(mergedNode);
   } // end merge method

   /**
    * This method prints the array in order for testing.
    * 
    * @author - Logan Griffin
    */
   void printArray() {

      // loop through array and print to console
      for (int i = 1; i < nextIndex; i++) {

         System.out.print(arr[i].data + ", ");
      }
      System.out.println();
   } // end print method

   /**
    * This method recursively prints the codes for the letters in Huffman Tree.
    * 
    * @param top  is the root node of the tree
    * @param code is the code for the letter
    * @param bw   is a bufferedwriter from main class
    * 
    * @author - Logan Griffin
    */
   void printCodes(Node top, String code, BufferedWriter bw) {

      // if the data in the node is complex, need to call again to find leaf
      if (top.data.length() > 1) {

         // calling again and adding o to code if going left
         printCodes(top.left, code + "0", bw);
         // calling again and addign 1 to code if going right
         printCodes(top.right, code + "1", bw);

         return;
      }

      try {
         // write letter and code to output file when leaf is found
         bw.write(top.data + " = " + code);
         bw.newLine();
      } catch (IOException e) {
         // TODO Auto-generated catch block
         System.err.println("Could not write codes to output file.");
         System.exit(0);
      }

      return;
   } // end printCodes method

   /**
    * This method prints the Huffman tree in preorder form.
    * 
    * @param root   is the root node of the tree
    * @param head   is the root node of the tree
    * @param writer is a bufferedwriter passed from main
    * 
    * @author - Logan Griffin
    */
   void printTree(Node root, Node head, BufferedWriter writer) {

      // if there is no root
      if (root == null) {

         return;
      }

      try {

         // for the first print, dont print a comma
         if (root.data.equals(head.data)) {

            writer.write(root.data + ": " + root.priority);
         } else {

            writer.write(", " + root.data + ": " + root.priority);
         }

      } catch (IOException e) {
         // TODO Auto-generated catch block
         System.err.println("Cannot print the Huffman tree.");
         System.exit(0);
      }

      // recursive calls to traverse tree
      printTree(root.left, head, writer);
      printTree(root.right, head, writer);

   } // end printTree method

   /**
    * This method finds the letter code for the letter that is passed in.
    * 
    * @param top    is the root node of the tree
    * @param code   is the code string
    * @param letter is the letter the code is needed for
    * @param helper is a bufferedwriter passed from main
    * 
    * @author - Logan Griffin
    */
   void getLetterCode(Node top, String code, String letter,
         BufferedWriter helper) {

      // if its a complex code, keep going to find a leaf
      if (top.data.length() > 1) {
         getLetterCode(top.left, code + "0", letter, helper);
         getLetterCode(top.right, code + "1", letter, helper);
         return;

         // if the leaf matches the letter
      } else if (!top.data.equalsIgnoreCase(letter)) {
         return;
      }

      // write the code to the output file
      try {
         helper.write(code);
      } catch (IOException e) {
         // TODO Auto-generated catch block
         System.err.println(
               "Could not write the letter code to the output file.");
         System.exit(0);
      }

      return;
   } // end getLetterCode method

   /**
    * This method finds the node associated with a specific code. If the node is a
    * simple letter, the letter is written to the output file.
    * 
    * @param top           is the root node
    * @param codetoCompare is the code the method will find the corresponding node
    *                      for
    * @param author        is a bufferedwriter passed from main
    * @return is a boolean telling if the letter was matched and written to output
    * 
    * @author - Logan Griffin
    */
   boolean getletter(Node top, String codetoCompare, BufferedWriter author) {

      boolean match = false;

      // to navigate to the node that matches the code passed
      for (int k = 0; k < codetoCompare.length(); k++) {

         // if next character is a 0
         if (codetoCompare.charAt(k) == 48) {
            top = top.left;

            // if next character is a 1
         } else if (codetoCompare.charAt(k) == 49) {
            top = top.right;
         }
      }
      // to check if the node arrived at is a leaf
      if (top.left == null && top.right == null) {

         try {
            author.write(top.data);
         } catch (IOException e) {
            // TODO Auto-generated catch block
            System.err.println("Could not write letter to output file.");
            System.exit(0);
         }
         match = true;
      }

      return match;
   } // end getLetter method

} // end Heap class
