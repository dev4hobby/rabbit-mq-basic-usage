# RabbitMQ Examples

## Usage

### Start RabbitMQ

```bash
docker-compose up -d
```

### Basic: send and receive

Consumers connected to a single message queue receive messages in a round-robin fashion.

```bash
# terminal 1
python basic_sender.py

# terminal 2
python basic_receiver.py

# terminal 3
python basic_receiver.py
```

### Fanout: send and receive

When using a fanout type exchange, all consumers receive the same messages.

```bash
# terminal 1
python fanout_sender.py

# terminal 2
python fanout_receiver.py

# terminal 3
python fanout_receiver.py
```
