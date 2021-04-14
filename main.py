import logging
import requests

logging.basicConfig(level=logging.WARNING,
                    filename='logfile.log',
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')


def foo(url):
    # print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    logging.info(f'Пытаемся открыть url={url}')
    result = requests.get(url)
    logging.info(f'Результат ответе код {result.status_code}')


if __name__ == '__main__':
    foo('https://ya.ru')

