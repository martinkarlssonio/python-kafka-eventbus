# Eventbus written in Python based on Kafka
### Decouple your BackEnd with Eventdriven architecture

<!--
*** Written by Martin Karlsson
*** www.martinkarlsson.io
-->

[![LinkedIn][linkedin-shield]][linkedin-url]


<!-- ABOUT THE PROJECT -->
## About The Project

Purpose for this tutorial is to show how to build a de-coupled, eventdriven, microservices architecture based on Kafka.

![Architecture overview][arch]

### Pre-requisite
- Ensure Python3 is installed.
- Ensure Docker is installed.
- Execute `pip3 install -r requirements.txt`

### Start

Execute `sudo python3 start.py` to start the Kafka containers and listener.py.

### Test

Execute `python3 testProducer.py` to produce two new events.
One of them has a configuration in "eventConfig/integration.json" with an action to start a Docker Container (hello-world), and the other one will just log out a message to the Terminal.

<!-- CONTRIBUTING -->
## Contributing

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/featureName`)
3. Commit your Changes (`git commit -m 'Add some featureName'`)
4. Push to the Branch (`git push origin feature/featureName`)
5. Open a Pull Request


<!-- CONTACT -->
## Contact

### Martin Karlsson

LinkedIn : [martin-karlsson][linkedin-url] \
Twitter : [@HelloKarlsson](https://twitter.com/HelloKarlsson) \
Email : hello@martinkarlsson.io \
Webpage : [www.martinkarlsson.io](https://www.martinkarlsson.io)


Project Link: [github.com/martinkarlssonio/python-kafka-eventbus](https://github.com/martinkarlssonio/python-kafka-eventbus)


<!-- MARKDOWN LINKS & IMAGES -->
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/martin-karlsson
[arch]: arch.png