public class Determinants{
  public static double det(double[][] matrix){
    if (matrix.length != matrix[0].length || matrix.length == 0){
      return -1;
    }
    else if (matrix.length == 1){
      return matrix[1][1];
    }
    else if (matrix.length == 2){
      return (matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]);
    }
    else{
      String[][] signs = new String[matrix.length][matrix.length];
      for (int i = 0; i < matrix.length; i++){
        for (int j = 0; j < matrix.length; j++){
          if ((i + j + 2) % 2 == 0){
            signs[i][j] = "+";
          }
          else{
            signs[i][j] = "-";
          }
        }
      }
      double sum = 0;

      for (int i = 0; i < matrix.length; i++){
        double coefficient = matrix[0][i];
        if (signs[0][i].equals("-")){
          coefficient *= -1;
        }
        double[][] submatrix = new double[matrix.length - 1][matrix.length - 1];
        for (int row = 1; row < matrix.length; row++){
          int colInc = 0;
          for (int col = 0; col < matrix.length; col++){
            if (col != i){
              submatrix[row - 1][colInc] = matrix[row][col];
              colInc++;
            }
          }
        }
        sum += coefficient * det(submatrix);
      }
      return sum;
    }
  }
  public static void main(String[] args){
    double[][] A = new double[][] {{1,2,3},{0,5,6},{0,0,9}};
    System.out.println(det(A));
  }
}
