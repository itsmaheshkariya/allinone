import java.util.*;
class StringDemo{
    public static void main(String args[]){
        String str;
        char n;
        int count=0;
        Scanner input= new Scanner(System.in);
        System.out.println("Enter any string:");
        str=input.next();
        char[] c=str.toCharArray();
        int count[];
        for(int j=0;j<c.length:j++)   
            for(int i=j+1;i<c.length;i++)
                {
                    if(c[j]==c[i])
                    {
                        count++;
                    }
                }
            System.out.println(count);
        // }
             


    }
}