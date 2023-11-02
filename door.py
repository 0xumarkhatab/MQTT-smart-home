import paho.mqtt.client as mqtt
print("Door is listening....")

# Define the MQTT broker address
MQTT_BROKER_ADDRESS = "localhost"

# Create an MQTT client
client = mqtt.Client()

# Connect to the MQTT broker
client.connect(MQTT_BROKER_ADDRESS)

# Subscribe to the topic for the door status sensor
client.subscribe("door/status")

# Define a callback function for the topic
def on_message(client, userdata, msg):
  value = msg.payload.decode()
  topic = msg.topic

  # Handle the message based on the topic
  door_status = value
  if door_status == "open":
    # Send a notification to the user
    print("Sending notification to user: Door is open")
client.on_message = on_message

# Start the MQTT loop
client.loop_forever()
