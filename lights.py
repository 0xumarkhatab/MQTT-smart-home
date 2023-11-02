import paho.mqtt.client as mqtt
print("Lights are listening....")

# Define the MQTT broker address
MQTT_BROKER_ADDRESS = "localhost"

# Create an MQTT client
client = mqtt.Client()

# Connect to the MQTT broker
client.connect(MQTT_BROKER_ADDRESS)

# Subscribe to the topic for the light ambient light level sensor
client.subscribe("light/ambient_light_level")

# Define a callback function for the topic
def on_message(client, userdata, msg):
  value = msg.payload.decode()
  topic = msg.topic

  # Handle the message based on the topic
  ambient_light_level = float(value)
  if ambient_light_level > 50:
    # Turn off the lights
    print("Turning off lights")
client.on_message = on_message

# Start the MQTT loop
client.loop_forever()
