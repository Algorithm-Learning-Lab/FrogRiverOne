
def solution(X, A):
  result = -1
  sum = 0
  n = len(A)

  if (n < 1 or n > 1000000) or (X < 1 or X > 1000000) :
    return print("result: range error")
  
  for i in range(n) :
    if A[i] > X or A[i] < 1 :
      return print("result: range error")



  LeavesBridge = [0] * (X+1)

  for k in range(n) :
    if A[k] <= X :  
      if LeavesBridge[A[k]] == 0 :
        LeavesBridge[A[k]] = 1
        sum += 1
    if sum == X :
      result = k
      break
  
  print("sum:", sum)
  print("result:", result)





A = list(map(int, input("insert array A : ").split()))
X = int(input("insert X : "))

solution(X, A)
