### 문제
[3169. Count Days Without Meetings](https://leetcode.com/problems/count-days-without-meetings/description/)
### 아이디어
초기 아이디어는 days의 크기만큼의 array를 할당하여 입력되는 meetings의 크기만큼 array로 확인하여 하려함.
이 아이디어는 공간복잡도 O($n$), 시간복잡도 O($n^2$)으로 효과적이지 않아 아이디어를 변경하였다.

meetings의 날짜가 중복되는 부분을 합쳐 meetings를 간소화 하여 날짜를 계산하는 로직으로 변경하였다. 이 경우 for문 내부 sort의 경우 O($nlogn$)이지만 2개의 항목만 비교하기에 O(1)이 된다. 그리고 코드 상단 sort의 경우를 확인하면 O($nlogn$)이 시간복잡도로 정해지게 된다
### 반성
list를 for문을 이용하여 접근할 경우 참조 접근이 아닌 복사 접근이라 직접 수정이 불가하다.