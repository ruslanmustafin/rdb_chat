import rethinkdb as r
import config as cfg

MESSAGES_TABLE = 'messages'

def main():
    conn = r.connect(host=cfg.HOST, port=cfg.PORT)
    r.db_create(cfg.DB).run(conn)
    r.db(cfg.DB).table_create(cfg.MESSAGES_TABLE).run(conn)

    print('DONE')

if __name__ == '__main__':
    main()
