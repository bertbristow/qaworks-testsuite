# learning-nightwatch
Learning nightwatch.js through an assignment.

## Pre-requisites

1. [NodeJS](https://nodejs.org/en/) - Downloads and installation instructions can be found on [the official website](https://nodejs.org/en/).

## Setting-up

1. Clone and change-directory to the project
    
    ```console
    $ git clone https://github.com/bertbristow/qaworks-testsuite.git
    Cloning into 'qaworks-testsuite'...
    remote: Counting objects: 30, done.
    remote: Compressing objects: 100% (21/21), done.
    remote: Total 30 (delta 9), reused 26 (delta 7), pack-reused 0
    Unpacking objects: 100% (30/30), done.

    $ cd qaworks-testsuite
    ```

2. Install npm packages (nightwatch)

    ```console
    $ npm install
    ```

3. Define a `npm-do` function for easily accessing npm executables.

    ```console
    $ function npm-do { (PATH=$(npm bin):$PATH; eval $@;) }
    ```


## Running the test

```console
$ npm-do nightwatch
Starting selenium server... started - PID:  20901

[Contact Us] Test Suite
===========================

Running:  QAWorks Contact Us
No assertions ran.

```


## Platform limitations

This should run on any Unix-like operating system. It has only been tested in Ubuntu 17.10 so far though.

## Bugs

Currently, the _Contact Us_ page has a bug, and doesn't work as intended. Upon submitting the form, it shows an error. Pls see screenshot
