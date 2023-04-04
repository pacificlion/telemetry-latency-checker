# Latency between two radios

To check the latency between two SiK Telemetry Radio v3 modules on an Ubuntu system, you need to set up and connect the telemetry radios. Here's a step-by-step guide:

1. Connect the telemetry radios: Connect one of the SiK Telemetry Radio modules to your drone/autopilot system and the other one to your Ubuntu computer using a USB cable.
2. For my experiment I used two different ubuntu machines
3. Install the required software: Make sure you have the 'screen' utility and 'python' installed on your Ubuntu system. You can install them by running the following commands:

```bash
sudo apt update
sudo apt install screen python

```

1. Find the telemetry radio devices: Run the following command to list all connected devices:

```bash
ls /dev/ttyUSB*

```

This command will show you the names of connected devices, such as **`/dev/ttyUSB0`** and **`/dev/ttyUSB1`**. One of these should be your telemetry radio connected to your computer.

1. Configure the radios: Make sure both radios are set up to communicate on the same frequency and settings. You can use the Mission Planner software on Windows or the APM Planner software on Ubuntu to do this.
2. Connect to the telemetry radio: Use the 'screen' command to establish a connection with the telemetry radio. Replace **`/dev/ttyUSB0`** with the name of your device if it's different:

[SiK Radio Integration | PX4 User Guide](https://docs.px4.io/main/en/data_links/sik_radio.html)

```bash
screen /dev/ttyUSB0 57600

screen /dev/ttyUSB0 57600 8N1
# netid (radio channel) should be same to send/receive data
```

The number '57600' is the default baud rate for SiK Telemetry Radios. If you have set a different baud rate, use that number instead.

- [x]  Test the connection: If your radios are connected and configured correctly, you should start seeing data being transmitted between the drone/autopilot and your Ubuntu computer.
    
    Remember that latency may vary depending on the environment and the distance between the two radios. Additionally, SiK telemetry radios are designed for long-range communication and may have higher latency compared to Wi-Fi or Ethernet connections.
    
    ## Code
    
    Link: [https://github.com/pacificlion/telemetry-latency-checker](https://github.com/pacificlion/telemetry-latency-checker)
    
    Able to send one message from one pc to other PC
    

- [x]  using same pc but different usb ports (2 radios close to 10 cm). Not much difference when distance was extended to 100 cm

- [x]  Measure latency by sending data and check bytes send and received.

| Payload (bytes) | Average latency (ms) |
| --- | --- |
| 128 | 97 |
| 220 | 125 |
| 1120 | 300 |
| 10120 | 894 |

## TODOS
- [ ]  check low latency mode