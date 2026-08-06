class Triangle_0_1{
    public static void main(String[] args){
 int n=5;


        for(int i=1;i<=n;i++){
            int val=0;
            
            if(i%2==1){
                val=1;
            }

            for(int j=1; j<=i;j++){
                System.out.print(val);
                if(val==0){
                    val=1;
                }
                else{
                    val=0;
                }
            }
            System.out.println(" ");
        }
    }
}