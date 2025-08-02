package LGriffinLab4.src;

import java.io.BufferedWriter;
import java.io.IOException;

/*
 * This class builds a linked list. There is a pointer
 * to the head node and to the tail node.
 * 
 * @author - Logan Griffin
 */
public class LinkedList {

   Node head = null;
   Node tail = null;
   int size = 0;

   // constructor
   LinkedList() {
   }

   /**
    * This method inserts a new node into the list.
    * 
    * @param insertedNode is a node passed in
    * 
    * @author - Logan Griffin
    */
   void insert(Node insertedNode) {

      Node temp = new Node();
      temp.data = insertedNode.data;
      
      // if the list is empty, make the new
      // node the head and tail
      if (head == null && tail == null) {
         head = temp;
         tail = temp;
      } else {
         // add to end of list
         tail.next = temp;
         tail = temp;
         tail.next = null;
      }
      
      // increment size
      size = size + 1;
   } // end insert method

   /**
    * This method deletes the head node of a list and
    * reassigns the pointer.
    * 
    * @return the node that was deleted
    */
   Node delete() {

      // store head node
      Node temp = new Node();
      temp = head;
      head = head.next;

      // if tail is being deleted, tail will now be null
      if (temp == tail) {
         tail = null;
      }
      
      // separating node from the list
      temp.next = null;

      // decrement size
      size = size - 1;
      
      return temp;

   } // end delete method
   
   /**
    * This method prints a linked list.
    * 
    * @param n is the head node of the list
    * @param output is a bufferedWriter to write to output file
    */
   void printList(Node n, BufferedWriter output) {
      
      // while there are still nodes to print
      while (n != null && n.next != null) {
         
         // print for file size 50
         try {
            output.write(String.valueOf(n.data) + ", ");
         } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
         }
         
         n = n.next;
      }
      
      // to print the last node in the list
      if (n != null) {
         try {
            output.write(String.valueOf(n.data) + ", ");
         } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
         }
      }

   } // end printList method
} // end LinkedList class
