import paho.mqtt.client as mqtt

# Create an MQTT client
client = mqtt.Client()

# Connect to the MQTT broker
client.connect("localhost", 1883)

# Subscribe to the temperature topic
client.subscribe("temperature")

# Define a callback function for when a message is received
def on_message(client, userdata, msg):
    print("Temperature:", msg.payload.decode())

# Set the callback function
client.on_message = on_message

# Start the MQTT loop
client.loop_forever()
