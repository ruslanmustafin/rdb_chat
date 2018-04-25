import rethinkdb as r
import queue
import threading
import config as cfg

NAME_KEY = 'name'
MESSAGE_KEY = 'message'

messages = []

def event_listener():
    conn = r.connect(host=cfg.HOST, port=cfg.PORT, db=cfg.DB)
    feed = r.table(cfg.MESSAGES_TABLE).changes().run(conn)

    for item in feed:
        messages.append(str(item))
        print('\r{}:{}'.format(item['new_val'][NAME_KEY], item['new_val'][MESSAGE_KEY]))

def main():
    name = input('Your name:')

    event_thread = threading.Thread(target=event_listener)
    event_thread.start()

    conn = r.connect(host=cfg.HOST, port=cfg.PORT, db=cfg.DB)

    while True:
        msg = input('>:')
        r.table(cfg.MESSAGES_TABLE).insert({ NAME_KEY: name, MESSAGE_KEY: msg}).run(conn)


if __name__ == '__main__':
    main()
