# coding: utf-8
from .db import Hub
import pymysql

db = Hub(pymysql)


db_config = {
    "test": dict(
                host="host_name",
                port=3306,
                user="root",
                passwd="xxx.",
                db="db_name",
    ),
}

for alias, config in db_config.items():
    db.add_pool(
        alias,
        host=config['host'],
        port=config['port'],
        user=config['user'],
        passwd=config['passwd'],
        db=config['db'],
        charset='utf8',
        autocommit=True,
        pool_size=16,
        wait_timeout=29
    )
