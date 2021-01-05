from rabbitmq_py.rabbitmq_consumer import Consumer
import time


def callback(data):
    print(data)
    print(f"Received {data}!")


def main():
    # 初始化消费者
    consumer = Consumer(
        exchange_name="",
        queue_name="webtest_privacyReport",
        routing_key="webtest_privacyReport",
        host="192.168.3.80",
        username="admin",
        password="admin",
        callback=callback,
        queue_args={"x-max-priority": 3}

    )
    # 消费者  开启一个守护线性去消费消息
    consumer.start()
    while True:
        time.sleep(1)


if __name__ == '__main__':
    main()
