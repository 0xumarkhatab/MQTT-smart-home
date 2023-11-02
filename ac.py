import paho.mqtt.client as mqtt
print("AC is listening....")
# Define the MQTT broker address
MQTT_BROKER_ADDRESS = "localhost"

# Create an MQTT client
client = mqtt.Client()

# Connect to the MQTT broker
client.connect(MQTT_BROKER_ADDRESS)

# Subscribe to the topic for this file
# For example, the file for the AC temperature sensor would subscribe to the topic "ac/temperature"
client.subscribe("ac/temperature")

# Define a callback function for the topic
def on_message(client, userdata, msg):
  value = msg.payload.decode()
  topic = msg.topic
#   print("topic is ",topic,value)
  # Handle the message based on the topic
  if topic == "ac/temperature":
    temperature = float(value)
    if temperature < 20:
      # Shut down the AC
      print("Shutting down AC")
client.on_message = on_message

  # Start the MQTT loop
client.loop_forever()