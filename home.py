import paho.mqtt.client as mqtt

print("Home is listening....")
# Define the MQTT broker address
MQTT_BROKER_ADDRESS = "localhost"

# Create an MQTT client
client = mqtt.Client()

# Connect to the MQTT broker
client.connect(MQTT_BROKER_ADDRESS)

# Subscribe to the topics for each device
client.subscribe("ac/temperature")
client.subscribe("light/ambient_light_level")
client.subscribe("door/status")
client.subscribe("smoke_detector/smoke_level")
client.subscribe("motion_sensor/motion_detected")

# Define callback functions for each topic
def on_message(client, userdata, msg):
  topic = msg.topic
  value = msg.payload.decode()

  print(f"Received message on topic {topic}: {value}")

  # Handle the message based on the topic
  if topic == "ac/temperature":
    temperature = float(value)
    if temperature < 20:
      # Shut down the AC
      print("Shutting down AC")

  elif topic == "light/ambient_light_level":
    ambient_light_level = float(value)
    if ambient_light_level > 50:
      # Turn off the lights
      print("Turning off lights")

  elif topic == "door/status":
    door_status = value
    if door_status == "open":
      # Send a notification to the user
      print("Sending notification to user: Door is open")

  elif topic == "smoke_detector/smoke_level":
    smoke_level = float(value)
    if smoke_level > 100:
      # Trigger an alarm
      print("Triggering alarm: Smoke detected")

  elif topic == "motion_sensor/motion_detected":
    motion_detected = value
    if motion_detected == "True":
      # Turn on the lights
      print("Turning on lights")

client.on_message = on_message

# Start the MQTT loop
client.loop_forever()