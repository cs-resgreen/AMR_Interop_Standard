# MassRobotics Autonomous Mobile Robot Interoperability Standard - MQTT Revision

TL:DR; This is an MQTT revision of the MRAMRIS(See name above) but with an MQTT backbone. This is a tweak on the original source here: https://github.com/MassRobotics-AMR/AMR_Interop_Standard/pull/10

This is a revision of the Mass Robotics Interop Standards MQTT publisher and subscriber project. The main changes are adding another level of nesting to the statusReport topics so it is nested under its UUID. This allows us to have multiple topics per different devices without needing to parse lots of unnecessary messages for other devices that also have a statusReport. the # symbol is a wildcard allowed by mosquito client for Subscribers only. Use this carefully!

[![MassRobotics AMR Interop](https://www.massrobotics.org/wp-content/uploads/2015/05/AMR_interop_MR-logo-scaled.jpg)](https://www.massrobotics.org/project/amrinteroperability/)

The MassRobotics AMR Interoperability Standard aims to help enable organizations to deploy autonomous mobile robots AMRs from multiple vendors and have them coexist effectively, better realizing the promise of warehouse and factory automation. This standard will allow autonomous vehicles of different types to share information about their robot(s) location, speed, direction, health, tasking / availability and other performance characteristics with other similar vehicles to help them be better teammates on a warehouse or factory floor.  Furthermore, it allows human agents to provide a similar set of information (through the use of external mobile devices) so that their work can be orchestrated alongside robots.

This project contains a schema definition file (AMR_Interop_Standard.json); a detailed description of the standard (AMR_Interop_Standard.pdf); an example implemetation of a client (MassRobotics-AMR-Sender), and a server (MassRobotics-AMR-Receiver); as well as some example messages.  The client and server each have their own README files describing their installation and usage.

For more information or to provide feedback on the standard, please visit: https://www.massrobotics.org/project/amrinteroperability/.
