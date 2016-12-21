### in2csv
- 엑셀과 관련한 행들을 전부 삭제 해 준다.
- ```in2csv INPUT.xlsx > OUTPUT.csv```

### csvlook
- 데이터를 터미널에서 표의 형태로 출력해준다.

### csvcut
- csv 파일의 열을 자르거나, 삭제하거나, 재정렬한다.

### pipe
- symbol : |
- 둘 이상의 명령으를 함께 묶어 출력의 결과를 다른 프로그램의 입력으로 전환하는 기능
- 프로그램 1 | 프로그램 2 | 프로그램 3
  - 프로그램 1의 결과물은 프로그램 2의 입력값으로 전환된다.
  - 프로그램 2의 결과물은 프로그램 3의 입력값으로 전환된다.

### csvstat
- 코드 없이 통계치를 내준다.
- 명령어를 통해 나오는 정보는 다음과 같다.
  - 데이터 타입.
  - 유니크한 정보.
  - 내림차순으로, 가장 많이 나온 데이터 5개.

### csvsort
- 선택된 열의 데이터를 (기본)오름차순으로 정렬해준다.
- 내림 차순으로 정렬을 하고 싶을 때는 -r 옵션을 붙여준다.

### csvjoin
- 2개의 csv 파일에서 공통되는 열을 기준으로 파일을 합친다.
- ```csvjoin -c fips data.csv acs2012_5yr_population.csv```

### csvstack
- 데이터의 열이 같은 2개의 파일을 묶어준다.(aggregate)
- ```csvstack A.csv B.csv > RESULT.csv```

### flags
- -c COLUMN_NAME
- -m STRING_WHICH_WANT_TO_MATH
- -g GROUPING
  - grouping column to each row. 
