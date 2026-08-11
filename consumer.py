from confluent_kafka import Consumer

consumer = Consumer({

    "bootstrap.servers":"localhost:9092",

    "group.id":"order-workers",

    "auto.offset.reset":"earliest"

})

consumer.subscribe(["orders"])

while True:

    msg = consumer.poll(1)

    if msg is None:
        continue

    print(msg.key().decode(), msg.value().decode())