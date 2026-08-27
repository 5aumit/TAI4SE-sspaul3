# 데이터베이스 연동(SQLite)
# 테이블 생성 및 삽입

# pkg 폴더안에 db 파일이 있어서 해당 파일 import 하기 위해 ... 다른 방법 없을까 ...
import os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

# db 정보 import 후 DbConn 메소드를 dbConn으로 사용명 변경
from pkg._DB_INFO import DbConn as dbConn
from pkg._DB_INFO import sysDate as nowDate

# doConn에 Cursor(커서) 연결 
# print('--->  ', dir(dbConn())) # sqlite3.connect()에서 사용가능 메소드
c = dbConn().cursor()
nowDateTime = nowDate()
print('Cursor Type : ', type(c))

# 테이블 생성(Data Type : Text. Numeric, Integer, Real, Blob)
# CREATE TABLE IF NOT EXISTS --> 있으면 그대로 사용하고 없으면 테이블 생성
# PRIMARY KEY -> 기본 키, 중복 불가
c.execute('CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username text, \
email text, phone text, website text, regdate text)')

# ID는 PRIMARY KEY라서 중복 불가
# INSERT 쿼리 한번 실행 후 주석 처리

# 데이터 삽입
c.execute("INSERT INTO users \
	VALUES(1, 'kang', 'abcdefg@aaa.com', '010-0000-0000', 'kang.com', ?)",
	(nowDateTime, ) ) # ? 뒤에 (, ) 안에 ,가 없으면 문자가 시퀀스 처리됨

# 다른 당법으로 데이터 삽입
c.execute('INSERT INTO users(id, username, email, phone, website, regdate) \
	VALUES(?,?, ?, ?, ?, ?)',
	(2, 'Park', 'Park@aaa.aaa', '010-0000-0001', 'Park.com', nowDateTime) )

# Many INSERT (대용량 삽입) -> 튜플, 리스트 (둘은 괄호만 바꾸면 된다)
userList = (
	(3, 'Lee', 'Lee@Lee.com', '010-1111-1111', 'Lee.com', nowDateTime),
	(4, 'Lee', 'Cho@Cho.com', '010-2222-2222', 'Cho.com', nowDateTime),
	(5, 'Yoo', 'Yoo@Yoo.com', '010-4444-4444', 'Yoo.com', nowDateTime)
)
# 튜플 형태로 한번에 집어 넣기 --> 나중 크롤링 한 정보를 입력할 때 도움 됨
c.executemany("INSERT INTO users(id, username, email, phone, website, regdate)\
	VALUES (?,?,?,?,?,?)", userList)

# 테이블 데이터 삭제
# c.execute('DELETE FROM users')
# 지우면서 print 함수로 몇개의 row를 지웠는지 확인 하는법
# print('users db delete : ', c.execute("DELETE FROM users").rowcount)

# 커밋 : isolation_level = None 일 경우 자동 반영 (오토 커밋)
# dbConn().commit()  # 오토 커밋을 안했을 경우 직접 커밋을 해줘야 된다
# 롤백 : 롤백이 실행된 시점 기준으로 그 전 쿼리들을 실행 안하고 전으로 돌림
# dbConn().rollback()

# 접속 해제
dbConn().close()

# c.execute('DROP TABLE users') # 테이블 삭제



