# STEP 1
import pymysql
import pymysql.cursors

try:
    # STEP 2: MySQL Connection 연결
    con = pymysql.connect(host='localhost', user='insystem', password='Insystem12!@)()',
                          db='hang_man', charset='utf8', cursorclass=pymysql.cursors.DictCursor)

    # STEP 4: SQL문 실행 및 Fetch

    def select_all(trminlCode):
        try:
            cur = con.cursor()  # cursor 생성
            sql = "SELECT * FROM hang_man.berthStat_schedule WHERE TRUE AND trminlCode = '{}'".format(
                trminlCode)
            print(sql)
            # 데이타 Fetch
            cur.execute(sql)
            # con.close()  # close 후에 rows 얻을 수 있음
            rows = cur.fetchall()
            return rows
        except Exception as e:
            print(e)
            cur.close()
        finally:
            cur.close()

    def select_incheon_all(hjit, snct, e1ct, ict):
        try:
            cur = con.cursor()
            sql = "SELECT * FROM hang_man.berthStat_schedule WHERE trminlCode IN ('{}', '{}', '{}', '{}')".format(
                hjit, snct, e1ct, ict)
            print(sql)
            cur.execute(sql)
            # con.close()
            rows = cur.fetchall()
            return rows
        except Exception as e:
            print(e)
            cur.close()
        finally:
            cur.close()

    def select_busan_all():
        try:
            cur = con.cursor()
            sql = "SELECT * FROM hang_man.berthStat_schedule WHERE trminlCode IN ('HKT', 'DPCT', 'BPTG', 'BNMT', 'BPTS', 'BNCT', 'HPNT', 'HJNC', 'PNC', 'PNIT')"
            print(sql)
            cur.execute(sql)
            # con.close()
            rows = cur.fetchall()
            return rows
        except Exception as e:
            print(e)
            cur.close()
        finally:
            cur.close()

    def insert_container(container_status, STATUS_DT, STATUS_NM, CNTR_STATUS, STATUS_TM, id):
        try:
            cur = con.cursor()
            sql = "UPDATE hang_man.container SET container_status = {} AND SET STATUS_DT = {} AND SET STATUS_NM = {} AND SET CNTR_STATUS = {} AND SET STATUS_TM = {} WHERE id = {}".format(
                container_status, STATUS_DT, STATUS_NM, CNTR_STATUS, STATUS_TM, id)
            print(sql)
            cur.execute(sql)
            # con.close()
            rows = cur.fetchall()
            return rows
        except Exception as e:
            print(e)
            cur.close()
        finally:
            cur.close()

except Exception as e:
    print(e)
