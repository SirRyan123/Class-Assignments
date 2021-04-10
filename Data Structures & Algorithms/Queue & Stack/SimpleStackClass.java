package p5_package;

public class SimpleStackClass
   {
    /**
     * Provides constant for default capacity
     */
    private final int DEFAULT_CAPACITY = 10;
   
    /**
     * Provides constant -999999 for access failure messaging
     */
    public static final int FAILED_ACCESS = -999999;
   
    /**
     * Stores current capacity of stack class
     */
    private int capacity;

    /**
     * Stores current size of stack class
     */
    private int size;
   
    /**
     * Stores stack top index
     */
    private int stackTopIndex;
   
    /**
     * Integer array stores stack data 
     */
    private int[] stackData;
   
    /**
     * Default constructor
     * 
     */
    public SimpleStackClass()
       {
        capacity = DEFAULT_CAPACITY;
        
        size = 0;
        
        stackTopIndex = -1;
               
        stackData = new int[ capacity ];
       }
      
    /**
     * Initialization constructor
     * 
     * @param capacitySetting initial capacity of stackData class
     * 
     */
    public SimpleStackClass( int capacitySetting )
       {
        capacity = capacitySetting;
       
        size = 0;
       
        stackTopIndex = -1;
              
        stackData = new int[ capacity ];
       }

    /**
     * Copy constructor
     * 
     * @param copied SimpleStackClass object to be copied
     * 
     */
    public SimpleStackClass( SimpleStackClass copied )
       {
        int index;
        capacity = copied.capacity;
       
        size = copied.capacity;
       
        stackTopIndex = copied.stackTopIndex;
              
        stackData = new int[ capacity ];
       
        for( index = 0; index < size; index++ )
           {
            stackData[ index ] = copied.stackData[ index ];
           }
       }

    /**
     * Checks for resize and resizes to twice the current
     * capacity if needed
     * <p>
     * Note: Returns true if resize is necessary and is conducted;
     * returns false if no action is taken
     * 
     * @return success of operation
     */
    private boolean checkForReSize()
       {
        int tempArr[];
        int index;
       
        if( size == capacity )
           {
            capacity *= 2;
            
            tempArr = new int[ capacity ];
           
            for( index = 0; index < size; index++ )
               {
                tempArr[ index ] = stackData[ index ];
               }                  
                       
           stackData = tempArr;
           
           return true;
          }
   
       return false;
      }

   /**
     * Clears stack by setting size to zero
     * and top index to negative one
     */
    public void clear()
       {
        size = 0;
        
        stackTopIndex = -1;
       }

   /**
     * Reports stack empty status
     * <p>
     * Note: Does not use if/else
     * 
     * @return Boolean evidence of empty list
     */
    public boolean isEmpty()
       {
        return size == 0;
       }
   
    /**
     * provides peek at top of stack
     * 
     * @return value if successful, FAILED_ACCESS if not
     */
    public int peekTop()
       {
        if( !isEmpty() )
          {
           return stackData[ stackTopIndex ];
          }
       
        return FAILED_ACCESS;
       }

   /**
     * Removes and returns data from top of stack
     * 
     * @return value if successful, FAILED_ACCESS if not
     */
    public int pop()
       {
        if( !isEmpty() )
           {
            size--;
            
            stackTopIndex--;
           
            return stackData[ stackTopIndex + 1 ];
           } 
       
        return FAILED_ACCESS;
       }

   /**
     * Checks for resize, then pushes value onto stack
     * <p>
     * Note: end of array is always the top of the stack;
     * index is incremented and then value is appended to array
     * 
     * @param newValue Value to be pushed onto stack
     */
    public void push( int newValue )
       {
        checkForReSize();
        
        stackTopIndex++;
        
        stackData[ stackTopIndex ] = newValue;
        
        size++;
       }

   }
