import blog_spider
import time
import threading


def single_thread():
    for url in blog_spider.urls:
        blog_spider.craw(url)


def multi_thread():
    threads = []
    for url in blog_spider.urls:
        threads.append(
            threading.Thread(target=blog_spider.craw, args=(url,)))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == '__main__':
    start_time = time.time()
    single_thread()
    end_time = time.time()
    print('single_thread time', end_time - start_time, 'seconds')

    start_time = time.time()
    multi_thread()
    end_time = time.time()
    print('multi_thread time', end_time - start_time, 'seconds')