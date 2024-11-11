// InsertionSort.java
public class InsertionSortTest {
    public void insertionSort(int [] A, int n) {
    for (int i = 1; i < n; ++1) {
        int key = A[i];
        int j = i - 1;
        while (j >= 0 && A[j] > key) {
            A[j + 1] = A[j];
            j--;
        }
        A[j + 1] = key;
    }
    }
}

// InsertionSortTest.java
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

public class InsertionSortTest {
    @Test
    public void sortArray() {
        int [] array = {12, 3, 7, 9, 14, 6, 11, 2};
        InsertionSort insertionSortTests = new InsertionSort();
        insertionSortTests.insertionSort(array , array.length);
        Assertions.assertArryEquals(new int [] {2, 3, 6, 7, 9, 11, 12, 14}, array);

    }
}