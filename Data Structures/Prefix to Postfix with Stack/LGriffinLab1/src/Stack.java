package LGriffinLab1.src;
/*
 * This class uses arrays to implement a stack.
 * There are methods to push, pop, peek, and check
 * to see if the stack/array is empty.
 * 
 * @author Logan Griffin
 */

public class Stack {
   
   private int length;
   private String[] chars;
   private int top = -1;
   
   Stack (int newlength) {
     length = newlength;
     chars = new String[length];
   }
   
/** 
 * This method pushes an item on the stack by adding it to 
 * the next array position.
 * 
 * @param newitemtoPush is a string type
 * 
 * @author Logan Griffin
 */
    public void push(String newitemtoPush) {
      
      String itemtoPush = newitemtoPush;
      
      // if the top of the stack is in bounds
      if (top < length - 1) {
         // assign the next spot in the array with the string
         chars[top + 1] = itemtoPush;
         top = top + 1;
      } else {
         // print that the stack is full
         System.out.println("Stack is full.");
      } // end if statement
   } // end push method
    
/**
 * This method pops an item from the stack by removing it 
 * from the array.
 * 
 * @return the item that was removed as a string
 * 
 * @author Logan Griffin
 */
   public String pop() {
      
      String itemtoPop = null;
      
      // if there is an item to remove
      if (top > -1) {
         // set the item to return
         itemtoPop = chars[top];
         // change index to null
         chars[top] = null;
         top = top - 1;
      } // end if statement
           
      return itemtoPop;
   } // end pop method
   
/**
 * This method tells whether the stack is empty or not.
 * 
 * @return a boolean true if empty and false if not
 * 
 * @author Logan Griffin
 */
   public boolean isEmpty() {
      
      boolean empty;
      
      if (top > -1) {
         empty = false;
      } else {
         empty = true;
      }
        
      return empty;
   } // end isEmpty method
   
   
/**
 * This method looks at the top of the stack and return the value.
 * 
 * @return a string containing the item at the top of the stack
 * 
 * @author Logan Griffin
 */
   public String peek() {
      String topofStack = null;
      
      if (top > -1) {
         topofStack = chars[top];
      }
      
      return topofStack;
   } // end peek method
     
/**
 * This method prints each index on the stack out on a
 * separate line. Mostly used for testing purposes.
 */
   public void printStack() {
      for (int i = 0; i<length; i++) {
         System.out.println(chars[i]);
      }
      System.out.println();
   } // end printStack method
     
} // end class
