from confluent_kafka import Producer

producer = Producer({
    "bootstrap.servers":"localhost:9092"
})

for i in range(10):

    producer.produce(
        "orders",
        key=f"user{i%3}",
        value=f"Order {i}"
    )

producer.flush()