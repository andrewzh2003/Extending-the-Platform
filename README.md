Assignment 4: Extending the Platform

This assignment includes the following starter files:

* __a4.py__: Use this file as the main module for your program.
* __OpenWeather.py__: Use this file as your module for the OpenWeather API.
* __LastFM.py__: Use this file as your module for the LastFM API.
* __WebAPI.py__: Use this file to implement common features for API modules.

Introduction
In assignment 3, you learned how to write a program that connects to and shares information with a program running on another computer. The systems we write programs for today are almost always connected to other computers in some capacity. Whether it is your computer operating system sending data back to its creator, your web browser automatically downloading updates, or you reaching out to friends and family for a video chat, nearly all the programs we use today rely on networked communication to extend their capabilities.

While your Distributed Social (DS) program has the ability to accept, store, and distribute information written by your users, it doesn’t yet take advantage of the vast wealth of information available to networked programs today. So for this assignment we are going to be extending the DS platform by adding some new features for the users of your program.

You have probably noticed how in programs like Slack, Discord, and Facebook Messenger, keywords can be entered into chat conversations that trigger some sort of automatic inclusion or formatting. In computer science, this process is called transclusion, which basically refers to the process of using a linking syntax to connect or include content from one source into the content of another. For this assignment, you will be enhancing the post writing feature you created in assignment 3 by adding support for keyword transclusion.

By now, you should have had a chance to digest some of the core principles of networked communication. You have learned about protocols, sockets, and request/response communication with a server. Your work for assignment 4 will focus on locking in these concepts as well as exploring some new ones.

Summary of Program Requirements
Connect to and retrieve data from at least 2 web API’s using Python’s urllib module.

Use transclusion to parse and replace keywords in a journal entry with content from web API’s.

Write classes to manage your APIs.

Learning Goals
How to work with public API’s

Know when and how to write a class

Understand and handle failures when communicating over HTTP

Use inheritance to extend class functionality

Program Requirements
Your main entry point to your program will be from a module called a4.py. As with a3, you will not have a validity checker to use for testing and you will be largely responsible for program input and output. You are encouraged to continue to bring the user interface and other functions you created in your a1.py through a3.py modules, but you will not be re-graded on the features you implemented for those assignments.

Your final program should contain the following new modules:

OpenWeather.py: A module for interacting with the OpenWeather API. See Part 1

LastFM.py: A module for interacting with the Last.FM API. See Part 2

ExtraCreditAPI.py: A module for interacting with an API of your choice, should you choose to earn extra credit. See Extra Credit

WebAPI.py: A base class module that provides access to common features for your API modules. See Part 3: The Refactor!

Since the code you write for this assignment will still be dependent on communication with the server, you should also include all modules you created or used for assignment 3.
