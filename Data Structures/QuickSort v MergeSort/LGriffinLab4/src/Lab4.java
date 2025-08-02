package LGriffinLab4.src;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;
import java.io.BufferedWriter;

/*
 * This class reads in files of integers from a folder and performs 4 different 
 * quick sort variations and a natural merge sort on the data. The way the sorts 
 * are completed is printed to an output file for the smallest file size, which 
 * is 50 integers. Another output file is used to store the number of comparisons
 * and swaps that occur during each sort.
 * 
 * @author - Logan Griffin
 */
public class Lab4 {

   static BufferedWriter output = null;
   static BufferedWriter stats = null;
   static int numComps = 0;
   static int numSwaps = 0;

   public static void main(String[] args) throws FileNotFoundException {
      // TODO Auto-generated method stub

      // open files for output
      try {
         output = new BufferedWriter(new FileWriter(args[1]));
         stats = new BufferedWriter(new FileWriter(args[2]));
      } catch (IOException e) {
         // TODO Auto-generated catch block
         e.printStackTrace();
      }

      // read in the folder of files
      File folder = new File(args[0]);
      
      // go thorugh each file
      for (File fdsa : folder.listFiles()) {

         Scanner input = new Scanner(fdsa);
         // separate scanner for merge sort so the file can be read again
         Scanner input2 = new Scanner(fdsa);

         // get file name
         fdsa.getName();

         // read the file name starting at character in index 3
         int startChar = 3;
         int length = 0;

         // while loop to get the length of the file so data structure size can be chosen
         while (fdsa.getName().charAt(startChar) != '.') {

            int ascii = fdsa.getName().charAt(startChar) - 48;
            // for every zero in the file name, multiply length by 10
            if (ascii == 0) {
               length = length * 10;
            } else {
               // set length if number read is not a zero
               length = ascii;
            }

            startChar++;
         } // end loop to get length
         
         // print to output file
         if (length == 50) {
            try {
               output.write(
                     "\n\n-----------------------------------------------"
                     + "--------------------------------------------------"
                     + "------------\n");
               output.write(
                     "Starting QuickSort variant 1 on: " + fdsa.getName());
               output.write(
                     "\n------------------------------------------------"
                     + "-------------------------------------------------"
                     + "------------\n");
            } catch (IOException e) {
               // TODO Auto-generated catch block
               e.printStackTrace();
            }
         }
         
         // read the data into an array and
         // copy it for the other quick sorts
         int[] data = setUpQuicksort(input, length);
         int[] data2 = data.clone();
         int[] data3 = data.clone();
         int[] data4 = data.clone();

         // run quicksort variant 1
         quickSort(data, 0, data.length - 1, 1, length, output);

         // output the comparisons and swaps to the stats file
         try {
            stats.write(fdsa.getName() + ", Quicksort Variant 1, " + length
                  + ", " + numComps + ", " + numSwaps);
            stats.newLine();
         } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
         }

         // reset counters
         numComps = 0;
         numSwaps = 0;

         // print to output file
         if (length == 50) {
            try {
               output.write(
                     "\n\n----------------------------------------------"
                     + "-------------------------------------------------"
                     + "--------------\n");
               output.write(
                     "Starting QuickSort variant 2 on: " + fdsa.getName());
               output.write(
                     "\n------------------------------------------------"
                     + "------------------------------------------------"
                     + "-------------\n");
            } catch (IOException e) {
               // TODO Auto-generated catch block
               e.printStackTrace();
            }
         }
         
         // quick sort variant 2
         quickSort(data2, 0, data2.length - 1, 2, length, output);

         // output comparisons and swaps to output file
         try {
            stats.write(fdsa.getName() + ", Quicksort Variant 2, " + length
                  + ", " + numComps + ", " + numSwaps);
            stats.newLine();
         } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
         }
         
         // reset counters
         numComps = 0;
         numSwaps = 0;

         // print to output file
         if (length == 50) {
            try {
               output.write(
                     "\n\n-----------------------------------------------"
                     + "--------------------------------------------------"
                     + "------------\n");
               output.write(
                     "Starting QuickSort variant 3 on: " + fdsa.getName());
               output.write(
                     "\n-------------------------------------------------"
                     + "---------------------------------------------------"
                     + "---------\n");
            } catch (IOException e) {
               // TODO Auto-generated catch block
               e.printStackTrace();
            }
         }
         
         // quick sort variant 3
         quickSort(data3, 0, data3.length - 1, 3, length, output);

