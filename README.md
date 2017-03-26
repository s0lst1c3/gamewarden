gamewarden
==========

Description here. What do this do, how does it do it, etc.

Usage Instructions
------------------

GameWarden is designed to be used in the manner outlined in the following steps.

1. Configure the GameWarden device
2. Connect the GameWarden device to a power soure
3. Press the Blue button to enable GameWarden's packet sniffer
4. If you've configured GameWarden to enable its access point on a schedule, skip to step 5. Otherwise, hit the red button to enable its built-in access point. 
5. Conceal the GameWarden device near a door or other entry point.
6. When you're ready to exfiltrate data from the GameWarden device, connect to its built-in AP and use the gw-analyzer script to exfiltrate and analyze the data.

For detailed instructions on how to complete each of the following steps, please refer to the appropriate section below.

\1. Configuring the GameWarden device
------------------------------------

If this is your first time configuring and running GameWarden, please complete the _First Time Setup_ guide before proceeding with this section.

Begin by using SSH to connect to your GameWarden device. Then run setup.py to reinitialize GameWarden's databases. Note that this will delete any previously saved entries in your GameWarden databases, so make backups if you want to keep your previous work.

	python setup.py

Next, decide whether you want to run GameWarden's access point on a schedule or run it continuously. Running GameWarden's access point on a schedule is recommeneded for two reasons:

1. It's stealthier
2. It conserves battery life

If you're planning on running the AP on a schedule, use the following command to launch the scheduler's setup wizard. Then follow the prompts.

	./gamewarden --set-schedule

Once you've configured the scheduler (or decided not to), proceed to configuring GameWarden's builtin access point using the following command. GameWarden will provide you with an easy to use wizard, so just enter in desired config values as prompted.

	./gamewarden --ap-config

Your GameWarden device should now be configured and ready to use.

2. Connect the GameWarden device to a power source
--------------------------------------------------

GameWarden can be run off of a variety of different power sources. Just make sure that whatever you're plugging it into can connect to its microusb power port. We recommend using something like a [Mophie battery](http://www.mophie.com/) for situations in which a power outlet isn't available 9. Otherwise, plug it into a concealed power outlet and adorn it with a label stating "Do not touch. -IT". 

3. Enable GameWarden's packet sniffer
-------------------------------------

To enable GameWarden's packet sniffer, use the blue button attached to the side of the device.

4. Conceal the GameWarden device
--------------------------------

GameWarden should be concealed in a location that will not interfere with wireless reception and where it won't become a fire hazard.

5. Manually Enabling GameWarden's AP
------------------------------------

To manually enable GameWarden's AP, press the red button attached to the side of the device. 

6. Exfiltrating and Analyzing Data From GameWarden
--------------------------------------------------

To exfiltrate and analyze data from the GameWarden device, first connect to its built-in access point. Then run following
command. 

	./gw-analyzer --retrieve

Then use the following command to analyze and the results. 

	./gw-analyzer --analyze --show

The resulting PNG file will be stored in your gamewarden/png-stash directory.

You can also combine the last two commands as follows:

	./gw-analyzer --analyze --show --retrieve

The following options are also included:

- --db-file
- --db-stash
- --output
- --remote-install-path
- --collector-ip

Run the following command if you want to learn more about them.

	./gw-analyzer -h

Setup Instructions
------------------

Gamewarden is intended to be installed on a Raspberry Pi microcontroller running Raspbien-Lite. The gw-listener script targets _Python 3.3_. All other Python code targets _Python 2.7_.

Python dependencies are listed in `pip.req`. Binary dependencies are listed in `dependencies.txt`.
