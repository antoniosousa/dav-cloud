import fdb
from dotenv import load_dotenv
from dotenv.main import dotenv_values

from app.lojas_ips import hosts

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
    __database = CONFIG["db_path"]
    __user = CONFIG["db_user"]
    __password = CONFIG["db_pass"]
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

                for (sitef, syspdvweb, crm, vale_gas) in cur:
                    resultado.append([cod_loja, sitef, syspdvweb, crm, vale_gas])
        except:
            resultado.append([cod_loja, None, None, None, None])

    return resultado
