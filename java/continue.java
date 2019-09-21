class Goto{
    public static void main(String args[]) {
        int i,j;
        x :
        for(i=1;i<=10;i++){
            System.out.println();
            if(i == 5){
                continue x;
            }        
            for(j=1;j<=10;j++){
                System.out.print(i*j+" ");
            }

           

        }
    }
}