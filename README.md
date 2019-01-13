本项目中除了助教提供的代码外，自己的代码有5个，分别是myAgent.py;myAgent_train_online.py;myAgent_256_train.py;myAgent_512_train.py;myAgent_1024_train.py。
第一个myAgent继承了助教提供的Agent类。 
第二个myAgent_train_online是在线学习的代码，基本思路是加载自己的和expectimax模型，根据expectimax生成正确方向并存储，之后再fit自己的模型并保存。 
后三个文件是离线学习的文件，由于一些原因我没法获得大量的数据集，因此这个离线学习的代码到后来就不使用了，不过离线学习学到的三个模型可以直接拿来给在线学习使用。 
使用我的agent的方法就是修改evaluate.py语句，变成“from game2048.myAgent import myAgent as TestAgent”。 
在运行model的过程中，可能需要根据实际情况，修改load model语句中model的路径。
三个model可通过https://pan.baidu.com/s/1mIs4Tih8gUY5uApXDJzNMA 下载
