# GFS MLModel

GFS MLModel is a stack to build, traind and test one or multiple Machine Learning models with a docker container as quickly as possible.  
It provides a lot of boilerplate code to help you develop and deploy to production your models.  
The stack runs models in the backend and provides, through Flask, a very efficient and robust API to use and monitor your models.  
Perfect match if you use the GFS-Stack.

Technologies used in the stack:

-   Flask
-   Huggingface
    transformer, huggingface_hub
-   Tensorflow
-   Keras (Tensorflow)
-   Jax
-   Pandas

## Intro and Credits

S

## To Start

git clone
make init
login hf hub

## To Production

dokerize and run locally or push to a server, where you can run models or just push the build to be run constantly.

## Useful Commands

## Stack Structure

## Basics - How to move around

## Note

1. add flask 'TEMPLATES_AUTO_RELOAD': True // hot reload doesn't work
2. How to manage ENVs in (local environment, done) docker

Later notes: 0. flask graceful shutdown in prod?
