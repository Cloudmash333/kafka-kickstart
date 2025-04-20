To start run
pip install kafka-python
docker-compose up -d

Make sure Docker is running Kafka (docker-compose up -d).

Start the consumer:
python consumer.py

Then run the producer in a separate terminal:
python producer.py

Optional 
You can check Kafka logs using:
docker-compose logs kafka

To list topics:
docker exec -it <kafka-container-id> kafka-topics --list --bootstrap-server localhost:9092
