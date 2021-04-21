import dotenv
from dotenv.main import dotenv_values
import fdb
from fdb.fbcore import DatabaseError
from lojas_ips import hosts
from dotenv import load_dotenv

load_dotenv()

CONFIG = dotenv_values(".env")

def executar_consulta() -> list:
    __script = """
   SELECT TCPIPTEFDLL
        , IPSRVWEB
        , IPSRVRET
        , CPCTCP
     FROM CONFIGPDV      
    INNER JOIN CONF_PAGUECONTAS ON 1=1
    """
    __database = r"C:\Syspdv\syspdv_srv.fdb"
    __user = CONFIG['db_user']
    __password = CONFIG['db_pass']
    resultado = list()

    for cod_loja in hosts:
        try:
            with fdb.connect(
                host=hosts[cod_loja],
                database=__database,
                user=__user,
                password=__password,
            ) as con:
                cur = con.cursor()
                cur.execute(__script)

                resultado.append(cod_loja)
                resultado.append(cur.fetchall())
        except:
            resultado.append(cod_loja)
            resultado.append(False)

    return resultado


a = executar_consulta()
print(a)