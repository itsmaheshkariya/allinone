import java.util.Scanner;
class Switch{
public static void main(String args[]) {

    Scanner op = new Scanner(System.in);
    int key = op.nextInt();
    switch (key) {
        case 1:
            System.out.print(1);
            break;
        case 2:
            System.out.print(2);
            break;
        default:
            System.out.print("nothing");
            break;
    }
    System.out.println();
}
}