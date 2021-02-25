
public class Main
{
	
    static void bubbleSort(int[] listToBeSorted) {
        for (int number1 = 0; number1 < listToBeSorted.length; number1++) {
            for (int number2 = 0; number2 < listToBeSorted.length; number2++) {
                if (listToBeSorted[number1] < listToBeSorted[number2]) {
                    int temporaryValue = listToBeSorted[number1];
                    listToBeSorted[number1] = listToBeSorted[number2];
                    listToBeSorted[number2] = temporaryValue;
                }
            }
        }
        
        for (int number = 0; number < listToBeSorted.length; number++) {
            System.out.print(listToBeSorted[number] + ", ");
        }
    }
    
	public static void main(String[] args) {
		int[] listToBeSorted = {5, 9, 3, 1, 2, 8, 4, 7, 6};
		System.out.println("Not sorted list: ");
		
		for (int number = 0; number < listToBeSorted.length; number++) {
            System.out.print(listToBeSorted[number] + ", ");
        }
		
		System.out.println();
		System.out.println("Sorted list: ");
		bubbleSort(listToBeSorted);
	}
}
