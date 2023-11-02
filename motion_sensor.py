import paho.mqtt.client as mqtt
print("Motion Sensor is listening....")

# Define the MQTT broker address
MQTT_BROKER_ADDRESS = "localhost"

# Create an MQTT client
client = mqtt.Client()

# Connect to the MQTT broker
client.connect(MQTT_BROKER_ADDRESS)

# Subscribe to the topic for the motion sensor motion detected sensor
client.subscribe("motion_sensor/motion_detected")

# Define a callback function for the topic
def on_message(client, userdata, msg):
  value = msg.payload.decode()
  topic = msg.topic

  # Handle the message based on the topic
  motion_detected = value
  if motion_detected == "True":
    # Turn on the lights
    print("Turning on lights")
client.on_message = on_message

# Start the MQTT loop
client.loop_forever()
