import json
import time
import random
import paho.mqtt.client as mqtt

student_name = "Reddi Satyanarayana"
unique_id = "42614109"
topic = "home/reddisatyanarayana-2025/sensor"

broker = "10.43.29.10"
port = 1883

def main():
    client = mqtt.Client(protocol=mqtt.MQTTv311)

    print(f"Connecting to MQTT broker at {broker}:{port} ...")
    client.connect(broker, port, 60)
    client.loop_start()
    print("Connected. Publishing data every 5 seconds...")
    print(f"Using topic: {topic}")

    while True:
        temperature = round(random.uniform(24.0, 30.0), 1)
        humidity = round(random.uniform(40.0, 70.0), 1)
        gas = random.randint(0, 100)  # gas level

        payload = {
            "student_name": student_name,
            "unique_id": unique_id,
            "temperature": temperature,
            "humidity": humidity,
            "gas": gas
        }

        client.publish(topic, json.dumps(payload))
        print(f"Published to {topic}: {payload}")
        time.sleep(5)

if __name__ == "__main__":
    main()