         // output comparisons and swaps to output file
         try {
            stats.write(fdsa.getName() + ", Quicksort Variant 3, " + length
                  + ", " + numComps + ", " + numSwaps);
            stats.newLine();
         } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
         }

         // reset counters
         numComps = 0;
         numSwaps = 0;

         // print to output file
         if (length == 50) {
            try {
               output.write(
                     "\n\n----------------------------------------------"
                     + "--------------------------------------------------"
                     + "-------------\n");
               output.write(
                     "Starting QuickSort variant 4 on: " + fdsa.getName());
               output.write(
                     "\n------------------------------------------------"
                     + "--------------------------------------------------"
                     + "-----------\n");
            } catch (IOException e) {
               // TODO Auto-generated catch block
               e.printStackTrace();
            }
         }
         
         // quick sort variant 4
         quickSort(data4, 0, data4.length - 1, 4, length, output);

         // output comparisons and swaps to stats file
         try {
            stats.write(fdsa.getName() + ", Quicksort Variant 4, " + length
                  + ", " + numComps + ", " + numSwaps);
            stats.newLine();
         } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
         }

         // reset counters
         numComps = 0;
         numSwaps = 0;

         // print to output file
         if (length == 50) {
            try {
               output.write(
                     "\n\n-----------------------------------------------"
                     + "--------------------------------------------------"
                     + "------------\n");
               output.write("Starting MergeSort on: " + fdsa.getName());
               output.write(
                     "\n-------------------------------------------------"
                     + "--------------------------------------------------"
                     + "----------\n");
            } catch (IOException e) {
               // TODO Auto-generated catch block
               e.printStackTrace();
            }
         }
         
         // run merge sort using separate scanner
         LinkedList[] dataMerge = setUpMerge(input2, length, output);
         merge(dataMerge, length, output);

         // print comparisons and swaps to stats file
         try {
            stats.write(fdsa.getName() + ", MergeSort, " + length + ", "
                  + numComps + ", " + numSwaps);
            stats.newLine();
         } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
         }

         // reset counters
         numComps = 0;
         numSwaps = 0;
      }

      // close both buffered readers and file writers
      try {
         output.close();
         stats.close();
      } catch (IOException e) {
         // TODO Auto-generated catch block
         e.printStackTrace();
      }
   } // end main
   
   /**
    * This method take the integers from the input file and puts
    * them into an integer array.
    * 
    * @param scan is a scanner to read the data
    * @param length is an integer representing the length of the file
    * @return an integer array
    * 
    * @author - Logan Griffin
    */
   static int[] setUpQuicksort(Scanner scan, int length) {

      // new int array
      int[] nums = new int[length];

      int index = 0;

      // read next integer and add to array
      while (scan.hasNextInt()) {

         nums[index] = scan.nextInt();
         index++;
      }
      
      // return int array
      return nums;
   } // end method to set up quick sort
  
   /**
    * This method creates an array of linked lists that represent
    * the natural runs from the input file. A new linked list is
    * created for every natural run.
    * 
    * @param read is a scanner to read the data
    * @param length is an integer representing the length of the file
    * @param output is a bufferedWriter to write to output file
    * @return a linked list array
    * 
    * @author - Logan Griffin
    */
   static LinkedList[] setUpMerge(Scanner read, int length,
         BufferedWriter output) {

      // new linked list array
      LinkedList[] lists = new LinkedList[length];

      int index = 0;
      
      // start of natural run
      int base = read.nextInt();

      // output for file size 50
      if (length == 50) {
         try {
            output.write("\n\nStarting Merge Sort\n");
         } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
         }
      }
      
      // read through the file
      while (read.hasNextInt()) {

         // new linked list for the natural run
         LinkedList run = new LinkedList();
         int next = read.nextInt();
         Node start = new Node(base);

         // add the first integer to the linked list as a node
         run.insert(start);

         // while the next number is higher
         while (next > base) {
            numComps = numComps + 1;
            Node follow = new Node(next);
            run.insert(follow);

            base = next;
            // get the next number to compare
            if (read.hasNextInt()) {
               next = read.nextInt();
            } else {
               break;
            }
         }

         // to account for comparison that breaks the loo
         numComps = numComps + 1;

         // iterate base number for new run
         base = next;

         // print list for file size 50
         if (length == 50) {

            try {
               output.write("\nPrinting new List: ");
            } catch (IOException e) {
               // TODO Auto-generated catch block
               e.printStackTrace();
            }
//            System.out.println("Head of created list is: ");
//            System.out.println(run.head.data);
            run.printList(run.head, output);
         }

         lists[index] = run;
         index++;
      } // end reading file
      
      
      // if the last number in the file is in a list by itself,
      // add that single node as a list to the array
      if (base != lists[index - 1].tail.data) {
         
         if (length == 50) {
            try {
               output.write("Printing new List: \n");
               output.write(base);
            } catch (IOException e) {
               // TODO Auto-generated catch block
               e.printStackTrace();
            }
         }
         
         LinkedList last = new LinkedList();
         Node straggler = new Node(base);
         last.insert(straggler);
         lists[index] = last;
      }

      // return the array of linked lists
      return lists;
      
   } // end method to set up merge sort

   /**
    * This method partitions an integer array depending on the type of
    * quicksort desired. Numbers from the lower and upper partitions are
    * checked against the pivot (first value in partition) and swapped if
    * an item lower than the pivot is found in upper partition or an item 
    * higher than the pivot is found in lower partition. Part of this code
    * was copied from the class Zybook (section 7.16)
    * 
    * @param numbers is an integer array
    * @param lowIndex is an integer representing the low end of the low partition
    * @param highIndex is an integer representing the high end of the upper partition
    * @param variant is an integer representing the type of quick sort
    * @param length is an integer representing the length of the file 
    * @param output is a bufferedwriter to write to the output file
    * @return an integer that represents the upper end of the lower partition.
    * 
    * @author - Logan Griffin, along with Zybook as stated above.
    */
   static int partition(int[] numbers, int lowIndex, int highIndex,
         int variant, int length, BufferedWriter output) {

      // output for file size 50
      if (length == 50) {

         // print the list as is
         for (int i = 0; i < numbers.length; i++) {
            // write to output
            try {
               output.write(numbers[i] + ", ");

            } catch (IOException e) {
               // TODO Auto-generated catch block
               e.printStackTrace();
            }
         }
         // print the variant of quick sort happening
         try {
            output.newLine();
            output.write("Variant of quickSort is: " + variant + "\n");
         } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
         }
      }

      // picking pivot
      int pivot = 0;

      if (variant == 4) {
         // median of three pivot method
         int low = numbers[lowIndex];
         int middle = numbers[lowIndex + (highIndex - lowIndex) / 2];
         int high = numbers[highIndex];

         // print for file size 50
         if (length == 50) {

            try {
               output.write("Picking median of 3 pivot: \n");
               output.write("Low is: " + low + "\n");
               output.write("Middle is: " + middle + "\n");
               output.write("High is: " + high + "\n");
            } catch (IOException e) {
               // TODO Auto-generated catch block
               e.printStackTrace();
            }
         }

         // determine the median number
         if (low == middle && middle == high) {
            pivot = low;
         } else if (low == middle || low == high) {
            pivot = low;
         } else if (middle == high) {
            pivot = middle;
         } else if (low > middle && low < high) {
            pivot = low;
         } else if (low > high && low < middle) {
            pivot = low;
         } else if (middle > low && middle < high) {
            pivot = middle;
         } else if (middle < low && middle > high) {
            pivot = middle;
         } else if (high < low && high > middle) {
            pivot = high;
         } else if (high > low && high < middle) {
            pivot = high;
         }

         numComps = numComps + 2;

      } else {
         // if not variant 4, pick the pivot as the low index.
         pivot = numbers[lowIndex];
      }
      
      // write to output for size 50
      if (length == 50) {

         try {
            output.write("\nPivot set as: " + pivot + "\n");
         } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
         }
      }

      boolean done = false;

      // while there are still items higher than pivot in low partition
      // or items lower than pivot in the high partition
      while (!done) {
         
         // increment lowIndex while numbers[lowIndex] < pivot
         // moving up the low partition looking for value higher than pivot
         while (numbers[lowIndex] < pivot) {
            numComps = numComps + 1;
            lowIndex = lowIndex + 1;
         }

         // print for file size 50
         if (length == 50) {
            try {
               output.write("Low Index is: " + lowIndex + "\n");
            } catch (IOException e) {
               // TODO Auto-generated catch block
               e.printStackTrace();
            }
         }

         // decrement highIndex while pivot < numbers[highIndex]
         // moving down the upper partition looking for a value lower than pivot
         while (pivot < numbers[highIndex]) {
            numComps = numComps + 1;
            highIndex = highIndex - 1;
         }

         // print for file size 50
         if (length == 50) {
            try {
               output.write("High Index is: " + highIndex + "\n");
            } catch (IOException e) {
               // TODO Auto-generated catch block
               e.printStackTrace();
            }
         }

         // if zero or one elements remain, then all numbers are partitioned, return
         // highIndex
         if (lowIndex >= highIndex) {
            done = true;
         } else {

            // swap lowIndex and highIndex values
            numSwaps = numSwaps + 1;
            int temp = numbers[lowIndex];
            numbers[lowIndex] = numbers[highIndex];

            // print for file size 50
            if (length == 50) {
               try {
                  output.write("Numbers swapped were: " + temp + " and "
                        + numbers[highIndex] + "\n");
               } catch (IOException e) {
                  // TODO Auto-generated catch block
                  e.printStackTrace();
               }
            }

            numbers[highIndex] = temp;
            // update high and low index
            lowIndex++;
            highIndex--;
         }

      } // end swapping while loop

      // print the array after partitioning
      if (length == 50) {
         try {
            output.write("\nOrder updated to: \n");
         } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
         }
         
         for (int i = 0; i < numbers.length; i++) {
            try {
               output.write(numbers[i] + ", ");
            } catch (IOException e) {
               // TODO Auto-generated catch block
               e.printStackTrace();
            }
         }
      }

      return highIndex;

   } // end partition method

   /**
    * This method calls the partition method and recursively calls itself
    * while the base cases have not been met. The base case is that no more
    * sorting needs to be done. Variant 2 of the quicksort will complete an
    * insertion sort when the partitions are less than 100 elements. Variant
    * 3 will complete an insertion sort when the partitions less than 50
    * elements. Part of this code was copied from the class Zybook (Section
    * 7.16).
    * 
    * @param numbers is an integer array
    * @param lowIndex is an integer representing the low end of the low partition
    * @param highIndex is an intger representing the high end of the upper parition
    * @param variant is an integer representing the type of quick sort
    * @param length is an integer representing the length of the file
    * @param output is a bufferedwriter to write to the output file
    * 
    * @author - Logan Griffin, along with Zybook as stated above.
    */
   static void quickSort(int[] numbers, int lowIndex, int highIndex,
         int variant, int length, BufferedWriter output) {

      // base case showing that all items are sorted
      if (lowIndex >= highIndex) {
         return;
      }

      // partition the data within the array. lowEndIndex returned from partitioning
      // is the index of the low partition's last element
      int lowEndIndex = partition(numbers, lowIndex, highIndex, variant,
            length, output);

      // recursively sort low partition (lowIndex to lowEndIndex) and high partition
      // (lowEndIndex + 1 to highIndex)
      if ((variant == 3 && (lowEndIndex - lowIndex <= 50))
            || (variant == 2 && (lowEndIndex - lowIndex <= 100))) {

         // print for file size 50
         if (length == 50) {

            try {
               output.write("\nInsertion sort for low partition started.\n");
            } catch (IOException e) {
               // TODO Auto-generated catch block
               e.printStackTrace();
            }
         }
         
         // insertion sort if conditions are met
         for (int i = lowIndex; i <= lowEndIndex; i++) {

            int j = i;
            
            // swapping with values to the left that are higher
            while (j > 0 && numbers[j] < numbers[j - 1]) {
               numComps = numComps + 1;
               numSwaps = numSwaps + 1;

               // swap numbers
               int temp = numbers[j];
               numbers[j] = numbers[j - 1];
               numbers[j - 1] = temp;
               --j;
            }
            numComps = numComps + 1;
         } // end insertion sort

         // print list after insertion sort
         if (length == 50) {
            try {
               output.write("Insertion sort for low partition complete.\n");
               output.write("Order is now: \n");
            } catch (IOException e) {
               // TODO Auto-generated catch block
               e.printStackTrace();
            }

            for (int i = 0; i < numbers.length; i++) {
               try {

                  output.write(numbers[i] + ", ");
               } catch (IOException e) {
                  // TODO Auto-generated catch block
                  e.printStackTrace();
               }
            }
         }

      // to stop at partitions of two and one to simply compare
      } else if (variant == 1 && (lowEndIndex - lowIndex < 2)) {

         // compare last two numbers if partition is only size 2
         // swap if value at lower index is higher
         if (numbers[lowIndex] > numbers[lowEndIndex]) {
            numComps = numComps + 1;
            numSwaps = numSwaps + 1;
            
            // swap
            int temp = numbers[lowIndex];
            numbers[lowIndex] = numbers[lowEndIndex];

            // print for file size 50
            if (length == 50) {
               try {
                  output.write("\nNumbers swapped were: " + temp + ", "
                        + numbers[lowEndIndex] + "\n");
               } catch (IOException e) {
                  // TODO Auto-generated catch block
                  e.printStackTrace();
               }
            }

            numbers[lowEndIndex] = temp;
         }
         // to account for comparison that didnt go through if statement
         numComps = numComps + 1;

      // if none of the stopping cases are met, call the method recursively
      } else {
         
         // print for file size 50
         if (length == 50) {
            try {
               output.write("\nCalling quicksort between index " + lowIndex
                     + " and " + lowEndIndex + "\n");
            } catch (IOException e) {
               // TODO Auto-generated catch block
               e.printStackTrace();
            }
         }
         // recursive call for lower partition
         quickSort(numbers, lowIndex, lowEndIndex, variant, length, output);
      }

      // recursively sort upper partition
      if ((variant == 3 && (highIndex - lowEndIndex <= 50))
            || (variant == 2 && (highIndex - lowEndIndex <= 100))) {
         // print for file size 50
         if (length == 50) {
            try {
               output.write(
                     "\nInsertion sort for high partition started.\n");
            } catch (IOException e) {
               // TODO Auto-generated catch block
               e.printStackTrace();
            }
         }

         // insertion sort
         for (int i = lowEndIndex; i <= highIndex; i++) {

            int j = i;
            
            // swapping with values to the left that are higher
            while (j > 0 && numbers[j] < numbers[j - 1]) {
               numComps = numComps + 1;
               numSwaps = numSwaps + 1;
               
               // swap numbers
               int temp = numbers[j];
               numbers[j] = numbers[j - 1];
               numbers[j - 1] = temp;
               --j;
            }
            numComps = numComps + 1;
         } // end insertion sort

         // print list after insertion sort
         if (length == 50) {
            try {
               output.write("Insertion sort for high partition complete.\n");
               output.write("Order is now: \n");
            } catch (IOException e) {
               // TODO Auto-generated catch block
               e.printStackTrace();
            }

            for (int i = 0; i < numbers.length; i++) {
               try {

                  output.write(numbers[i] + ", ");
               } catch (IOException e) {
                  // TODO Auto-generated catch block
                  e.printStackTrace();
               }
            }
         }

      // to stop at partitions of two and one to simply compare 
      } else if (variant == 1 && (highIndex - lowEndIndex < 2)) {

         // compare last two numbers if partition is only size 2
         // swap if value at lower index is higher
         if (numbers[lowEndIndex] > numbers[highIndex]) {
            numComps = numComps + 1;
            numSwaps = numSwaps + 1;
            
            // swap
            int temp = numbers[lowEndIndex];
            numbers[lowEndIndex] = numbers[highIndex];
            
            // print for file size 50
            if (length == 50) {
               try {
                  output.write("\nNumbers swapped were: " + temp + ", "
                        + numbers[highIndex] + "\n");
               } catch (IOException e) {
                  // TODO Auto-generated catch block
                  e.printStackTrace();
               }
            }
            numbers[highIndex] = temp;
         }
         // to account for comparison that didnt go through if statement
         numComps = numComps + 1;

      // if none of the stopping cases are met, call the method recursively
      } else {
         if (length == 50) {
            try {
               output.write("\nCalling quicksort between index "
                     + lowEndIndex + " and " + highIndex + "\n");
            } catch (IOException e) {
               // TODO Auto-generated catch block
               e.printStackTrace();
            }
         }
         // recursive call
         quickSort(numbers, lowEndIndex + 1, highIndex, variant, length,
               output);
      }
   } // end quick sort method

   /**
    * This method merges linked lists in an array of linked lists, 2 at a time.
    * Once all the lists have been merged once, the method is called recursively
    * until there is only one linked list remaining. Parts of this method were 
    * copied and adapted from the class Zybook (section 8.5).
    * 
    * @param arr is an array of linked lists
    * @param length is an integer representing the length of the file
    * @param output is a bufferedwriter to write to the output file
    * 
    * @author - Logan Griffin
    */
   static void merge(LinkedList[] arr, int length, BufferedWriter output) {

      // base case for recursive function, when there is only one list left
      if (arr[1] == null && arr[2] == null) {
         return;
      } else {

         // figure out how many items there are to merge
         int k = 0;
         while (k < arr.length && arr[k] != null) {
            k = k + 1;
         }

         int itemsToMerge = k - 1;
         
         // print for file size 50
         if (length == 50) {
            try {
               output.write("\nLists to Merge: " + itemsToMerge + "\n");
            } catch (IOException e) {
               // TODO Auto-generated catch block
               e.printStackTrace();
            }
         }

         int i = 0;

         // to go through all the merges in the array
         while (i <= itemsToMerge) {
            // new linked list that matches the linked list
            // in the index of the first two to be merged
            LinkedList first = new LinkedList();
            first = arr[i];

            // print for file size 50
            if (length == 50) {
               try {
                  output.write("\nFirst list of merge is: \n");
               } catch (IOException e) {
                  // TODO Auto-generated catch block
                  e.printStackTrace();
               }
               first.printList(first.head, output);
            }
            
            // new linked list that matches the linked list
            // in the index of the second two to be merged
            LinkedList second = new LinkedList();

            // if at the end of the array on the first pass
            // second list will be null
            if (i == arr.length - 1) {
               second.head = null;          
            // if at the end of the lists that need to merge
            // if the second list needs to be null
            } else if (arr[i + 1] == null) {
               second.head = null;
            } else {
               // set the second list
               second = arr[i + 1];
            }

            // print for file size 50
            if (length == 50) {
               try {
                  output.write("\nSecond list of merge is: \n");
               } catch (IOException e) {
                  // TODO Auto-generated catch block
                  e.printStackTrace();
               }
               second.printList(second.head, output);

            }

            // new linked list for the merge sort
            LinkedList merged = new LinkedList();
            
            // from Zybook (section 8.5)
            // while there are still nodes in the two lists being merged
            while (first.head != null && second.head != null) {

               numComps = numComps + 1;

               // if next value in first list is lower than second list
               if (first.head.data <= second.head.data) {
                  
                  // insert into new list
                  merged.insert(first.head);
                  
                  // print for file size 50
                  if (length == 50) {
                     try {
                        output.write("\nInserted: " + first.head.data);
                     } catch (IOException e) {
                        // TODO Auto-generated catch block
                        e.printStackTrace();
                     }
                  }
                  // delete node from the first list
                  first.delete();
               } else {
                  // if the next value in the second list is lower than the first list
                  merged.insert(second.head);
                  
                  // print for file size 50
                  if (length == 50) {
                     try {
                        output.write("\nInserted: " + second.head.data);
                     } catch (IOException e) {
                        // TODO Auto-generated catch block
                        e.printStackTrace();
                     }
                  }
                  // delete node from the second list
                  second.delete();
               }
            }

            // if first list is empty, load the second
            while (first.head == null && second.head != null) {
               merged.insert(second.head);
               if (length == 50) {
                  try {
                     output.write("\nFirst list empty. Inserted: "
                           + second.head.data);
                  } catch (IOException e) {
                     // TODO Auto-generated catch block
                     e.printStackTrace();
                  }
               }
               second.delete();
            }

            // if second list is empty, load the first
            while (second.head == null && first.head != null) {
               merged.insert(first.head);
               if (length == 50) {
                  try {
                     output.write("\nSecond list empty. Inserted: "
                           + first.head.data);
                  } catch (IOException e) {
                     // TODO Auto-generated catch block
                     e.printStackTrace();
                  }
               }
               first.delete();
            }

            // empty index
            arr[i] = null;

            // if the second list was null
            if (i == arr.length - 1) {
               // do nothing
            } else {
               // empty the second index
               arr[i + 1] = null;
            }
            
            // print for file size 50
            if (length == 50) {
               try {
                  output.write(
                        "\nInserting merged list into index: " + i / 2);
                  output.write("\nMerged list is: \n");

               } catch (IOException e) {
                  // TODO Auto-generated catch block
                  e.printStackTrace();
               }
               merged.printList(merged.head, output);
            }

            // insert merged list back into array for next pass
            arr[i / 2] = merged;

            i = i + 2;
 
            if (length == 50) {
               try {
                  output.newLine();
               } catch (IOException e) {
                  // TODO Auto-generated catch block
                  e.printStackTrace();
               }
            }
         } // end while loop
         
         // recursive call to merge the lists in the array again
         merge(arr, length, output);
      }
   } // end merge method
} // end class
