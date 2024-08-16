import time
from threading import Thread


def wite_words(word_count,file_name):
    with open(file_name, 'w+', encoding='utf8') as f:
        for i in range(word_count):
            f.write(f'Какое-то слово № { i + 1}\n' )
            time.sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")


if __name__ == '__main__':
    start_time = time.time()
    wite_words(10,"exemple1.txt")
    wite_words(30, "exemple2.txt")
    wite_words(200, "exemple3.txt")
    wite_words(100, "exemple4.txt")
    end_time = time.time()
    duration = end_time - start_time
    print(f'Время выполнения: {duration} секунд')
    start_time_2 = time.time()
    p1 = Thread(target=wite_words, args=(10, 'example5.txt'))
    p2 = Thread(target=wite_words, args=(30, 'example6.txt'))
    p3 = Thread(target=wite_words, args=(200, 'example7.txt'))
    p4 = Thread(target=wite_words, args=(100, 'example8.txt'))

    p1.start()
    p2.start()
    p3.start()
    p4.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()

    end_time_2 = time.time()
    duration_2 = end_time_2 - start_time_2
    print(f'Время выполнения с использованием потоков: {duration_2} секунд')


