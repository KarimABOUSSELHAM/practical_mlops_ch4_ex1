[![CI/CD flask container app](https://github.com/KarimABOUSSELHAM/practical_mlops_ch4_ex1/actions/workflows/docker-build.yml/badge.svg)](https://github.com/KarimABOUSSELHAM/practical_mlops_ch4_ex1/actions/workflows/docker-build.yml)  

This repository exposes a solution to the exercise n° 1 of the chapter 4 of Gift, N., & Deza, A. (2021). [*Practical MLOps Operationalizing Machine Learning Models*](https://www.oreilly.com/library/view/practical-mlops/9781098103002/). O'Reilly Media.  
  
# Exercise n° 1 statement

`Create your own Flask application in a container, publish it to a GitHub repository, document it thoroughly, and add GitHub Actions to ensure it builds correctly.`

# Answer documentation

In this exercise I chose to use the flask app defined in the exercises set of the previous chapter.  

We don't need to push the image by itself to the github repository: First, because github has a normal file limit of 100 MB as mentioned in page 100 of the book. Second, because github actions will do the job to test the container builds correctly as required in the exercise statement and third, because a Dockerfile
is enough to expose all the instructions needed to define the container.  

For all of the aforementioned considerations I think answers to exercises 3 and 4 of chapter 3 fully satisfy this portion of the current exercise `Create your own Flask application in a container`.  

The `yml` workflow ingested by github actions will run the following steps:  

1) Checkout the code; 
2) Set up QEMU for multi platform support (optional);   
3) Set up docker;  
4) Build the docker image;  
5) Run the container;  
6) Test the "GET" endpoints of the flask application;  
7) Stop the docker container and remove it.  


