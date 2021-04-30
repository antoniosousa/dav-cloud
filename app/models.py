import socket

import fdb
from dotenv import load_dotenv
from dotenv.main import dotenv_values

from app import db
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

class Url(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), index=True, unique=True)
    ip_atual = db.Column(db.String(15), index=True)
    ip_novo = db.Column(db.String(15), index=True)
    ip_que_deve_ser = db.Column(db.String(15), index=True)

    def __repr__(self):
        return f'<Url {self.nome}>'

    def atualizar_ip_atual(self):
        try:
            ip = socket.gethostbyname(self.nome)
            self.ip_atual = ip
        except socket.gaierror:
            self.ip_atual = None

    def atualizar_ip_novo(self):
        try:
            ip = socket.gethostbyname(self.nome)
            if self.ip_atual != ip:
                self.ip_novo = ip
        except socket.gaierror:
            self.ip_novo = None