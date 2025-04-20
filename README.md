# Quickstart

```bash
pip install kafka-python
```

```bash
docker-compose up -d
```

Make sure Docker is running Kafka (docker-compose up -d).

Start the consumer:

```bash
python consumer.py
```

Then run the producer in a separate terminal:

```bash
python producer.py
```

## Optional 
You can check Kafka logs using:

```bash
docker-compose logs kafka
```

To list topics:

```bash
docker exec -it <kafka-container-id> kafka-topics --list --bootstrap-server localhost:9092
```

## How to Stop Kafka + Zookeeper Containers

Since you're using Docker Compose, the clean way is:

```bash
docker-compose down
```

What this does:
Stops all containers defined in your docker-compose.yml.

Removes the containers (but not the images, volumes, or networks unless specified).

If you just want to stop them without removing, use:

```bash
docker-compose stop
```

## 🔄 How to Start / Restart

## ✅ To start again after down:

```bash
docker-compose up -d
```

It will recreate the containers and start them in detached mode.

## 🔁 To restart (like a reboot):

```bash
docker-compose restart
```

This is useful if you changed some environment variables or configs in the YAML and want to restart without stopping everything manually.

## License
 
The MIT License (MIT)

Copyright (c) 2015 Chris Kibble

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
