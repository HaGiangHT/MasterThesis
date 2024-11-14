# Resoruce-Aware Active Learning for Object Detection 

Master-Thesis of Ha Giang Hoang Tran

# Abstract
Autonomous driving is currently one of the topics where intensive research has been done over the last
few years. One of the crucial aspects of it is safety through environmental perception. Thus, object
detection is an important technology to get to know the surroundings, requiring object detection models
based on deep neural networks (DNN). However, these models require a large amount of annotated
data. Exchanging the data through the vehicular network for model training would result in a network
overload because these DNN-based models require huge amounts of data.
Active Learning is a training method that selects informative samples from the dataset and therefore
reduces the amount of required training data. Recent researches dealing with active learning for object
detection (ALOD) however provide the dataset for the active learning cycle in a centralized manner.
Therefore, this thesis proposes a distributed ALOD by dividing the active learning cycle into two parts,
similar to a server-client architecture. This design imitates a deployment of the ALOD framework into
real-world scenarios. Hence, the clients are responsible for collecting and selecting the most useful
samples. These selected samples are transmitted by considering the network utility. Consequently, this
aims to reduce the amount of data that is transferred in the vehicular network compared to the approach
that would send every collected sample. On the other hand, the server receives these selected samples,
provides them to an annotation process, and trains the model. Furthermore, it provides for the clients,
class balance values as feedback, enabling them to refine their selection. The approach was evaluated by
using the YOLOv8 model and the nuImages dataset. The results showed that the proposed approach is
capable of reaching nearly similar performance scores as the typical centralized ALOD approach.
