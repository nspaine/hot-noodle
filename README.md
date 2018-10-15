# hot-noodle
We built an IoT WiFi-enabled smart pool sensor that texts you to alert you of different features (e.g. hot tub temperature)! It can float aimlessly or move around on its own with a 3D-printed propeller! Built as part of a hackathon project at HackUMass VI and winner of the MLH DragonBoard competition!

*For a detailed overview of our project check our [Visual Step-by-Step Guide!](https://github.com/nspaine/hot-noodle/blob/master/Visual%20Step-by-Step%20Guide.pdf)*

# Who made this amazing Hack?
Nigel Paine ([LinkedIn](https://www.linkedin.com/in/nigel-paine/)) - CSE '18 UMass Amherst

Jakub Polanowski ([GitLab](https://gitlab.com/JakubPol)) - Chem '20 UMass Amherst

Zenry Padua - Informatics '21 UMass Amherst

# What inspired us to make this?
One of our teammates' fathers owns a pool business and the idea came from observing his clients who constantly have to be aware of chemical inbalances and other features in their pool. We decided instead of having people constantly check their pools, they could just get notified directly via an IoT smart pool device that floats around the pool or hottub.

# What does our project do?
Sends you an SMS text message via WiFi from an onboard sensor suite that floats around in your pool. The sensors can tell you different things but the main use case we built was a hot tub "readiness" alert system.

# How did we build it?
We used a DragonBoard 410c with the Debian Linux RTOS, and using an Arduino Uno we were able to serially send data from the sensor to a Python client on the DragonBoard. The client would then connect to a Google Cloud VM server we built also using Python and would text you with updates via Twilio! The floating HotNoodle device was built using popsicle sticks and hot glue with a cut-up pool noodle, and is motor-powered with a 3D-printed propeller.

# What challenges did we face?
Many!! Our first challenge was not being able to use the pH sensors that were available to us due to issues reading from the device, we believe it to be a hardware issue. So we then switched to temperature sensing and the next challenge was using the Mezzanine suite provided to us by MLH to interface with the DragonBoard. We decided to ditch that in favor of a much more usable Arduino Uno since that was basically the same exact interface. Learning how to navigate the DragonBoard was definitely challenging since it was an on-board RTOS with Debian and presented its own host of issues we had to work around. At first we had a Java server with a Python script on the Google Cloud VM but decided to ditch the Java server in favor of a replica Python server. Networking was also spotty. 3D printing was actually quite a big challenge because even a millimeter off can make a big difference and some of the prints failed as well and were very time-consuming. The final challenge was staying up late to make everything look polished and nice!!

# What did we learn while building this?
A LOT. How to solder, how to use a Debian Linux RTOS on a DragonBoard, how to create a Python client/server, how to build a flotation device, how to create beautiful documentation, how to use Google Cloud VM, how to read data from a temperature sensor, how to create an Arduino project, how to network, how to 3D print a propellor/motor system, and how to troubleshoot!

# What's next for our project?
We'd like to potentially improve this product into a better smart home product for your pool that consumers can easily use and add on more sensors like pH sensing, chlorine sensing, detecting if someone peed in your pool, or maybe even some RGB lighting!

# What did we build it with?
Python, Google Cloud VM, DragonBoard 410c, Arduino Uno, 3D-Printing, Pool Noodle, Popsicle Sticks, DC Motor w/ 9V battery, Debian Linux, Hot Glue, Waterproof Temperature Sensor, and countless man hours of blood, sweat, and tears.
