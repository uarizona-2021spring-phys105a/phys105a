#include <stdlib.h>
#include <stdio.h>

int n_trials = 100;

int randomwalk(int n_steps) {
  int X = 0;

  for (int i = 0; i < n_steps; ++i) {
    int last = X;
    int curr;
    int r = rand();
    if (r < RAND_MAX/2)
      curr = last + 1;
    else
      curr = last - 1;
    X = curr;
  }
  return X;
}


int main() {
  for (int t = 1; t < 1001; ++t) {
    double M = 0;
    for (int trial = 0; trial < n_trials; ++trial) {
      int X = randomwalk(t);
      M += abs(X);
    }
    M /= n_trials;
    printf("%d %g\n", t, M);
  }
  return 0;
}
