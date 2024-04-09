# Code by Caleb Stewart, Robert Longo, and Caitlin Swift.
# Bot icon by @GLITTERGVTS on Twitter
# Supporting Guides + Code:
# Michael Sklar, "Analog Inputs for Raspberry Pi Using the MCP3008": https://learn.adafruit.com/reading-a-analog-in-and-controlling-audio-volume-with-the-raspberry-pi?view=all
# Lady Ada, "Basic Photocell Reading": https://learn.adafruit.com/basic-resistor-sensor-reading-on-raspberry-pi/basic-photocell-reading
# Frederic, "DHT11 temperature and humidity sensor on Raspberry Pi": https://www.freva.com/dht11-temperature-and-humidity-sensor-on-raspberry-pi/


from digitalio import DigitalInOut, Direction
from dotenv import load_dotenv
import time
import board
import adafruit_dht
import psutil
import os
import discord


#Discord
intents = discord.Intents.all()
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected!')

@client.event
async def on_message(message):
    #If message is from this bot, do nothing
    if message.author == client.user:
        return

    #Water Sensor
    if '/water' in message.content.lower():
        waterSensor = board.D12
        with DigitalInOut(waterSensor) as ws:
            print("Water: " + str(ws.value))
            if ws.value == False:
                await message.channel.send("No water detected.")
                return
            await message.channel.send("Water detected!")
        return

    #Temp Sensor
    if '/temp' in message.content.lower():
        try:
            tempSensor = adafruit_dht.DHT11(board.D23)
            temp = (tempSensor.temperature) * (9/5) + 32
            humidity = tempSensor.humidity
            await message.channel.send("Temperature: " + str(temp) + "°F")
            await message.channel.send("Humidity: " + str(humidity) + "%")
            print("Temp: " + str(temp) + "\nHumidity: " + str(humidity))
            return
        except RuntimeError as error:
            print(error)
            await message.channel.send("Sensor Error: " + error.args[0])
            time.sleep(0.5)
        except Exception as error:
            tempSensor.exit()
            print(error)
            await message.channel.send("Sensor Error: " + error.args[0])
            raise error
            return
        return

    #Light Sensor
    if '/light' in message.content.lower():
        lightSensor = board.D25
        # BASED ON CODE BY LADY ADA
        with DigitalInOut(lightSensor) as ls:
            reading = 0
            # setup pin as output and direction low value
            ls.direction = Direction.OUTPUT
            ls.value = False
            time.sleep(0.1)

            # setup pin as input and wait for low value
            ls.direction = Direction.INPUT

            # This takes about 1 millisecond per loop cycle
            light = True
            while ls.value is False:
                reading += 1
                if reading > 100:
                    light = False
                    break
            if light:
                level = 100 - reading
                await message.channel.send("Light detected! Light level = " + str(level) + "%!")
                print("Light: " + str(level) + "%")
            else:
                await message.channel.send("Low light detected.")
                print("Low Light")
            return


    if '/' in message.content.lower():
        await message.channel.send("Please use one of the following commands: \n/light\n/water\n/temp\n")
        return


client.run(str(TOKEN))
