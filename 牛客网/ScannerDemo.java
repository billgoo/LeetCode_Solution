import java.util.Scanner; 
 
public class ScannerDemo {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int i = 0;
        while (in.hasNextInt()) {//注意while处理多个case              int a = in.nextInt();
            char b = in.next().charAt(i);
            System.out.println(b);
            i++;
        }
        in.close();
    }
}