from kafka import KafkaProducer
import time

producer = KafkaProducer(bootstrap_servers='localhost:9092')

for i in range(10):
    message = f"Hello Kafka {i}"
    producer.send('test-topic', message.encode('utf-8'))
    print(f"Sent: {message}")
    time.sleep(1)

producer.close()

