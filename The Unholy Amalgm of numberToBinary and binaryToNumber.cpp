#include <iostream>
#include <cmath>
#include <string>
using namespace std;

   void numberToBinary(double sum){   
      int i = -1;
      while(sum >= pow(2, i + 1)){
         i += 1;
      }      
      string result = "";
      while(i >= 0){
         string str1;         
         if(sum >= pow(2, i)){              
            sum -= pow(2, i);              
            str1 = "1";                    
         }else{
            str1 = "0";                     
         }  
            result += str1;
            i -= 1;
         }
      cout << "Binary: " << result << endl;
   }
   
   
   void binaryToNumber(string str1){
      int sum = 0;
      int i = 0;
      string value = "";
      while(i < str1.length()){   
         value = str1.at(i);
         if(value == "1"){
            sum += pow(2, str1.length() - i - 1);      
         }
         i += 1;
      }
      cout << "Integer: " << sum << endl;
   }


int main(){

/* Quick note:

   When it comes to the binaryToNumber function, it can only go as high as 31 digits, 
   or any number less than or equal to 1111111111111111111111111111111 in Binary.
   
   As far as the numberToBinary, it can convert numbers as high as 999999999999999999, 
   but you should only do up to 2147483647, that way the binaryToNumber can still be used 
   (2147483647 converts to 1111111111111111111111111111111)
   
   Outside of that, just make sure when using the binaryToNumber function to input it as a string, 
   otherwise it won't work.
   
   numberToBinary();
                         
   binaryToNumber("");
    
   ^^^For copy/pasting
*/

   numberToBinary(42);
   //numberToBinary(999999999999999999);                      
   binaryToNumber("101010");
   
   return 0;
}
 