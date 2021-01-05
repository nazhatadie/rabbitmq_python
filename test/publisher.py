from rabbitmq_py.rabbitmq_publisher import Publisher


def main():
    publisher = Publisher(
        exchange_name="",
        queue_name="webtest_privacyReport",
        routing_key="webtest_privacyReport",
        host="192.168.3.80",
        username="admin",
        password="admin",
        exchange_type='direct',
        queue_args={"x-max-priority": 3}

    )
    # 生产者发送消息
    publisher.publish({"app_id": "565"})


if __name__ == '__main__':
    main()
