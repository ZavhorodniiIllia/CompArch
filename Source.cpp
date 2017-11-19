#include "Header.h"


int main() {
	
	//Creating an array
	int arr_size;
	int determinant;
	cout << "Input array size: ";
	cin >> arr_size;
	double **arr = new double *[arr_size];
	double **a_arr = new double *[arr_size];
	double *b_arr = new double[arr_size];
	double *c_arr = new double[arr_size];
	double *result_arr = new double[arr_size];
	for (int i = 0; i < arr_size; i++) {
		arr[i] = new double[arr_size];
		a_arr[i] = new double[arr_size];
	}
	
	//Filling and outputing the array with random numbers
	for (int i = 0; i < arr_size; i++) {
		for (int j = 0; j < arr_size; j++) {
			arr[i][j] = (rand() % 21) - 10;
			cout << setw(4) << arr[i][j];
			if (j == arr_size - 1) {
				b_arr[i] = (rand() % 21) - 10;
				cout << setw(4) << b_arr[i];
			}
		}
		cout << endl;
	}

	determinant = find_matrix_determinant(arr, arr_size, 0, 0);
	//cout << determinant << endl;

	//Finding addition to matrix
	for (int i = 0; i < arr_size; i++) {
		for (int j = 0; j < arr_size; j++) {
			if (j % 2 == 0 && i%2 == 0)
				a_arr[i][j] = find_matrix_determinant(creating_new_array(arr, arr_size, i, j), arr_size-1, 0, 0);
			else if (j % 2 == 1 && i % 2 == 0)
				a_arr[i][j] = (- find_matrix_determinant(creating_new_array(arr, arr_size, i, j), arr_size-1, 0, 0));
			else if (j % 2 == 0 && i % 2 == 1)
				a_arr[i][j] = (-find_matrix_determinant(creating_new_array(arr, arr_size, i, j), arr_size - 1, 0, 0));
			else 
				a_arr[i][j] = find_matrix_determinant(creating_new_array(arr, arr_size, i, j), arr_size - 1, 0, 0);
			//cout << setw(6) << a_arr[i][j];
		}
		//cout << endl;
	}
	//cout << endl;

	a_arr = matrix_transposition(a_arr, arr_size);
	/*for (int i = 0; i < arr_size; i++) {
	for (int j = 0; j < arr_size; j++) {
			cout << setw(10) << a_arr[i][j];
		}
		cout << endl;
	}*/

	c_arr = multiplication_matrix(a_arr, arr_size, determinant, b_arr);
	for (int j = 0; j < arr_size; j++) {
		cout << setw(10) << c_arr[j] << endl;
	}
	cout << endl;

	cout << "Test:" << endl;
	result_arr = test(arr, c_arr, arr_size);
	for (int i = 0; i < arr_size; i++) {
		cout << setw(3) << result_arr[i] << '=' << setw(3) << b_arr[i] << endl;
	}

	//Deliting the array
	for (int i = 0; i < arr_size; i++) {
		delete[]arr[i];
	}

	system("pause");
}