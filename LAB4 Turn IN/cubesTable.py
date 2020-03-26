# CPE 101 Lab 4
# Name:Hayden Tam

def main():
   table_size = get_table_size()
   while table_size != 0:
      first = get_first()
      increment=get_increment()
      show_table(table_size, first,increment)
      table_size = get_table_size()
      

      

# Obtain a valid table size from the user
#none->int
def get_table_size():
   size = int(input("Enter number of rows in table (0 to end): "))

   while (size) < 0:
      print ("Size must be non-negative.")
      size = int(input("Enter number of rows in table (0 to end): "))
      
   return size;

# Obtain the first table entry from the user 
#none->int
def get_first():
   first = int(input("Enter the value of the first number in the table: "))
   while(first<0):
       print("First number must be non-negative.")
       first=int(input("Enter the value fo the first number in the table:"))
   return first;

# Display the table of cubes
#int,int,int->none
def show_table(size, first,increment):
   
   print ("A cube table of size %d will appear here starting with %d." % (size, first))
   print ("Number  Cube")
   sum=0
   # Insert Loop Here
   for first in range  (first,(size*increment)+first,increment):
        
         print ("%-6d %s %-16d" % (first,"", first**3))
         sum+=(first**3)
   print()
   print("The sum of cubes is:", sum)
    
#Ask user for the increment between rows
#none->int
def get_increment():
    increment=int(input("Enter the increment between rows:"))
    while(increment<0):
        print("Increment must be non-negative.")
        increment=int(input("Enter the increment between rows:"))
        
    return increment;

if __name__ == "__main__":
   main()
