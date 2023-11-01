Steps followed when setting up the stack:
1. Use Spring initializer to create app template using the following dependencies Spring Web, Spring Data JPA, and MySQL Driver
2. Initialize mysql (either locally or in a container) -> https://hub.docker.com/_/mysql/
3. 



### Shell error
If you get an error warning about a syntax error while running your code like the one below:
```
 > [app 3/3] RUN sh ./mvnw install:
: not foundw: line 20:
: not foundw: line 35:
0.306 ./mvnw: line 56: syntax error: unexpected word (expecting "in")
```

The reason could be that you are using a Windows OS and when you pull the image from github, it replaces 
```LF``` with ```CRLF``` for line breaks in the ./mvnw shell file. You can fix it by creating a new project folder
running the following commands:
```
git init
git config --local core.autocrlf false
```
Continue with normal install.

