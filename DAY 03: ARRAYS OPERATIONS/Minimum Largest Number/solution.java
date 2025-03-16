import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

class Main 
{
    public static void main(String[] args) 
    {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
      
        int[] arr = new int[n];
        int small = Integer.MAX_VALUE;
        int secSmall = Integer.MAX_VALUE;
      
        for(int i = 0; i < n; i++) 
        {
            arr[i] = sc.nextInt();
            small = Math.min(arr[i], small);
        }
      
        int min = small;
        for (int i = 0; i < n; i++) 
        {
            if (arr[i] == small) 
            {
                small = 10;
                arr[i] = 10;
            }
          
            secSmall = Math.min(arr[i], secSmall);
        }
      
        //Arrays.sort(arr);
        System.out.println(secSmall*10 + min);
    }
}
