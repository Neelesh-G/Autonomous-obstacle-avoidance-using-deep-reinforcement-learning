Obstacle avoidance using Deep reinforcement learning
  * The above is the implementation of obstacle avoidance using reingorcement learning in raspberry pi 3.
  * The code is writtern for a bot with three ultrasonicc sensors only
  * The below pic is what the bot looks like
![bot](https://user-images.githubusercontent.com/72451756/95423894-71293080-095f-11eb-81a0-7bcf6f1fed14.jpeg)
![bot2](https://user-images.githubusercontent.com/72451756/95425944-be5ad180-0962-11eb-9479-89aac81d6e8f.jpeg)
  
  *In order to run the code pytorch must be installed.
  
  Install Pytorch on raspberry pi  [**here**](https://wormtooth.com/20180617-pytorch-on-raspberrypi/)
 
  *The network contains 3 inputs from each of the sensors and three action outputs(right,left,straight).It consists of one hidden layer with 60 neurons.
  
  
  *In order to start the training connect to raspberry pi and run environment.py.A lastbrain.pth file will be created to save the weights and the model whenever training is     stopped which would be loaded again from the same checkpoint when the training is resumed.
  
  [**Click link to view the video for the trained bot**](https://photos.google.com/share/AF1QipMxLZVE02uz_t9IwG3EcjsDQ8wOdn3wYDOjhKieswX3YYoc6S8a_1FijJo_Ep6mOA?key=bEtvbEZfNWh1VkZoOWtqeDhtRjVmaFVRSXgwSW9R)
