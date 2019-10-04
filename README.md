Gradient Descent 구현
=====================
#### 모듈 1: Basic Vector Operations  
* 두 벡터를 더하는 함수 add를 작성하세요. add 함수는 리스트 vec1과 vec2를 입력으로 받아 그 결과를 리스트로 반환합니다.
```
def add(vec1, vec2) :
    #Your code here

#example
add([1, 2], [3, 4]) == [4, 6]
```
* 다음으로는 스칼라 곱을 구현하는 함수 multiply를 작성합니다. multiply 함수는 int 혹은 float 값 scal과 리스트 vec을 입력으로 받아 그 결과를 리스트로 반환합니다.
```
def multiply(scal, vec) :
    #Your code here

#example
multiply(2, [2, 1]) == [4, 2]
```
#### 모듈 2: Numerical Differentiation
* 함수 uni_func와 int 혹은 float 값 float_t를 입력으로 받아, float_t에서의 uni_func의 미분계수를 결과로 출력하는 함수 df_dx를 작성합니다. 미분계수의 정의(변화율의 극한값)를 이용하여 근삿값을 구하는 것으로 충분합니다. 더 자세한 내용을 알고 싶으시면 위키백과의 [Numerical differentiation](https://en.wikipedia.org/wiki/Numerical_differentiation) 문서를 참고하세요.
```
def df_dx(uni_func, float_t) :
    #Your code here

#example
derivative = df_dx(lambda x: x+1, 1)
round(derivative) == 1
```
* 다음으로는 다변수함수 multi_func와 리스트 list_t를 입력으로 받아, list_t에서의 그래디언트를 리스트로 출력하는 함수 gradient를 작성합니다. 앞에서 작성한 df_dx 함수를 이용해 편미분 값을 구하시면 됩니다. multi_func는 리스트를 입력으로 받아 int 혹은 float 값을 반환하는 함수로 생각합니다.
```
def gradient(multi_func, list_t) :
    #Your code here

#example
grad = gradient(lambda x : sum(x), [1, 2])
list(map(round, grad)) == [1, 1]
```
#### 모듈 3: Gradient Descent
* 위키백과의 [Gradient descent](https://en.wikipedia.org/wiki/Gradient_descent) 문서를 참고하시고 Computational examples의 Python 코드를 임의의 다변수함수에 대해서도 적용할 수 있도록 수정해보세요. 다변수함수 multi_func와 리스트 start_t를 입력받아, start_t에서 출발하여 multi_func를 최소로 만드는 벡터값을 찾아 리스트 형태로 반환하는 함수 optim을 작성하시면 됩니다. 추가로 루프문의 반복횟수와, time 모듈을 이용해서 구한 함수의 실행 시간을 같이 출력해주세요.
```
from time import time
def optim(multu_func, start_t) :
    #Your code here
 
#example
def myfunc(list_t) :
    return list_t[0]**2 + list_t[1]**2

optimal_t = optim(myfunc, [1, 1])
list(map(round, optimal_t)) == [0, 0]
```
