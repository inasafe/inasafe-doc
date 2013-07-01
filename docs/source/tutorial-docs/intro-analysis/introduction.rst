Introduction
============

Learning Objectives
--------------------

* Understand the concept of GIS
* Understand the benefits of GIS in informing contingency plan 
* Understand the use of QGIS/InaSAFE
* Understand the benefits of using QGIS/InaSAFE for developing disaster scenario to inform contingency planning


Data vs. Information
--------------------

In the first unit, we looked at OpenStreetMap and how to collect data and add it to the worldwide map.  But what do we mean when we say that we collect data?  Is this the same as collecting information?  Well, not exactly.


Data is raw facts.  Information is data that is organized and presented in such a way as to be useful.  In other words, when we go mapping to collect locations and facts about those locations, we have collected data - we have collected facts.  To turn this data into information, we must make sense of it.  We must present the data in such a way that it can be easily understood.


OpenStreetMap data is already made informative in an obvious way.  The map that you see when you visit the OSM website is there because a computer has processed all of the OSM data and used it to paint a nice looking map.  The map is informative, and useful for us to see where places are in relation to us.


In this unit we will take this even further.  We will learn how to perform geographic data analysis, and thereby learn how to make our data more useful, informative, and effective.


What is a Geographic Information System (GIS)?
----------------------------------------------

A Geographic Information System (GIS) is a system designed to enable people to work with data related to places on the Earth.  A GIS allows the creation, storage, manipulation, and analysis of geographic data.  GIS is a very broad concept and can involve complex hardware and software.  But for most people’s purposes, a simple GIS software application is all that is required, and in this unit we will learn how to use the excellent open-source application, Quantum GIS.


GIS provides different ways to analyze data.  It enables us to ask complex questions, such as:
* *where are all schools with more than 100 students?*
* *how many children live in a certain district?*
* *How many women live within 500 meters of a certain hospital?*
* *What is the shortest walking path from a given point to a hospital?*


GIS helps us to answer these sorts of questions.  In the previous unit we learned how to collect data, and in this unit we will see how to analyze it.
 
GIS for Preparing Contingency Plans
-----------------------------------

GIS has an important role in contingency planning.  A contingency plan is intended to support community preparedness to anticipate the arrival of a potentially hazardous event, such as an earthquake or tsunami. [a] The purpose of such a plan is to minimize casualties and losses in case of such an event.


Before contemplating a contingency plan, one must first consider potential disaster scenarios.  A good plan will likely answer questions such as:
* *what sort of disaster would be likely to happen?*
* *how widespread will the impact be?*
* *who is responsible for helping?*
* *what can be given as aid?*
* *where are the priority areas?*


In other words, a contingency plan answers the question, ***who does what, where and when?***


A Geographic Information System is able to help planners answer these questions, especially the important spatial elements of contingency planning.  GIS may be used to model hazardous events so that they can be better predicted and reduce risk.  It may be used to plan evacuation routes prior to a disaster.  When a disaster occurs, GIS may also play a role in the emergency response phase.  It can be used to map the area affected and position of refugee camps, so that helpers can be directed to the most useful locations to aid those affected.  After a disaster, GIS may also be used to plan for rehabilitation and reconstruction.  Overall, GIS helps to perform analysis of a disaster, damage and losses caused, and opportunities for reducing risk.


The Importance of Data
We previously learned how to start collecting exposure data.  When thinking about GIS it is important to remember that if your data is bad, your analysis will be bad also.  Hence the more detailed and accurate your data is, the better your analysis and action may be during a disaster.


As we shall see in this unit, some data may be obtained from various agencies that specialize in certain kinds of data.  For example, we will obtain our hazard models (hazard data) from various organizations that specialize in this.  As for exposure data, some data we may find through agencies, such as population data.  For ever important infrastructure data, collecting data at a community level is key, which is why in the previous unit we learned how to utilize the crowd-sourced OpenStreetMap platform.


QGIS and InaSAFE
Quantum GIS (QGIS) is a user friendly open-source Geographic Information System (GIS).  It runs on Windows, Mac OSX, and Linux.  QGIS provides a continually growing number of capabilities provided by core functions and plugins.  You can visualize, manage, edit, analyze data, and compose printable maps.


QGIS is awesome because:
1. It’s completely free.  It doesn’t cost anything.
2. It’s free, as in liberty.  If you think a feature is missing, you can sponsor the development of a feature, or add it yourself if you are familiar with programming.
3. It’s constantly developing and improving.  Because many people continue adding features, it keeps getting better.
4. Extensive help and documentation is available.  If you have problems you can always turn to the software documentation, other QGIS users, or even the developers.


QGIS has many plugins which extend the core functionality of the software.  One of these plugins is InaSAFE, which can be used to analyze the impact of a disaster and create a list of actions needed to be taken when a disaster occurs.  QGIS and InaSAFE can also help to determine the location of ideal places of refuge, evacuation routes, areas likely to be damaged, and more.





InaSAFE provides overviews of potential disaster scenarios, of their outcomes, as well as maps which can aid decision makers when disaster strikes.  Maps are an effective way of communicating disaster impact, but showing in a simple way the areas of damage, such as the extent of flood-affected areas and buildings affected by a flood.


In the preface to this guide you may have followed along in our optional quickstart guide to using InaSAFE.  If you followed the steps in this chapter, then you have already installed QGIS and InaSAFE and seen them in action.  If you haven’t, don’t worry, we’ll go through the steps again in this unit.
[a]Kate Chapman:
should it be more than community preparedness? (Kate look for contingency plan definition from AIFDR)