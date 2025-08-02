package LGriffinLab2.src;

/*
 * This class creates nodes with reference to the left and right child nodes.
 * 
 * @author - Logan Griffin
 */
public class Node {

   String data = null;
   Node left;
   Node right;
   
   // constructor
   Node(String data) {
      this.data = data;
      
      left = null;
      right = null;
   }
   /**
    * This method is used to get the value stored by the left child of a node.
    * 
    * @return a string type
    * 
    * @author - Logan Griffin
    */
   public String getLeft() {
      return left.data;
   }
   
   /**
    * This method is used to get the value stored by the right child of a node.
    * 
    * 
    * @return a string type
    * 
    * @author - Logan Griffin
    */
   public String getRight() {
      return right.data;
   }
} // end Node class
