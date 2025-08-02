package LGriffinLab3.src;

/*
 * This class creates a node with a priority attribute, 
 * and a left and right child.
 * 
 * @auhtor - Logan Griffin
 */
public class Node {

      String data = null;
      int priority;
      Node left;
      Node right;
      
      // constructor
      Node(String data, int priority) {
         this.data = data;
         this.priority = priority;
       
         left = null;
         right = null;
      }
} // end node class
