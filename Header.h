#pragma once
#include <iostream>
#include <ctime>
#include <iomanip>
#include <algorithm>

using namespace std;

int find_matrix_determinant_3x3(double **arr) {
	double result=0;
	result += arr[0][0] * arr[1][1] * arr[2][2];
	result += arr[0][1] * arr[1][2] * arr[2][0];
	result += arr[1][0] * arr[0][2] * arr[2][1];
	result -= arr[0][2] * arr[1][1] * arr[2][0];
	result -= arr[0][0] * arr[1][2] * arr[2][1];
	result -= arr[1][0] * arr[0][1] * arr[2][2];
	return result;
}

double** creating_new_array(double **arr, int arr_size, int row, int column) {
	double **new_arr = new double*[arr_size - 1];
	for (int i = 0; i < arr_size - 1; i++) {
		new_arr[i] = new double[arr_size-1];
	}
	bool flag = false;
	int new_row = 0;
	int new_column = 0;
	for (int i = 0; i < arr_size; i++) {
		for (int j = 0; j < arr_size; j++) {
			if (i != row && j != column) {
				new_arr[new_row][new_column] = arr[i][j];
				//cout << setw(4) << arr[i][j];
				new_column++;
				flag = true;
			}
		}
		if (flag == true) {
			new_column = 0;
			new_row++;
		}
		flag = false;
		//cout << endl;
	}
	//cout << endl;
	return new_arr;
}

int find_matrix_determinant(double **arr, int arr_size, int row, int column) {
	int result = 0;
	for (int i = 0; i < arr_size; i++) {
		if (arr_size > 3) {
			if(i%2==0)
				result += arr[row][i] * find_matrix_determinant(creating_new_array(arr, arr_size, row, i), arr_size-1, row, i);
			else
				result -= arr[row][i] * find_matrix_determinant(creating_new_array(arr, arr_size, row, i), arr_size - 1, row, i);
		}
		else {
			result += find_matrix_determinant_3x3(arr);
			break;
		}

	}
	return result;
}

double** matrix_transposition(double **arr, int arr_size) {
	int i = 0;
	for (int j = 1; j < arr_size; j++) {
		swap(arr[i][j], arr[j][i]);
		if (j == arr_size - 1) {
			i++;
			j = i;
		}
	}
	return arr;
}

double* multiplication_matrix(double **arr, int arr_size, int number, double *b_arr) {
	double *result_arr = new double[arr_size];
	for (int i = 0; i < arr_size; i++) {
		double result_column = 0;
		for (int j = 0; j < arr_size; j++) {
			result_column += arr[i][j] * b_arr[j];
		}
		result_arr[i] = result_column/number;
	}
	return result_arr;
}

double* test(double **a_arr, double *c_arr, int arr_size) {
	double *result = new double[arr_size];
	for (int i = 0; i < arr_size; i++) {
		result[i] = 0;
		for (int j = 0; j < arr_size; j++) {
			result[i] += a_arr[i][j] * c_arr[j];
		}
	}
	return result;
}