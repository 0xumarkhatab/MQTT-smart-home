import paho.mqtt.client as mqtt
print("Smoke Detector is listening....")

# Define the MQTT broker address
MQTT_BROKER_ADDRESS = "localhost"

# Create an MQTT client
client = mqtt.Client()

# Connect to the MQTT broker
client.connect(MQTT_BROKER_ADDRESS)

# Subscribe to the topic for the smoke detector smoke level sensor
client.subscribe("smoke_detector/smoke_level")

# Define a callback function for the topic
def on_message(client, userdata, msg):
  value = msg.payload.decode()
  topic = msg.topic
  # Handle the message based on the topic
  smoke_level = float(value)
  if smoke_level > 100:
    # Trigger an alarm
    print("Triggering alarm: Smoke detected")
client.on_message = on_message

# Start the MQTT loop
client.loop_forever()
