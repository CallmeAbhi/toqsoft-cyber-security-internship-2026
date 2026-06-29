# Week 3 Day 2 – Website Availability Checker

## Objective

Develop a Python program that checks whether a website is reachable by sending an HTTP request.

## Features

* Accepts a website URL from the user.
* Automatically adds `https://` if the protocol is not provided.
* Checks website availability using the Requests library.
* Displays:

  * URL
  * Website Status
  * HTTP Status Code
  * Response Time
  * Date & Time
* Handles common network errors such as:

  * Invalid URL
  * DNS Lookup Failure
  * Connection Error
  * Timeout
  * SSL Error
* Saves the result to `results.txt`.

## Technologies Used

* Python
* Requests
* Time
* Datetime

## Outcome

Successfully developed a Website Availability Checker that verifies website accessibility, measures response time, handles common network-related errors, and generates a formatted report for every execution.
