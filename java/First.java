import java.util.Scanner;
class First{

public static void main(String args[]){
    System.out.println("Enter Type of processor:(8/16/32 bit) ");
    Scanner in = new Scanner(System.in);
    int a = in.nextInt();
    System.out.println("Enter Type of customer:(gov/uni/ind) ");
    Scanner in1 = new Scanner(System.in);
    String b = in1.nextLine();
    System.out.println("Enter Price ");
    Scanner in2 = new Scanner(System.in);
    int c = in2.nextInt();
    // System.out.println(b);
    double discount = 0.0;
    if(a == 32){
        if(c < 50000){
            if(b=="ind"){
                discount = 5;
            }else if(b=="gov"){
                discount = 6.5;
            }
            
        }else if(c>=50000 && c<100000){
            if(b=="ind"){
                discount = 7.5;
            }else if(b=="gov"){
                discount = 8.5;
            }
        }else{
            if(b=="ind" || b=="gov"){
                discount = 7.5;
            }else if(b=="uni"){
                discount = 8.5;
            }

        }
        
    }
    else if(a == 16){
        // System.out.println("Do 16");
        }
    else if(a == 8){
        // System.out.println("Do 8");
        }
    else{
        // System.out.println("Wrong Input");
        }
        System.out.println(discount);

}


}