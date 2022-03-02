import java.util.*;
import java.io.*;
import java.lang.Math;

public class PowerTwo
{
    public static int checkforPowerTwo(int N) {

        //this is default OUTPUT. You can change it.
        int result = 0;
        if (N==1 || N==-1 || N==0) return -1;
        //write your Logic here:
        while (N!=1 && N!=-1){
            if (N % 2!=0){
                result=-1;
                break;
            }else {
                result++;
                N/=2;
            }
        }
        if (N==-1 && result % 2==0 ){
            return -1;
        }
        return result;
    }
    public static void main (String[] args)
    {
        Scanner sc=new Scanner(System.in);

        //INPUT [uncomment & modify if required]
        int N = sc.nextInt();
        sc.close();

        //OUTPUT [uncomment & modify if required]
        System.out.print(checkforPowerTwo(N));
    }
}
