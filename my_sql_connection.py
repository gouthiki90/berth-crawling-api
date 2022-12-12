# STEP 1
import pymysql
import pymysql.cursors

try:
    # STEP 2: MySQL Connection 연결
    con = pymysql.connect(host='13.125.119.4', user='insystem', password='insystem12!@',
                          db='ship_schedule', charset='utf8', cursorclass=pymysql.cursors.DictCursor)

    # STEP 4: SQL문 실행 및 Fetch

    def select_all(trminlCode):
        try:
            cur = con.cursor()  # cursor 생성
            sql = "SELECT * FROM ship_schedule.berthStat_schedule WHERE TRUE AND trminlCode = '{}'".format(
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
            sql = "SELECT * FROM ship_schedule.berthStat_schedule WHERE trminlCode IN ('{}', '{}', '{}', '{}')".format(
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
            sql = "SELECT * FROM ship_schedule.berthStat_schedule WHERE trminlCode IN ('HKT', 'DPCT', 'BPTG', 'BNMT', 'BPTS', 'BNCT', 'HPNT', 'HJNC', 'PNC', 'PNIT')"
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

    def select_container():
        try:
            cur = con.cursor()
            sql = "SELECT CNTR_NO FROM ship_schedule.container WHERE CNTR_STATUS NOT IN('78', '59') GROUP BY CNTR_NO ORDER BY STATUS_DT ASC"
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

    def upsert_container(STATUS_DT, STATUS_NM, CNTR_STATUS, STATUS_TM, container_status):
        try:
            cur = con.cursor()
            sql = f"INSERT INTO ship_schedule.container (STATUS_DT, STATUS_NM, CNTR_STATUS, STATUS_TM, container_status) VALUES ('{STATUS_DT}', '{STATUS_NM}', '{CNTR_STATUS}', '{STATUS_TM}', {container_status}) ON DUPLICATE KEY UPDATE STATUS_DT = '{STATUS_DT}', STATUS_NM = '{STATUS_NM}', CNTR_STATUS = '{CNTR_STATUS}', STATUS_TM = '{STATUS_TM}', container_status = {container_status}"
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
