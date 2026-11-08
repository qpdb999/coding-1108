
'''
반복자 (Iterator)

    오늘 배운 내용

이번에는 파이썬에서 데이터를 하나씩 꺼내 사용할 수 있도록 도와주는
반복자(Iterator)에 대해 배웠다.

반복 가능한 객체와 반복자의 차이를 알아보고,
iter()와 next()를 사용하는 방법을 학습했다.

    정의

1) 반복 가능한 객체 (Iterable)

리스트, 튜플, 문자열처럼 반복문을 사용해
요소를 하나씩 가져올 수 있는 객체이다.

2) 반복자 (Iterator)

데이터를 한 번에 모두 가져오는 것이 아니라,
필요할 때마다 다음 요소를 하나씩 반환하는 객체이다.

3) iter()

반복 가능한 객체를 반복자로 변환하는 함수이다.

4) next()

반복자에서 다음 요소를 하나씩 가져오는 함수이다.
더 이상 가져올 요소가 없으면 StopIteration 오류가 발생한다.

    사용 방법

1) iter()와 next() 사용하기

numbers = [10, 20, 30, 40]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

실행 결과
10
20
30
40

2) 반복문으로 반복자 사용하기

numbers = [10, 20, 30]

iterator = iter(numbers)

for num in iterator:
    print(num)

실행 결과
10
20
30

3) 문자열을 반복자로 변환하기

text = "PYTHON"

iterator = iter(text)

print(next(iterator))
print(next(iterator))
print(next(iterator))

실행 결과
P
Y
T

4) while문으로 반복자 사용하기

numbers = [1, 2, 3, 4, 5]

iterator = iter(numbers)

while True:
    try:
        num = next(iterator)
        print(num)
    except StopIteration:
        break

실행 결과
1
2
3
4
5

    코드 분석

1) iter() 사용

iterator = iter(numbers)

리스트 numbers를 반복자로 변환한다.
이제 next()를 사용해 데이터를 하나씩 가져올 수 있다.

2) next() 사용

next(iterator)

현재 위치에서 다음 요소를 반환하고,
반복자의 위치를 다음 요소로 이동시킨다.

3) 반복이 끝났을 때

반복자에 더 이상 가져올 데이터가 없으면
StopIteration 오류가 발생한다.

for문은 이 상황을 자동으로 처리하기 때문에
일반적으로 반복자를 사용할 때는 for문을 많이 활용한다.

    복습하면서 알게 된 점

반복 가능한 객체와 반복자는 서로 다른 개념이라는 것을 알게 되었다.

리스트는 여러 데이터를 저장하고 있는 반복 가능한 객체이고,
반복자는 그 데이터에서 값을 하나씩 가져오는 역할을 한다.

또한 iter()로 반복자를 만들고 next()를 실행할 때마다
다음 요소로 이동한다는 점을 이해했다.

📌 AI 활용 복습 문제

1) 반복자란 무엇인가?

정답: 데이터를 한 번에 가져오는 것이 아니라
필요할 때마다 다음 요소를 하나씩 반환하는 객체이다.

2) 반복 가능한 객체를 반복자로 변환하는 함수는?

정답: iter()

3) 반복자에서 다음 요소를 가져오는 함수는?

정답: next()

4) 반복자에 더 이상 가져올 요소가 없으면 어떤 오류가 발생할까?

정답: StopIteration

5) 다음 코드의 실행 결과는?

numbers = [5, 10, 15]
iterator = iter(numbers)

print(next(iterator))
print(next(iterator))

정답:
5
10

6) for문은 반복자가 끝났을 때 발생하는 상황을 어떻게 처리할까?

정답: StopIteration을 자동으로 처리하고 반복을 종료한다.
'''
