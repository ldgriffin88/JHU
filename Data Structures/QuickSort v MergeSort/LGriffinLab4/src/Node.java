package LGriffinLab4.src;

/*
 * This class creates nodes for linked lists. 
 * Each node has a data attribute and a pointer
 * to the next node.
 * 
 * @author - Logan Griffin
 */
public class Node {

   Node next;
   int data;
   
   // constructor
   Node() {
      this.data = 0;
      this.next = null;
   }
   
   // constructor with data
   Node(int data) {    
      this.data = data;
      this.next = null;
   }
} // end node class
