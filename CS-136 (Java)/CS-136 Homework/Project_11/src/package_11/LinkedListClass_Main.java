package package_11;

public class LinkedListClass_Main
{
	
      public static void main(String[] args)
         {
          // working set of student data
          StudentClass sc1 = new StudentClass( 
                                   "Johnson, Robert", 603667,'M', 2.844077875 );
          StudentClass sc2 = new StudentClass( 
                                   "Reyes, Connor", 191261,  'M', 3.295578577 );
          StudentClass sc3 = new StudentClass( 
                                   "Sanchez, Susan", 54838,  'F', 2.063213296 );
          StudentClass sc4 = new StudentClass( 
                                 "Penn, Frederick", 819367,  'M', 2.828974752 );
          StudentClass sc5 = new StudentClass( 
                               "Deangelis, Shawna", 764050,  'F', 2.203316877 );
          StudentClass sc6 = new StudentClass( 
                                 "Shafer, Tristan", 693686,  'F', 3.180700609 );
          StudentClass sc7 = new StudentClass( 
                                 "Ruan, Francisco", 587182,  'M', 3.726603614 );
          StudentClass sc8 = new StudentClass( 
                                    "Werner, Riley", 444253,  'F', 2.34553428 );
          StudentClass sc9 = new StudentClass( 
                              "Davis, Glen-Andrew", 488133,  'M', 3.937722411 );
          StudentClass sc10 = new StudentClass( 
                                    "Thomas, Sena", 302398,  'F', 2.918400394 );
          StudentClass sc11 = new StudentClass( 
                                  "Elliott, Cayley", 135658, 'F', 2.978848017 );
          
          // test default constructor
          LinkedListClass list = new LinkedListClass();
          // test append, with empty and non-empty list, 
          // display for verification
          
          // test getNodeData
          // display for verification
          //list.displayList();
          // test clearList
          // display for verification
          
          // test getNodeData
          // display for verification

          // test insertNodeAfter with empty list,
          // list with data, and list without the specified
          // Student Class object in it
          list.appendData(sc1);
          list.appendData(sc2);
          list.displayList();
          // test insertNodePrio with empty list,
          // list with data, and list without the specified
          // Student Class object in it
          // test removeItem with empty list,
          // list with data, and list without the requested
          // Student Class object in it
          //                              
          
         }
      
      /**
       * Accepts name of student and returns StudentClass object
       * with dummy information to be used for inserting, accessing, or removing
       * data from linked list
       * 
       * @param name String name of student to be returned
       * as StudentClass object with dummy data
       * 
       * @return StudentClass object having name and dummy data
       */
      public static StudentClass getQueryObject( String name )
         {
          return new StudentClass( name, 0, 'x', 0.0 );
         }

   }